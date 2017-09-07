

def coin_list(self):

    """ 
    https://www.cryptocompare.com/api/#-api-data-coinlist-
    """
    
    return self._fetch_data(self.COIN_LIST_URL)


def coin_snapshot_full_by_id(self, coin_id):
    
    """ 
    https://www.cryptocompare.com/api/#-api-data-coinsnapshotfullbyid-

    Keyword arguments:
    coin_id - The id of the coin you want data for
    
    """

    if(coin_id == None or coin_id == ''):
        raise ValueError('coin_id cannot be empty!')

    return self._fetch_data(self.COIN_SNAPSHOT_FULL_BY_ID_URL+str(coin_id))


def coin_snapshot(self, fsym, tsym):

    """
    https://www.cryptocompare.com/api/#-api-data-coinsnapshot-

    Keyword arguments:
    fsym - The symbol of the currency you want to get that for
    tsym - The symbol of the currency that data will be in.

    """

    self._is_params_valid(fsym=fsym, tsym=tsym)
    
    return self._fetch_data(self.COIN_SNAPSHOT_URL+'?fsym='+fsym+'&tsym='+tsym)