import json
import urllib2

ALLOWED_KEYS = [
    'fsym',
    'fsyms',
    'tsym',
    'tsyms',
    'ts',
    'e',
    'markets',
    'extraParams',
    'sign',
    'tryConversion',
    'calculationType'
]

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
            
            if key == "fsym" or key == "fsyms":
                fsym = value
            elif key == 'tsym' or key == 'tsyms':
                tsym = value
            
            if key in ALLOWED_KEYS:
                querystring = "{}&{}".format(querystring, "{}={}".format(key, value))
            
    return fsym, tsym, querystring
