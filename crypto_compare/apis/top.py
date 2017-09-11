

def top_exchanges(self, **kwargs):

    """
    https://min-api.cryptocompare.com/
    
    Keyword arguments:

    inside kwargs

    fsym         - From Symbol
    tsym         - To Symbol
    extraParams  - Name of your application
    sign         - If set to true, the server will sign the requests.
    limit        - default 5, max 50, min 1

    """

    fsym, tsym, querystring = self._get_querystring(kwargs)

    self._is_params_valid(fsym=fsym, tsym=tsym)

    return self._fetch_data(self.TOP_EXCHANGES_URL+querystring)      


def top_volumes(self, **kwargs):

    """
    https://min-api.cryptocompare.com/
    
    Keyword arguments:

    inside kwargs

    tsym         - To Symbol
    extraParams  - Name of your application
    sign         - If set to true, the server will sign the requests.
    limit        - default 20, max 1000, min 1

    """

    fsym, tsym, querystring = self._get_querystring(kwargs)

    self._is_params_valid(tsym=tsym)

    return self._fetch_data(self.TOP_VOLUMES_URL+querystring)   


def top_pairs(self, **kwargs):

    """
    https://min-api.cryptocompare.com/
    
    Keyword arguments:

    inside kwargs

    fsym         - From Symbol
    extraParams  - Name of your application
    sign         - If set to true, the server will sign the requests.
    limit        - default 5, max 50, min 1

    """

    fsym, tsym, querystring = self._get_querystring(kwargs)

    self._is_params_valid(fsym=fsym)

    return self._fetch_data(self.TOP_PAIRS_URL+querystring)