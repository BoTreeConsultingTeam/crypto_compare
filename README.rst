# crypto_compare

CryptoCompare.com API client for Python

## Folder/code structure

The code is written such that all the methods are available as instance methods in `Client` class, but grouped them in diff. modules under `apis` module to keep the code readable. All these module methods are imported inside the class `Client`.

```
|_ crypto_compare
|__ client.py -- This is the main client class which has all the public methods
|__ apis
|___ average.py - methods for average APIs
|___ coin.py - methods for coin APIs
|___ helper.py - helper methods
|___ histo.py - methods for histo APIs
|___ mining.py - methods for mining APIs
|___ price.py - methods for pricing APIs
|___ subs.py - methods for subs APIs
|___ top.py - methods for top data APIs
|___ uncategorized.py - other API methods


```

## Usage

1. Install it using pip

``` shell
pip install crypto_compare

```
2. Use it as following
``` python

import crypto_compare

crypto_compare_client = crypto_compare.Client() #Create an instance and call any public API method!
crypto_compare_client.coin_list()
crypto_compare_client.coin_snapshot('BTC', 'USD')

```

## API docs

### Coin methods
1. `coin_list()`
2. `coin_snapshot_full_by_id(coin_id)`
3. `coin_snapshot(fsym, tsym)`

### Price methods
4. `price(**kwargs) - fsym and tsyms are mandatory as named arguments`
5. `price_multi(**kwargs) - fsyms and tsyms are mandatory as named arguments`
6. `price_multifull(**kwargs) - fsyms and tsyms are mandatory as named arguments`
7. `price_historical(**kwargs) - fsym and tsyms are mandatory as named arguments`

### Average methods
8. `generate_avg(**kwargs) - fsym, tsym and markets are mandatory as named arguments`
9. `day_avg(**kwargs) - fsym and tsym are mandatory as named arguments`

### Subs methods
10. `subs_watchlist(**kwargs) - fsyms and tsym are mandatory as named arguments`
11. `subs(**kwargs) - fsym is mandatory as named argument`

### Top Data methods
12. `top_exchanges(**kwargs) - fsym and tsym are mandatory as named arguments`
13. `top_volumes(**kwargs) - tsym is mandatory as named argument`
14. `top_pairs(**kwargs) - fsym and tsym are mandatory as named arguments`

### Histo methods
15. `histo_day(**kwargs) - fsym and tsym are mandatory as named arguments`
16. `histo_hour(**kwargs) - tsym is mandatory as named argument`
17. `histo_minute(**kwargs) - fsym and tsym are mandatory as named arguments`

### Mining methods
18. `mining_contracts()`
19. `mining_equipment()`

### Other methods
20. `all_exchanges(**kwargs)`
21. `social_stats(coin_id)`

## ToDo

1. Add tests