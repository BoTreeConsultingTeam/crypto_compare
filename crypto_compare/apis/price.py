

def price(self, **kwargs):

    """
    https://www.cryptocompare.com/api/#-api-data-price-

    Keyword arguments:

    inside kwargs
    
    fsym          - From Symbol - *
    tsyms         - To Symbols, include multiple - *
    e             - Name of exchanges, include multiple
    extraParams   - Name of your application
    sign          - If set to true, the server will sign the requests.
    tryConversion - If set to false, it will try to get values without using any conversion at all

    """
    fsym, tsyms, querystring = self._get_querystring(kwargs)

    self._is_params_valid(fsym=fsym, tsyms=tsyms)

    return self._fetch_data(self.PRICE_URL+querystring) 


def price_multi(self, **kwargs):

    """
    https://www.cryptocompare.com/api/#-api-data-price-

    Keyword arguments:

    inside kwargs
    
    fsyms         - From Symbol - *
    tsyms         - To Symbols, include multiple - *
    e             - Name of exchanges, include multiple
    extraParams   - Name of your application
    sign          - If set to true, the server will sign the requests.
    tryConversion - If set to false, it will try to get values without using any conversion at all

    """
    fsyms, tsyms, querystring = self._get_querystring(kwargs)

    self._is_params_valid(fsyms=fsyms, tsyms=tsyms)

    return self._fetch_data(self.PRICE_MULTI_URL+querystring)


def price_multifull(self, **kwargs):

    """
    https://www.cryptocompare.com/api/#-api-data-price-

    Keyword arguments:

    inside kwargs
    
    fsyms         - From Symbol - *
    tsyms         - To Symbols, include multiple - *
    e             - Name of exchanges, include multiple
    extraParams   - Name of your application
    sign          - If set to true, the server will sign the requests.
    tryConversion - If set to false, it will try to get values without using any conversion at all

    """
    fsyms, tsyms, querystring = self._get_querystring(kwargs)

    self._is_params_valid(fsyms=fsyms, tsyms=tsyms)

    return self._fetch_data(self.PRICE_MULTI_FULL_URL+querystring)  


def price_historical(self, **kwargs):

    """
    https://www.cryptocompare.com/api/#-api-data-pricehistorical

    Keyword arguments:

    inside kwargs
    
    fsym          - From Symbol - *
    tsyms         - To Symbols, include multiple - *
    ts            -     
    e             - Name of exchanges, include multiple
    extraParams   - Name of your application
    sign          - If set to true, the server will sign the requests.
    tryConversion - If set to false, it will try to get values without using any conversion at all

    """
    fsym, tsyms, querystring = self._get_querystring(kwargs)

    self._is_params_valid(fsym=fsym, tsyms=tsyms)

    return self._fetch_data(self.PRICE_HISTORICAL_URL+querystring)