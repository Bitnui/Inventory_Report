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

def sort_by_price(kw,price):

    df = pd.read_csv(f'{kw}_data.csv')
    df = df.loc[df['Price'] == price]
    df.to_csv(kw + '_data.csv')
    return df

def subtract_retail(amount,kw):
    df = pd.read_csv(f'{kw}_data.csv')
    df.loc[:, "Price"] = df["Price"].apply(lambda x: x - amount)
    return df 

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

def final_filter(kw,retail,wholesale):
    df = pd.read_csv(f'{kw}_data.csv')
    sort_by_price(kw,retail).to_csv(f'{kw}_data.csv')
    subtract_retail(wholesale,kw).to_csv(f'{kw}_data.csv')

def total(kw):

    sort_by_kw(kw)
    df = pd.read_csv(f'{kw}_data.csv')
    match kw:
        case 'Melt':
            final_filter(kw,5.99,4.99)
        case 'Candle':
            final_filter(kw,14.99,9.99)
            #final_filter(kw,12.5,7.5)
            #final_filter(kw,19.99,14.99)
        case '10 Ounce':
            final_filter(kw,19.99,14.99)
        case '5 Pack':
            final_filter(kw,19.99,14.99)
        
    calculate_total(kw)
    clean(kw)


# Ask Question
kw = str(input("What's the keyword? (Melt, Candle, 10 Ounce, 5 Pack)"))
# Call Function
total(kw)

