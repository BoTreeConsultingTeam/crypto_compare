

def mining_contracts(self):

    """ 
    https://www.cryptocompare.com/api/#-api-data-miningcontracts-
    """
    
    return self._fetch_data(self.MINING_CONTRACTS_URL)


def mining_equipment(self):

    """ 
    https://www.cryptocompare.com/api/#-api-data-miningequipment-
    """
    
    return self._fetch_data(self.MINING_EQUIPMENT_URL)
