import csv
import plotly.express as px
import numpy as np


def getDataSource():
    temp=[]
    iceCreamSale=[]

    with open('data1.csv', newline='') as f:
        reader = csv.DictReader(f)
        for i in reader:
            temp.append(int(i['Temperature']))
            iceCreamSale.append(int(i['Ice-cream Sales']))

    return{'x':temp, 'y':iceCreamSale}

def getCorelation(dataSource):
    corelation=np.corrcoef(dataSource['x'], dataSource['y'])
    print(corelation[0,1])

def setup():
    dataSource=getDataSource()
    getCorelation(dataSource)

setup()
