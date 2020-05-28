
class Client:
    def __init__(self, apikey):
        self.apikey = apikey

    BASE_URL = 'https://min-api.cryptocompare.com'
    
    COIN_LIST_URL = BASE_URL + '/data/all/coinlist'
    COIN_SNAPSHOT_FULL_BY_ID_URL = 'https://www.cryptocompare.com/api/data/coinsnapshotfullbyid/?id='
    COIN_SNAPSHOT_URL  = BASE_URL + '/data/top/exchanges/full'

    PRICE_URL = BASE_URL + '/data/price'
    PRICE_MULTI_URL = BASE_URL + '/data/pricemulti'
    PRICE_MULTI_FULL_URL = BASE_URL + '/data/pricemultifull'
    PRICE_HISTORICAL_URL = BASE_URL + '/data/pricehistorical'

    GENERATE_AVG_URL = BASE_URL + '/data/generateAvg'
    DAY_AVG_URL = BASE_URL + '/data/dayAvg'

    SUBS_WATCH_LIST_URL = BASE_URL + '/data/subsWatchlist'
    SUBS_URL = BASE_URL + '/data/subs'

    ALL_EXCHANGES_URL = BASE_URL + '/data/all/exchanges'
    TOP_EXCHANGES_URL = BASE_URL + '/data/top/exchanges'
    TOP_VOLUMES_URL = BASE_URL + '/data/top/volumes'
    TOP_PAIRS_URL = BASE_URL + '/data/top/pairs'

    HISTO_DAY_URL = BASE_URL + '/data/histoday'
    HISTO_HOUR_URL = BASE_URL + '/data/histohour'
    HISTO_MINUTE_URL = BASE_URL + '/data/histominute'

    SOCIAL_STATS_URL = 'https://www.cryptocompare.com/api/data/socialstats?id='

    MINING_CONTRACTS_URL = BASE_URL + '/data/mining/contracts/general'
    MINING_EQUIPMENT_URL = BASE_URL + '/data/mining/equipment/general'

    from .apis.coin import coin_list, coin_snapshot_full_by_id, coin_snapshot
    from .apis.price import price, price_multi, price_multifull, price_historical
    from .apis.average import generate_avg, day_avg
    from .apis.subs import subs_watchlist, subs
    from .apis.top import top_exchanges, top_volumes, top_pairs
    from .apis.histo import histo_day, histo_hour, histo_minute
    from .apis.mining import mining_contracts, mining_equipment
    from .apis.uncategorized import all_exchanges, social_stats

    from .apis.helper import _is_params_valid, _fetch_data, _get_querystring
