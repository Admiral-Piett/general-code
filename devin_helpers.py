from tabulate import tabulate as tb
import json


# Pretty prints dataframes for me in an easier way than typing the full command each time
def dfpp(df, head=''):
    if head == 'yes':
        print tb(df.head(), headers='keys')
    else:
        print tb(df, headers='keys')


# Converts lists to strings
def convertToString(value):
    strValue = ''
    for v in value:
        strValue = strValue + str(v) + ','
    strValue = strValue[:-1]

    return strValue


def columnCount(dataframe):
    headerList = dataframe.columns
    count = -1

    for v in headerList:
        count = count + 1
        print str(v) + " - " + str(count)


def jsonpp(js):
    print json.dumps(js, indent=4)