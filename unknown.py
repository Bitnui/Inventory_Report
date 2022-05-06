# Read Restock report possibly?
# Get total stock and * by price (Posiblly overwrite total stock with price)
# Output price and add up the whole column?
# Figure out the UI problem (So dad can use it)
import pandas as pd
df = pd.read_csv('restock_report.csv')

def sort_by_kw(kw):

    df = pd.read_csv('restock_report.csv')
    df = df[df['Product name'].str.contains(kw)]
    df.to_csv(kw + '_data.csv')

def further_filtration(kw):
    df = pd.read_csv(f'{kw}_data.csv')
    df = df[df['Price']
    df.to_csv(kw + '_data.csv')

def subtract_retail(amount,df):

    df.loc[:, "Price"] = df["Price"].apply(lambda x: x - amount)

def calculate_total(kw):

    df = pd.read_csv(f'{kw}_data.csv')
    total_Price = df.assign(Total_price= lambda x: df['Price'] * df['Total Units'])
    total_Price.to_csv('Total_Price.csv')
    sort = pd.read_csv('Total_Price.csv')
    sort.sort_values(by=['Total_price'],inplace=True,ascending=False)
    inv_price_sum = sort['Total_price'].sum()
    print(f'Total Inventory of {kw} is ${inv_price_sum}')
    total_inventory_amount = sort['Total Units'].sum()
    print(f'Total Units of {kw} is {total_inventory_amount}')

def clean(kw):

    import os 
    os.remove(f'{kw}_data.csv')
    os.remove('Total_Price.csv')

def total(kw):

    sort_by_kw(kw)
    df = pd.read_csv(kw + '_data.csv')
    match kw:
        case 'Melt':
            subtract_retail(4.99,df)
            print('Melt')
            #Further filtration on Melt Data (Based on price)
            further_filtration()
            df.to_csv(f'{kw}_data.csv')
        case 'Candle':
            subtract_retail(10,df)
            print('6 oz')
            df.to_csv(f'{kw}_data.csv')
        case '10 oz':
            subtract_retail(14.99,df)
            df.to_csv(f'{kw}_data.csv')
        case '5 pack':
            subtract_retail(4.99,df)
    calculate_total(kw)
    #clean(kw)



total('Candle')

