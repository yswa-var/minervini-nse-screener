# NSE-Stock-Dashboard

<h1>iterating through (TOP 30-NIFTY50) downloading 1Y data in '1D candle' into csv.</h1>

-calculating:

	# Condition 1: Current Price > 150 SMA and > 200 SMA
	# Condition 2: 150 SMA and > 200 SMA
	# Condition 3: 200 SMA trending up for at least 1 month
	# Condition 4: 50 SMA> 150 SMA and 50 SMA> 200 SMA
	# Condition 5: Current Price > 50 SMA
	# Condition 6: Current Price is at least 30% above 52 week low
	# Condition 7: Current Price is within 25% of 52 week high

<p>-if all condition match = "selected stocks to invest": exportList</p>
