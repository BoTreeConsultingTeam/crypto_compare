

def generate_avg(self, **kwargs):

    """
    https://min-api.cryptocompare.com/
    
    Keyword arguments:

    inside kwargs

    fsym         - From Symbol
    tsym         - To Symbols
    markets      - Name of exchange
    extraParams  - Name of your application
    sign         - If set to true, the server will sign the requests.
    tryConversion - If set to false, it will try to get values without using any conversion at all
    
    """

    fsym, tsym, querystring = self._get_querystring(kwargs)
    markets = kwargs['markets'] if 'markets' in kwargs else ''

    self._is_params_valid(fsym=fsym, tsym=tsym, markets=markets)

    return self._fetch_data(self.GENERATE_AVG_URL+querystring) 


def day_avg(self, **kwargs):

    """
    https://www.cryptocompare.com/api/#-api-data-price- --> dayAvg
    
    Keyword arguments:

    inside kwargs

    fsym         - From Symbol
    tsym         - To Symbols
    e            - Name of exchange
    extraParams  - Name of your application
    sign         - If set to true, the server will sign the requests.
    tryConversion - If set to false, it will try to get values without using any conversion at all
    avgType      -    
    UTCHourDiff  - By deafult it does UTC, if you want a different time zone just pass the hour difference. 
                   For PST you would pass -8 for example.
    toTs         - hour unit

    """

    fsym, tsym, querystring = self._get_querystring(kwargs)

    self._is_params_valid(fsym=fsym, tsym=tsym)

    return self._fetch_data(self.DAY_AVG_URL+querystring)