

def histo_day(self, **kwargs):

    """
    https://min-api.cryptocompare.com/
    
    Keyword arguments:

    inside kwargs

    fsym            - From Symbol
    tsym            - To Symbol
    extraParams     - Name of your application
    sign            - If set to true, the server will sign the requests.
    limit           - default 30, max 2000, min 1
    tryConversion   - If set to false, it will try to get values without using any conversion at all
    e               - market list
    aggregate       - default 1, max 30, min 1
    allData         - default false
    toTs            - timestamp

    """

    fsym, tsym, querystring = self._get_querystring(kwargs)

    self._is_params_valid(fsym=fsym, tsym=tsym)

    return self._fetch_data(self.HISTO_DAY_URL+querystring)


def histo_hour(self, **kwargs):

    """
    https://min-api.cryptocompare.com/
    
    Keyword arguments:

    inside kwargs

    fsym            - From Symbol
    tsym            - To Symbol
    extraParams     - Name of your application
    sign            - If set to true, the server will sign the requests.
    limit           - default 168, max 2000, min 1
    tryConversion   - If set to false, it will try to get values without using any conversion at all
    e               - market list
    aggregate       - default 1, max 30, min 1
    allData         - default false
    toTs            - timestamp

    """

    fsym, tsym, querystring = self._get_querystring(kwargs)

    self._is_params_valid(fsym=fsym, tsym=tsym)

    return self._fetch_data(self.HISTO_HOUR_URL+querystring)


def histo_minute(self, **kwargs):

    """
    https://min-api.cryptocompare.com/
    
    Keyword arguments:

    inside kwargs

    fsym            - From Symbol
    tsym            - To Symbol
    extraParams     - Name of your application
    sign            - If set to true, the server will sign the requests.
    limit           - default 1440, max 2000, min 1
    tryConversion   - If set to false, it will try to get values without using any conversion at all
    e               - market list
    aggregate       - default 1, max 30, min 1
    allData         - default false
    toTs            - timestamp

    """

    fsym, tsym, querystring = self._get_querystring(kwargs)

    self._is_params_valid(fsym=fsym, tsym=tsym)

    return self._fetch_data(self.HISTO_MINUTE_URL+querystring)