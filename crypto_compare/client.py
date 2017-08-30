
class Client:
    
    COIN_LIST_URL = 'https://www.cryptocompare.com/api/data/coinlist/'
    COIN_SNAPSHOT_FULL_BY_ID_URL = 'https://www.cryptocompare.com/api/data/coinsnapshotfullbyid/?id='
    COIN_SNAPSHOT_URL  = 'https://www.cryptocompare.com/api/data/coinsnapshot/'

    PRICE_URL = 'https://min-api.cryptocompare.com/data/price'
    PRICE_MULTI_URL = 'https://min-api.cryptocompare.com/data/pricemulti'
    PRICE_MULTI_FULL_URL = 'https://min-api.cryptocompare.com/data/pricemultifull'
    PRICE_HISTORICAL_URL = 'https://min-api.cryptocompare.com/data/pricehistorical'

    GENERATE_AVG_URL = 'https://min-api.cryptocompare.com/data/generateAvg'
    DAY_AVG_URL = 'https://min-api.cryptocompare.com/data/dayAvg'

    SUBS_WATCH_LIST_URL = 'https://min-api.cryptocompare.com/data/subsWatchlist'
    SUBS_URL = 'https://min-api.cryptocompare.com/data/subs'

    ALL_EXCHANGES_URL = 'https://min-api.cryptocompare.com/data/all/exchanges'
    TOP_EXCHANGES_URL = 'https://min-api.cryptocompare.com/data/top/exchanges'
    TOP_VOLUMES_URL = 'https://min-api.cryptocompare.com/data/top/volumes'
    TOP_PAIRS_URL = 'https://min-api.cryptocompare.com/data/top/pairs'

    HISTO_DAY_URL = 'https://min-api.cryptocompare.com/data/histoday'
    HISTO_HOUR_URL = 'https://min-api.cryptocompare.com/data/histohour'
    HISTO_MINUTE_URL = 'https://min-api.cryptocompare.com/data/histominute'

    SOCIAL_STATS_URL = 'https://www.cryptocompare.com/api/data/socialstats?id='

    MINING_CONTRACTS_URL = 'https://www.cryptocompare.com/api/data/miningcontracts/'
    MINING_EQUIPMENT_URL = 'https://www.cryptocompare.com/api/data/miningequipment/'


    from apis.coin import coin_list, coin_snapshot_full_by_id, coin_snapshot
    from apis.price import price, price_multi, price_multifull, price_historical
    from apis.average import generate_avg, day_avg
    from apis.subs import subs_watchlist, subs
    from apis.top import top_exchanges, top_volumes, top_pairs
    from apis.histo import histo_day, histo_hour, histo_minute
    from apis.mining import mining_contracts, mining_equipment
    from apis.uncategorized import all_exchanges, social_stats

    from apis.helper import _is_params_valid, _fetch_data, _get_querystring
