#!/usr/bin/env python
# CoinMarketCap API Class - Developed by acidvegas in Python (https://acid.vegas/coinmarketcap)

import http.client
import json
import time
import zlib

CACHE_EXPIRY_TIME = 300

class CoinMarketCap(object):
	def __init__(self, api_key):
		self.api_key = api_key
		self.cache   = {'global':dict(), 'ticker':dict()}
		self.last    = {'global':0     , 'ticker':0     }

	def _api(self, _endpoint):
		'''Make a request to the CoinMarketCap API.'''
		with http.client.HTTPSConnection('pro-api.coinmarketcap.com', timeout=15) as conn:
			conn.request('GET', f'/v1/{_endpoint}', headers={'Accept':'application/json', 'Accept-Encoding':'deflate, gzip', 'X-CMC_PRO_API_KEY':self.api_key})
			response = conn.getresponse()
			if response.getheader('Content-Encoding') == 'gzip':
				content = zlib.decompress(response.read(), 16+zlib.MAX_WBITS).decode('utf-8')
			else:
				content = response.read().decode('utf-8')
		return json.loads(content.replace(': null', ': "0"'))['data']

	def _global(self):
		'''Get global market data.'''
		if time.time() - self.last['global'] < CACHE_EXPIRY_TIME:
			return self.cache['global']
		else:
			data = self._api('global-metrics/quotes/latest')
			self.cache['global'] = {
				'cryptocurrencies' : data['active_cryptocurrencies'],
				'exchanges'        : data['active_exchanges'],
				'btc_dominance'    : int(data['btc_dominance']),
				'eth_dominance'    : int(data['eth_dominance']),
				'market_cap'       : int(data['quote']['USD']['total_market_cap']),
				'volume'           : int(data['quote']['USD']['total_volume_24h'])
			}
			self.last['global'] = time.time()
			return self.cache['global']

	def _ticker(self):
		'''Get ticker data.'''
		if time.time() - self.last['ticker'] < CACHE_EXPIRY_TIME:
			return self.cache['ticker']
		else:
			data = self._api('cryptocurrency/listings/latest?limit=5000')
			self.cache['ticker'] = dict()
			for item in data:
				self.cache['ticker'][item['id']] = {
					'name'       : item['name'],
					'symbol'     : item['symbol'],
					'slug'       : item['slug'],
					'rank'       : item['cmc_rank'],
					'price'      : float(item['quote']['USD']['price']),
					'percent'    : {'1h':float(item['quote']['USD']['percent_change_1h']), '24h':float(item['quote']['USD']['percent_change_24h']), '7d':float(item['quote']['USD']['percent_change_7d'])},
					'volume'     : int(float(item['quote']['USD']['volume_24h'])),
					'market_cap' : int(float(item['quote']['USD']['market_cap']))
				}
			self.last['ticker'] = time.time()
			return self.cache['ticker']