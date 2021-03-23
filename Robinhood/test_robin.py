from Robinhood import Robinhood

qr_code = 'JVHN6WPKZ5YDPTXR'
robinhood_client = Robinhood()
robinhood_client.login(username='svalenzuela8@miners.utep.edu', password='Svelty+Car0+2o16!', qr_code=qr_code)


# # summary of your current portfolios
robinhood_client.portfolios()


# # Current positions and history positions
# robinhood_client.positions()

# # Get stock information, url needed to make buy/sell order.
# # Note: Sometimes more than one instrument may be returned for a given stock symbol
stock_instrument = robinhood_client.instruments('MSFT')[0]
print(stock_instrument)

# # Get a stock's quote
# stock_quote = robinhood_client.quote_data('MSFT')

# # Market price
# print(stock_quote['last_trade_price'])

# # one week of 5minut OHLC info, you can change '5minute' to '10minute'|'30minute'
# robinhood_client.get_historical_quotes('MSFT', '5minute','week')

# # one week of daily OHLC info, 
# robinhood_client.get_historical_quotes('MSFT', 'day','week')

# # one year of daily OHLC info,
# robinhood_client.get_historical_quotes('MSFT', 'day','year')

# # marekt dorder 
# stock_instrument = robinhood_client.instruments('DWT')[0]
# buy_order = robinhood_client.place_market_buy_order(stock_instrument['url'], 'DWT', 'GFD', 1)
# sell_order = robinhood_client.place_market_sell_order(stock_instrument['url'], 'DWT', 'GFD', 1)

order = robinhood_client.place_limit_buy_order(stock_instrument['url'], 'DWT', 'GTC', 4.1, 1)

# order_id = order.json()['id']
# cancel_order = robinhood_client.cancel_order(order_id)

# # staus code is 200 means order is successfully cancelled.
# print(cancel_order.status_code)

# # Order history for the account
# robinhood_client.order_history()