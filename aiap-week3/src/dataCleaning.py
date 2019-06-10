import pandas as pd
import numpy as np

def dropEntryWithoutCustomerID(df_input):
    df_output = df_input.dropna(axis=0, subset=['CustomerID'])
    return df_output

def dropDuplicatedEntries(df_input):
    df_output = df_input.drop_duplicates()
    return df_output

def removeQuatityLessThanZero(df):
	temp = df[df.Quantity > 0]
	return temp

def featureEngineer(temp):
    intermediate = temp.groupby(['CustomerID']).agg({'InvoiceNo': "nunique",
                                         'StockCode': "nunique",
                                          'Quantity': ["sum",'count'],
                                          'UnitPrice': ['mean','std']})
    
    # Using ravel, and a string join, we can create better names for the columns:
    intermediate.columns = ["_".join(x) for x in intermediate.columns.ravel()]
    
    intermediate['QuantityPerInvoice'] = intermediate['Quantity_sum']/intermediate['InvoiceNo_nunique']
    intermediate['UniqueItemsPerInvoice'] = intermediate['Quantity_count']/intermediate['InvoiceNo_nunique']
    
    intermediate.drop(['Quantity_sum'], axis=1, inplace=True)
    
    intermediate.rename(columns={'InvoiceNo_nunique':'NoOfInvoices','StockCode_nunique':'NoOfUniqueItems',
                             'Quantity_count':'TotalQuantity','UnitPrice_mean':'UnitPriceMean',
                            'UnitPrice_std':'UnitPriceStd'}, inplace=True)
    
    intermediate.fillna(0, inplace=True)
    
    return intermediate

def cleanAndEngineer(df):
	cleanedData = featureEngineer(removeQuatityLessThanZero(dropDuplicatedEntries(dropEntryWithoutCustomerID(df))))

	return cleanedData