# -*- coding: utf-8 -*-
"""
Created on Mon Aug 29 22:03:24 2022

@author: Kaptan
"""

from pandas_datareader import data as pdr
import yfinance as yf
import pandas as pd
import datetime
import time
import os
import requests
#import time
#import schedule
#import requests
#from quote import quote

yf.pdr_override()

#Smallcap  top50 ::::medium volitile::: only good for bull run
#url = "https://www1.nseindia.com/content/indices/ind_niftysmallcap50list.csv"

#multicap500: large cap - 50%, midcap - 25%, smallcap - 25% ::::diversified::: 
#url = "https://www1.nseindia.com/content/indices/ind_nifty500Multicap502525_list.csv"

#Smallcap 250 #::::very high volatility::: riskey!
#url = "https://www1.nseindia.com/content/indices/ind_niftysmallcap250list.csv"

#microcap 250 #:::::v.v.v high volatility:::: can be worthless
#url = "https://www1.nseindia.com/content/indices/ind_niftymicrocap250_list.csv"

#nifty top 100 ::::low risk::: average returns::::
url = "https://archives.nseindia.com/content/indices/ind_nifty100list.csv"

def telegram_bot_sendtext(bot_message):
    
    bot_token = "5781922280:AAH23xtyuJo4hqPcxnJlExi7_Pq0MbxYz_0"
    #bot_chatID = '-1001541599572' #telegram #group
    bot_chatID = '5562607566' #telegram personal "yash"
    
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)

    return response.json()

def main(cunt=0):
    ticker_list = pd.read_csv(url)+".NS"
    
    index_name = '^NSEI'
    start_date = datetime.datetime.now() - datetime.timedelta(days=365)
    end_date = datetime.date.today()
    exportList = pd.DataFrame(columns=['Stock', "RS_Rating", "50 Day MA", "150 Day Ma", "200 Day MA", "52 Week Low", "52 week High"])
    returns_multiples = []
    
    index_df = pdr.get_data_yahoo(index_name, start_date, end_date)
    index_df['Percent Change'] = index_df['Adj Close'].pct_change()
    index_return = (index_df['Percent Change'] + 1).cumprod()[-1]
    for ticker in ticker_list.Symbol:
        print(ticker)
        df = pdr.get_data_yahoo(ticker, start_date, end_date)
        cunt = cunt+1
        if(os.path.isfile(f'data/{ticker}.csv')):
            os.remove(f'data/{ticker}.csv')
            print(f'{ticker}.csv  is removed')
        df.to_csv(f'data/{ticker}.csv')
        print(cunt)
    
        
        df['Percent Change'] = df['Adj Close'].pct_change()
        stock_return = (df['Percent Change'] + 1).cumprod()[-1]
        
        returns_multiple = round((stock_return / index_return), 2)
        returns_multiples.extend([returns_multiple])
        
        print (f'Ticker: {ticker}; Returns Multiple against NIFTY 50: {returns_multiple}\n')
        time.sleep(1)
        
    rs_df = pd.DataFrame(list(zip(ticker_list.Symbol, returns_multiples)), columns=['Ticker', 'Returns_multiple'])
    rs_df['RS_Rating'] = rs_df.Returns_multiple.rank(pct=True) * 100
    rs_df = rs_df[rs_df.RS_Rating >= rs_df.RS_Rating.quantile(.70)]
    
    rs_stocks = rs_df['Ticker']
    for stock in rs_stocks:    
        try:
            df = pd.read_csv(f'data/{stock}.csv', index_col=0)
            sma = [50, 150, 200]
            for x in sma:
                df["SMA_"+str(x)] = round(df['Adj Close'].rolling(window=x).mean(), 2)
     
            currentClose = df["Adj Close"][-1]
            moving_average_50 = df["SMA_50"][-1]
            moving_average_150 = df["SMA_150"][-1]
            moving_average_200 = df["SMA_200"][-1]
            low_of_52week = round(min(df["Low"][-260:]), 2)
            high_of_52week = round(max(df["High"][-260:]), 2)
            RS_Rating = round(rs_df[rs_df['Ticker']==stock].RS_Rating.tolist()[0])
            
            try:
                moving_average_200_20 = df["SMA_200"][-20]
            except Exception:
                moving_average_200_20 = 0
    
            condition_1 = currentClose > moving_average_150 > moving_average_200
            condition_2 = moving_average_150 > moving_average_200
            condition_3 = moving_average_200 > moving_average_200_20
            condition_4 = moving_average_50 > moving_average_150 > moving_average_200
            condition_5 = currentClose > moving_average_50
            condition_6 = currentClose >= (1.3*low_of_52week)
            condition_7 = currentClose >= (.80*high_of_52week)
            
            if(condition_1 and condition_2 and condition_3 and condition_4 and condition_5 and condition_6 and condition_7):
                exportList = exportList.append({'Stock': stock, "RS_Rating": RS_Rating ,"50 Day MA": moving_average_50, "150 Day Ma": moving_average_150, "200 Day MA": moving_average_200, "52 Week Low": low_of_52week, "52 week High": high_of_52week}, ignore_index=True)
                print (stock + " made the Minervini requirements")
        except Exception as e:
            print (e)
            print(f"Could not gather data on {stock}")
    
    exportList = exportList.sort_values(by='RS_Rating', ascending=False,ignore_index=True)
    print('\n', exportList)
    
    expl = exportList.Stock
    """
    compare the new companies with previous
    """
    time.sleep(3)
    
    #telegram sender
    time.sleep(1)
    telegram_bot_sendtext("-----hi-------")
    
    telegram_bot_sendtext("This group is for education purpose only!")
    telegram_bot_sendtext("----Index used Niftysmall250------")
    
    
    #writer = ExcelWriter("ScreenOutput.xlsx")
    #exportList.to_excel(writer, "Sheet1")
    #writer.save()
    
    
    #spit top 5 stocks
    for ticker in expl.head(5):
        Remove_last = ticker[:-3]
        my_message = Remove_last
        telegram_bot_sendtext(my_message)
        time.sleep(2)
    
    telegram_bot_sendtext("-----end-------")
    
main()