import unittest
import adshopcart_locators as locators
import adshopcart_methods as methods


class AdshopcartAppPositiveTestCases(unittest.TestCase):  # container for the test

    @staticmethod
    def test_advantage_shopping_cart():
        methods.setUp()
        methods.sign_up()
        methods.check_full_name()
        methods.check_orders()
        methods.log_out()
        methods.log_in()
        methods.delete_test_account()
        methods.check_homepage()
        methods.tearDown()
