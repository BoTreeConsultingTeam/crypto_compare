def all_exchanges(self, **kwargs):

    """
    https://min-api.cryptocompare.com/
    
    Keyword arguments:

    inside kwargs

    extraParams  - Name of your application
    sign         - If set to true, the server will sign the requests.

    """

    fsym, tsym, querystring = self._get_querystring(kwargs)

    return self._fetch_data(self.ALL_EXCHANGES_URL+querystring)


def social_stats(self, coin_id):

    """ 
    https://www.cryptocompare.com/api/#-api-data-socialstats-

    Keyword arguments:

    id            - The id of the coin/exchange you want social data for
    """

    if(coin_id == None or coin_id == ''):
        raise ValueError('coin_id cannot be empty!')
    
    return self._fetch_data(self.SOCIAL_STATS_URL+str(coin_id))