import time
import pandas as pd
from sklearn import metrics
from sklearn.model_selection import train_test_split


# Random Forest Classifier
def random_forest_classifier(train_X, train_y):
    from sklearn.ensemble import RandomForestClassifier
    model = RandomForestClassifier(n_estimators=8, max_features=3)
    model.fit(train_X, train_y)  #拟合模型 由X_train, y_train训练数据集建模；
    return model


# Decision Tree Classifier
def decision_tree_classifier(train_X, train_y):
    from sklearn import tree
    model = tree.DecisionTreeClassifier()
    model.fit(train_X, train_y)
    return model


def read_data(data_file):
    col = ['ric']
    col += [str(i) for i in range(50)]
    col += ['label']
    data = pd.read_csv(data_file, names=col)
    # data.head()

    y = data['label'].apply(lambda x : 0 if x is -1 else 1)
    X_train, X_test, y_train, y_test = train_test_split(data.drop(['ric', 'label'], axis=1), y, test_size=0.2, random_state=0)
    return X_train, X_test, y_train, y_test


if __name__ == '__main__':
    data_file = 'C:\\Python36\\TestCode\\RandomForest\\part-00000'
    test_classifiers = ['Random Forest', 'Decision Tree']
    classifiers = {'Random Forest': random_forest_classifier,
                    'Decision Tree': decision_tree_classifier}

    print('****Reading training and testing data...****')

    X_train, X_test, y_train, y_test = read_data(data_file)
    num_train, num_feat = X_train.shape
    num_test, num_feat = X_test.shape
    print('******************** Data Info *********************')
    print('#training data: %d, #testing_data: %d, dimension: %d' % (num_train, num_test, num_feat))

    for classifier in test_classifiers:
        print('******************* %s ********************' % classifier)
        start_time = time.time()
        model = classifiers[classifier](X_train, y_train)
        print('training took %fs!' % (time.time() - start_time))
        predict = model.predict(X_test)  #模型预测, X_test测试数据集预测；对训练数据集测试得分(因为有时根本不知道测试数据集对应的真实y值)
        
        score = model.score(X_test, y_test)
        precision = metrics.precision_score(y_test, predict)
        accuracy = metrics.accuracy_score(y_test, predict)
        # recall = metrics.recall_score(y_test, predict)

        print('Model score is: %.2f%%' % (100 * score))  #评估模型准确率
        print('precision: %.2f%%, accuracy: %.2f%%' % (100 * precision,  100 * accuracy))
        # print('Recall: %.2f%%' % 100 * recall)
