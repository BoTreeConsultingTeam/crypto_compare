import mock 
import pytest
from pytest_mock import mocker 
from crypto_compare.client import Client
import urllib2
from urlparse import urlparse
import os.path
import unittest
from mock import patch


def describe_coin():

    def describe_list():

        @mock.patch('urllib2.urlopen', _fake_url_open_with_success)
        def with_success():
            _assert_success(Client().coin_list())


        @mock.patch('urllib2.urlopen', _fake_url_open_with_error)
        def with_error():

            with pytest.raises(ValueError) as excinfo:
                Client().coin_list()


    def describe_snapshot_full_by_id():
    

        @mock.patch('urllib2.urlopen', _fake_url_open_with_success)
        def with_success():

            _assert_success(Client().coin_snapshot_full_by_id(1182))

        @mock.patch('urllib2.urlopen', _fake_url_open_with_error)
        def without_coin_id():
            with pytest.raises(ValueError) as excinfo:
                Client().coin_snapshot_full_by_id('')


        @mock.patch('urllib2.urlopen', _fake_url_open_with_error)
        def with_invalid_coin_id():

            with pytest.raises(ValueError) as excinfo:
                Client().coin_snapshot_full_by_id(123456)


    def describe_snapshot():
    

        @mock.patch('urllib2.urlopen', _fake_url_open_with_success)
        def with_success():

            _assert_success(Client().coin_snapshot('BTC','ETH'))


        @mock.patch('urllib2.urlopen', _fake_url_open_with_error)
        def with_empty_args():

            with pytest.raises(ValueError) as excinfo:
                Client().coin_snapshot('','')

            with pytest.raises(ValueError) as excinfo:
                Client().coin_snapshot('BTC','')

            with pytest.raises(ValueError) as excinfo:
                Client().coin_snapshot('','ETH')


        @mock.patch('urllib2.urlopen', _fake_url_open_with_error)
        def with_invalid_args():

            with pytest.raises(ValueError) as excinfo:
                Client().coin_snapshot('123', '456')


def describe_price():


    @mock.patch('urllib2.urlopen', _fake_url_open_with_success)
    def with_success():

        response = Client().price(fsym='BTC', tsyms='ETH')
        assert response['USD'] != None


    @mock.patch('urllib2.urlopen', _fake_url_open_with_error)
    def with_empty_args():

        with pytest.raises(ValueError) as excinfo:
            Client().price()

        with pytest.raises(ValueError) as excinfo:
            Client().price(fsym='')

        with pytest.raises(ValueError) as excinfo:
            Client().price(tsyms='')


    def describe_multi():

    
        @mock.patch('urllib2.urlopen', _fake_url_open_with_success)
        def with_success():

            response = Client().price_multi(fsyms='BTC,ETH', tsyms='USD,EUR')
            assert response['BTC'] != None
            assert response['ETH'] != None


        @mock.patch('urllib2.urlopen', _fake_url_open_with_error)
        def with_empty_args():

            with pytest.raises(ValueError) as excinfo:
                Client().price_multi()

            with pytest.raises(ValueError) as excinfo:
                Client().price_multi(fsyms='')

            with pytest.raises(ValueError) as excinfo:
                Client().price_multi(tsyms='')

        
        @mock.patch('urllib2.urlopen', _fake_url_open_with_error)
        def with_invalid_args():

            with pytest.raises(ValueError) as excinfo:
                Client().price_multi(fsyms='BTC,ETH', tsyms='PPH')


    def describe_multifull():


        @mock.patch('urllib2.urlopen', _fake_url_open_with_success)
        def with_success():

          response = Client().price_multifull(fsyms='BTC,ETH', tsyms='USD,EUR')
          assert response['RAW'] != None


        @mock.patch('urllib2.urlopen', _fake_url_open_with_error)
        def with_empty_args():

            with pytest.raises(ValueError) as excinfo:
                Client().price_multifull()

            with pytest.raises(ValueError) as excinfo:
                Client().price_multifull(fsyms='')

            with pytest.raises(ValueError) as excinfo:
                Client().price_multifull(tsyms='')


        @mock.patch('urllib2.urlopen', _fake_url_open_with_error)
        def with_invalid_args():

            with pytest.raises(ValueError) as excinfo:
                Client().price_multifull(fsyms='BTC,ETH', tsyms='PPH')


    def describe_historical():


        @mock.patch('urllib2.urlopen', _fake_url_open_with_success)
        def with_success():

            response = Client().price_historical(fsym='BTC', tsyms='USD,EUR')
            assert response['BTC'] != None


        @mock.patch('urllib2.urlopen', _fake_url_open_with_success)
        def with_empty_args():

            with pytest.raises(ValueError) as excinfo:
                Client().price_historical()

            with pytest.raises(ValueError) as excinfo:
                Client().price_historical(fsym='')

            with pytest.raises(ValueError) as excinfo:
                Client().price_historical(tsyms='')


        @mock.patch('urllib2.urlopen', _fake_url_open_with_error)
        def with_invalid_args():

            with pytest.raises(ValueError) as excinfo:
                Client().price_historical(fsym='BTC', tsyms='USD,EUR')


def describe_generate_avg():

    @mock.patch('urllib2.urlopen', _fake_url_open_with_success)
    def with_success():

        response = Client().generate_avg(fsym='BTC', tsym='USD', markets='Coinbase')
        assert response['RAW'] != None


    @mock.patch('urllib2.urlopen', _fake_url_open_with_error)
    def with_empty_args():

        with pytest.raises(ValueError) as excinfo:
            Client().generate_avg()

        with pytest.raises(ValueError) as excinfo:
            Client().generate_avg(fsym='BTC')

        with pytest.raises(ValueError) as excinfo:
            Client().generate_avg(markets='Coinbase', tsym='ETH')


    @mock.patch('urllib2.urlopen', _fake_url_open_with_error)
    def with_invalid_args():

        with pytest.raises(ValueError) as excinfo:
            Client().generate_avg(markets='TestMarket', tsym='ETH', fsym='BTC')


def describe_day_avg():

    @mock.patch('urllib2.urlopen', _fake_url_open_with_success)
    def with_success():

        response = Client().day_avg(fsym='BTC', tsym='USD')
        assert response['USD'] != None


    @mock.patch('urllib2.urlopen', _fake_url_open_with_error)
    def with_empty_args():

        with pytest.raises(ValueError) as excinfo:
            Client().day_avg()

        with pytest.raises(ValueError) as excinfo:
            Client().day_avg(fsym='BTC')

        with pytest.raises(ValueError) as excinfo:
            Client().day_avg(tsym='ETH')


    @mock.patch('urllib2.urlopen', _fake_url_open_with_error)
    def with_invalid_args():

        with pytest.raises(ValueError) as excinfo:
            Client().day_avg(tsym='DFG', fsym='BTC')


def describe_subs():


    @mock.patch('urllib2.urlopen', _fake_url_open_with_success)
    def with_success():

        response = Client().subs(fsym='BTC')
        assert response['USD'] != None


    @mock.patch('urllib2.urlopen', _fake_url_open_with_error)
    def with_empty_args():

        with pytest.raises(ValueError) as excinfo:
            Client().subs()


    @mock.patch('urllib2.urlopen', _fake_url_open_with_error)
    def with_invalid_args():

        with pytest.raises(ValueError) as excinfo:
            Client().subs(fsym='DFG')


def describe_subs_watchlist():


    @mock.patch('urllib2.urlopen', _fake_url_open_with_success)
    def with_success():

        response = Client().subs_watchlist(fsyms='BTC', tsym='ETH')
        assert response['BTC'] != None


    @mock.patch('urllib2.urlopen', _fake_url_open_with_error)
    def with_empty_args():

        with pytest.raises(ValueError) as excinfo:
            Client().subs_watchlist()

        with pytest.raises(ValueError) as excinfo:
            Client().subs_watchlist(fsyms='BTC')

        with pytest.raises(ValueError) as excinfo:
            Client().subs_watchlist(tsym='ETH')


    @mock.patch('urllib2.urlopen', _fake_url_open_with_error)
    def with_invalid_args():

        with pytest.raises(ValueError) as excinfo:
            Client().subs_watchlist(fsyms='DFG', tsym='BTC')


def describe_top():

    def describe_exchanges():

        @mock.patch('urllib2.urlopen', _fake_url_open_with_success)
        def with_success():
            response = Client().top_exchanges(fsym='BTC', tsym='ETH')
            assert response['Response'] == "Success"
            assert response['Data'] != None


        @mock.patch('urllib2.urlopen', _fake_url_open_with_error)
        def with_empty_args():
            
            with pytest.raises(ValueError) as excinfo:
                Client().top_exchanges()

            with pytest.raises(ValueError) as excinfo:
                Client().top_exchanges(fsym='BTC')

            with pytest.raises(ValueError) as excinfo:
                Client().top_exchanges(tsym='ETH')


        @mock.patch('urllib2.urlopen', _fake_url_open_with_error)
        def with_invalid_args():

            with pytest.raises(ValueError) as excinfo:
                Client().top_exchanges(fsym='DFG', tsym='PPH')

    
    def describe_volumes():

        @mock.patch('urllib2.urlopen', _fake_url_open_with_success)
        def with_success():
            response = Client().top_volumes(tsym='BTC')
            assert response['Response'] == "Success"
            assert response['Data'] != None


        @mock.patch('urllib2.urlopen', _fake_url_open_with_error)
        def with_empty_args():
            
            with pytest.raises(ValueError) as excinfo:
                Client().top_volumes()


        @mock.patch('urllib2.urlopen', _fake_url_open_with_error)
        def with_invalid_args():

            with pytest.raises(ValueError) as excinfo:
                Client().top_volumes(tsym='PPH')


    def describe_pairs():

        @mock.patch('urllib2.urlopen', _fake_url_open_with_success)
        def with_success():
            response = Client().top_pairs(fsym='BTC')
            assert response['Response'] == "Success"
            assert response['Data'] != None


        @mock.patch('urllib2.urlopen', _fake_url_open_with_error)
        def with_empty_args():
            
            with pytest.raises(ValueError) as excinfo:
                Client().top_pairs()


        @mock.patch('urllib2.urlopen', _fake_url_open_with_error)
        def with_invalid_args():

            with pytest.raises(ValueError) as excinfo:
                Client().top_pairs(fsym='DFG')


def describe_histo():

    def describe_day():

        @mock.patch('urllib2.urlopen', _fake_url_open_with_success)
        def with_success():
            response = Client().histo_day(fsym='BTC', tsym='ETH')
            assert response['Response'] == "Success"
            assert response['Data'] != None


        @mock.patch('urllib2.urlopen', _fake_url_open_with_error)
        def with_empty_args():
            
            with pytest.raises(ValueError) as excinfo:
                Client().histo_day()

            with pytest.raises(ValueError) as excinfo:
                Client().histo_day(fsym='BTC')

            with pytest.raises(ValueError) as excinfo:
                Client().histo_day(tsym='ETH')


        @mock.patch('urllib2.urlopen', _fake_url_open_with_error)
        def with_invalid_args():

            with pytest.raises(ValueError) as excinfo:
                Client().histo_day(fsym='DFG', tsym='PPH')


    def describe_hour():

        @mock.patch('urllib2.urlopen', _fake_url_open_with_success)
        def with_success():
            response = Client().histo_hour(fsym='BTC', tsym='ETH')
            assert response['Response'] == "Success"
            assert response['Data'] != None


        @mock.patch('urllib2.urlopen', _fake_url_open_with_error)
        def with_empty_args():
            
            with pytest.raises(ValueError) as excinfo:
                Client().histo_hour()

            with pytest.raises(ValueError) as excinfo:
                Client().histo_hour(fsym='BTC')

            with pytest.raises(ValueError) as excinfo:
                Client().histo_hour(tsym='ETH')


        @mock.patch('urllib2.urlopen', _fake_url_open_with_error)
        def with_invalid_args():

            with pytest.raises(ValueError) as excinfo:
                Client().histo_hour(fsym='DFG', tsym='PPH')


    def describe_minute():

        @mock.patch('urllib2.urlopen', _fake_url_open_with_success)
        def with_success():
            response = Client().histo_minute(fsym='BTC', tsym='ETH')
            assert response['Response'] == "Success"
            assert response['Data'] != None


        @mock.patch('urllib2.urlopen', _fake_url_open_with_error)
        def with_empty_args():
            
            with pytest.raises(ValueError) as excinfo:
                Client().histo_minute()

            with pytest.raises(ValueError) as excinfo:
                Client().histo_minute(fsym='BTC')

            with pytest.raises(ValueError) as excinfo:
                Client().histo_minute(tsym='ETH')


        @mock.patch('urllib2.urlopen', _fake_url_open_with_error)
        def with_invalid_args():

            with pytest.raises(ValueError) as excinfo:
                Client().histo_minute(fsym='DFG', tsym='PPH')


def describe_mining():

    def describe_contracts():

        @mock.patch('urllib2.urlopen', _fake_url_open_with_success)
        def with_success():
            _assert_success(Client().mining_contracts())


    def describe_equipments():

        @mock.patch('urllib2.urlopen', _fake_url_open_with_success)
        def with_success():
            _assert_success(Client().mining_equipment())


def describe_all_exchanges():

    @mock.patch('urllib2.urlopen', _fake_url_open_with_success)
    def with_success():
        response = Client().all_exchanges()
        response["Cryptsy"] != None


def describe_social_stats():

    @mock.patch('urllib2.urlopen', _fake_url_open_with_success)
    def with_success():
        response = Client().social_stats(1182)
        assert response['Response'] == "Success"
        assert response['Data'] != None


    @mock.patch('urllib2.urlopen', _fake_url_open_with_error)
    def with_empty_args():
        
        with pytest.raises(ValueError) as excinfo:
            Client().social_stats('')


    @mock.patch('urllib2.urlopen', _fake_url_open_with_error)
    def with_invalid_args():

        response = Client().social_stats("abcdefg")
        assert response['Response'] == "Success"
        assert response['Data']['General']['Name'] == ''



def __url_resource_filepath(url, sub_folder):
    parsed_url = urlparse(url)
    url_parts = filter(None, parsed_url.path.split('/'))
    data_parts = url_parts[url_parts.index("data")+1: len(url_parts)]
    resource_name = '/' + "/".join(data_parts)
    resource_file = os.path.normpath('tests/resources/' + sub_folder + "/" + resource_name)
    return resource_file


def _fake_url_open_with_success(url):
    return open(__url_resource_filepath(url, 'success'), mode='rb')


def _fake_url_open_with_error(url):
    return open(__url_resource_filepath(url, 'error'), mode='rb')


def _assert_success(response):
    assert response['Response'] == "Success"
    assert response['Message'] != None