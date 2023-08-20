# coinmarketcap
> A Python class for the API on [CoinMarketCap](https://coinmarketcap.com)

## Requirements
* [Python](https://www.python.org/downloads/)

## API Documentation
- [CoinMarketCap API Documentation](https://coinmarketcap.com/api/documentation/v1/)

## Information
In order to use the CoinMarketCap API, you will need an API key which you can sign up for one [here](https://pro.coinmarketcap.com/signup/).

Data from the API will be cached for 5 minutes at a time (that is how long it takes CoinMarketCap to refresh their data) this way you will not get rate limited.

The class has only 2 main functions, one for global data and one for ticker data.

## Example
```python
from coinmarketcap import CoinMarketCap

CMC  = CoinMarketCap('API_KEY_HERE')

global_data = CMC._global() # Global data example
print('Cryptocurrencies : ' + str(global_data['cryptocurrencies']))
print('Exchanges        : ' + str(global_data['exchanges']))
print('BTC Dominance    : ' + str(global_data['btc_dominance']))
print('ETH Dominance    : ' + str(global_data['eth_dominance']))
print('Market Cap       : ' + str(global_data['market_cap']))
print('Volume           : ' + str(global_data['volume']))

ticker_data = CMC._ticker() # Ticker data example
for item in ticker_data:
    print('ID          : ' + item)
    print('Name        : ' + ticker_data[item]['name'])
    print('Symbol      : ' + ticker_data[item]['symbol'])
    print('Slug        : ' + ticker_data[item]['slug'])
    print('Rank        : ' + str(ticker_data[item]['rank']))
    print('Price       : ' + str(ticker_data[item]['price']))
    print('1h  Percent : ' + str(ticker_data[item]['percent']['1h']))
    print('24h Percent : ' + str(ticker_data[item]['percent']['24h']))
    print('7d  Percent : ' + str(ticker_data[item]['percent']['7d']))
    print('Volume      : ' + str(ticker_data[item]['volume']))
    print('Market Cap  : ' + str(ticker_data[item]['market_cap']))
    input('') # Press enter to continue...
```

___

###### Mirrors
[acid.vegas](https://git.acid.vegas/coinmarketcap) • [GitHub](https://github.com/acidvegas/coinmarketcap) • [GitLab](https://gitlab.com/acidvegas/coinmarketcap) • [SuperNETs](https://git.supernets.org/acidvegas/coinmarketcap)
