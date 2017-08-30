

def subs_watchlist(self, **kwargs):

    """
    https://min-api.cryptocompare.com/
    
    Keyword arguments:

    inside kwargs

    fsyms        - From Symbol
    tsym         - To Symbols
    extraParams  - Name of your application
    sign         - If set to true, the server will sign the requests.

    """

    fsyms, tsym, querystring = self._get_querystring(kwargs)

    self._is_params_valid(fsyms=fsyms, tsym=tsym)

    return self._fetch_data(self.SUBS_WATCH_LIST_URL+querystring)


def subs(self, **kwargs):

    """
    https://min-api.cryptocompare.com/
    
    Keyword arguments:

    inside kwargs

    fsym         - From Symbol
    tsyms        - To Symbols
    extraParams  - Name of your application
    sign         - If set to true, the server will sign the requests.

    """

    fsym, tsyms, querystring = self._get_querystring(kwargs)

    self._is_params_valid(fsym=fsym)

    return self._fetch_data(self.SUBS_URL+querystring)