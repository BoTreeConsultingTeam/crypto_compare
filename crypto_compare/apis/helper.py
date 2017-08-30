import json
import urllib2


def _is_params_valid(self, **kwargs):

    for key,value in kwargs.items():
        if(value == None or value == ''):
            raise ValueError(key+' cannot be empty!')

    return True


def _fetch_data(self, url):

    print('Calling URL - ' + url)
    
    json_response = json.load(urllib2.urlopen(url))
    
    if 'Response' in json_response and json_response["Response"] == 'Error':
        raise ValueError("API Error - {} !".format(json_response['Message']))
    else:
        return json_response

def _get_querystring(self, kwargs):

    querystring = '?'
    fsym = ''
    tsym = ''

    if kwargs is not None:
        
        for key,value in kwargs.items():
            
            if key == 'fsym':
                fsym = value
                querystring = "{}&{}".format(querystring, "fsym={}".format(fsym))
            elif key == 'fsyms':
                fsym = value
                querystring = "{}&{}".format(querystring, "fsyms={}".format(fsym))
            elif key == 'tsyms':
                tsym = value
                querystring = "{}&{}".format(querystring, "tsyms={}".format(tsym))
            elif key == 'tsym':
                tsym = value
                querystring = "{}&{}".format(querystring, "tsym={}".format(tsym))
            elif key == 'ts':
                querystring = "{}&{}".format(querystring, "ts={}".format(value))
            elif key == 'e':
                querystring = "{}&{}".format(querystring, "e={}".format(value))
            elif key == 'markets':
                querystring = "{}&{}".format(querystring, "markets={}".format(value))
            elif key == 'extraParams':
                querystring = "{}&{}".format(querystring, "extraParams={}".format(value))
            elif key == 'sign':
                querystring = "{}&{}".format(querystring, "sign={}".format(value))
            elif key == 'tryConversion':
                querystring = "{}&{}".format(querystring, "tryConversion={}".format(value))
            elif key == 'calculationType':
                querystring = "{}&{}".format(querystring, "calculationType={}".format(value))

    return fsym, tsym, querystring