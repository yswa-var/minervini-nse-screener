# NSE-Stock-Dashboard
<h1>****website under progress******</h1>
<h3>iterating through (TOP 30-NIFTY50) downloading 1Y data in '1D candle' into csv.</h3>

-calculating:

	# Condition 1: Current Price > 150 SMA and > 200 SMA
	# Condition 2: 150 SMA and > 200 SMA
	# Condition 3: 200 SMA trending up for at least 1 month
	# Condition 4: 50 SMA> 150 SMA and 50 SMA> 200 SMA
	# Condition 5: Current Price > 50 SMA
	# Condition 6: Current Price is at least 30% above 52 week low
	# Condition 7: Current Price is within 25% of 52 week high

<p>-if all condition match = "selected stocks to invest": exportList</p>


![image](https://user-images.githubusercontent.com/65719349/185805148-6a1de0c1-f105-4af5-8ef1-abbc8f635a01.png)


<h2>Ticker List that can be used</h2>
<ul>
<li>Smallcap  top50 ::::medium volitile::: only good for bull run
#url = "https://www1.nseindia.com/content/indices/ind_niftysmallcap50list.csv"</li>

<li>multicap500: large cap - 50%, midcap - 25%, smallcap - 25% ::::diversified::: 
#url = "https://www1.nseindia.com/content/indices/ind_nifty500Multicap502525_list.csv"</li>

<li>Smallcap 250 #::::very high volatility::: riskey!
#url = "https://www1.nseindia.com/content/indices/ind_niftysmallcap250list.csv"</li>

<li>microcap 250 #:::::v.v.v high volatility:::: can be worthless
#url = "https://www1.nseindia.com/content/indices/ind_niftymicrocap250_list.csv"</li>

<li>nifty top 100 ::::low risk::: average returns::::Recomended
url = "https://archives.nseindia.com/content/indices/ind_nifty100list.csv"</li>
</ul>


<h3>!!important</h3>
make sure that there is a folder named "data" in the same directory to store stocks csv data.

<h3>now to back test the stocks</h3>
head here: https://github.com/bbmusa/ibkr-backtest-india-nse
