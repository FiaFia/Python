import csv
import re


def extract_all(filename):
    result =[]
    
    print('Extracting data----')

    lines = open(filename, 'r', encoding='utf8', errors='ignore').readlines()
    
    for line in lines:
        if "BDt;" in line:
            tradableid = None
            exchange = None
            symbol = None
            name = None
            isin = None
            currency = None
            instrumentSubType = None
            country = None
            securityType = None
            newsitem = None
           
            tradableid = re.findall(r";i(.+?);",line) 
            exchange = re.findall(r";Ex(.+?);",line)
            symbol = re.findall(r";SYm(.+?);",line)
            name = re.findall(r";NAm(.+?);",line)
            isin = re.findall(r";ISn(.+?);",line)
            currency = re.findall(r";CUt(.+?);",line)
            instrumentSubType = re.findall (r";INt(.+?);",line)
            country = re.findall(r";CNy(.+?);",line)
            securityType = re.findall(r";STy(.+?);",line)
            lotSize = re.findall(r";LSz(.+?);",line)
             
            newsitem = [tradableid[0],exchange[0],symbol[0],name[0],isin[0],currency,instrumentSubType[,country,securityType[0],lotSize[0]]  
            result.append(newsitem)
        
    
    return result


def writetocsv(newsitems, reportfile):
    
    print('Start writing to csv')
    
    if newsitems:
        with open(reportfile, mode='w+', encoding='utf8', errors='ignore') as csvfile:
            writer = csv.writer(csvfile,lineterminator='\n')
            writer.writerow(['TradableID','Exchange','symbol','Name','isin','currenty','instrumentSubType','country','securityType','lotSize']) 
        
            for i in range (0, len(newsitems)):
                writer.writerow(newsitems[i])
   
    print('csv written done')
    return


if __name__ == '__main__':
    filename = 'XSTO_Stock_BasicData0725'
    data_file = filename  +'.tip'
    reportcsv = 'BDt_' + filename + '.csv'
    
    newsitemsum = extract_all(data_file)
    writetocsv(newsitemsum, reportcsv)
