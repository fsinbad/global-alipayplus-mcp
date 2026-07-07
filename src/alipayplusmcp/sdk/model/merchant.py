#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
from alipayplusmcp.sdk.model.address import Address


class Merchant(object):
    def __init__(self):
        self.__merchant_id = None
        self.__reference_merchant_id = None
        self.__merchant_mcc = None
        self.__merchant_name = None
        self.__merchant_display_name = None
        self.__merchant_address = None  # type: Address
        self.__merchant_register_date = None
        self.__merchant_status = None
        self.__store = None

    @property
    def reference_merchant_id(self):
        return self.__reference_merchant_id

    @reference_merchant_id.setter
    def reference_merchant_id(self, value):
        self.__reference_merchant_id = value

    @property
    def merchant_id(self):
        return self.__merchant_id

    @merchant_id.setter
    def merchant_id(self, value):
        self.__merchant_id = value

    @property
    def merchant_mcc(self):
        return self.__merchant_mcc

    @merchant_mcc.setter
    def merchant_mcc(self, value):
        self.__merchant_mcc = value

    @property
    def merchant_name(self):
        return self.__merchant_name

    @merchant_name.setter
    def merchant_name(self, value):
        self.__merchant_name = value

    @property
    def merchant_display_name(self):
        return self.__merchant_display_name

    @merchant_display_name.setter
    def merchant_display_name(self, value):
        self.__merchant_display_name = value

    @property
    def merchant_address(self):
        return self.__merchant_address

    @merchant_address.setter
    def merchant_address(self, value):
        self.__merchant_address = value

    @property
    def merchant_register_date(self):
        return self.__merchant_register_date

    @merchant_register_date.setter
    def merchant_register_date(self, value):
        self.__merchant_register_date = value

    @property
    def merchant_status(self):
        return self.__merchant_status

    @merchant_status.setter
    def merchant_status(self, value):
        self.__merchant_status = value

    @property
    def store(self):
        return self.__store

    @store.setter
    def store(self, value):
        self.__store = value

    def to_aps_dict(self):
        params = dict()
        if hasattr(self, "merchant_id") and self.merchant_id:
            params['merchantId'] = self.merchant_id

        if hasattr(self, "reference_merchant_id") and self.reference_merchant_id:
            params['referenceMerchantId'] = self.reference_merchant_id

        if hasattr(self, "merchant_mcc") and self.merchant_mcc:
            params['merchantMCC'] = self.merchant_mcc

        if hasattr(self, "merchant_name") and self.merchant_name:
            params['merchantName'] = self.merchant_name

        if hasattr(self, "merchant_display_name") and self.merchant_display_name:
            params['merchantDisplayName'] = self.merchant_display_name

        if hasattr(self, "merchant_address") and self.merchant_address:
            params['merchantAddress'] = self.merchant_address

        if hasattr(self, "merchant_register_date") and self.merchant_register_date:
            params['merchantRegisterDate'] = self.merchant_register_date

        if hasattr(self, "merchant_status") and self.merchant_status:
            params['merchantStatus'] = self.merchant_status

        if hasattr(self, "store") and self.store:
            params['store'] = self.store

        return params

    def parse_rsp_body(self, merchant_body):
        if type(merchant_body) == str:
            merchant_body = json.loads(merchant_body)

        if 'merchantId' in merchant_body:
            self.__merchant_id = merchant_body['merchantId']

        if 'referenceMerchantId' in merchant_body:
            self.__reference_merchant_id = merchant_body['referenceMerchantId']

        if 'merchantMCC' in merchant_body:
            self.__merchant_mcc = merchant_body['merchantMCC']

        if 'merchantName' in merchant_body:
            self.__merchant_name = merchant_body['merchantName']

        if 'merchantDisplayName' in merchant_body:
            self.__merchant_display_name = merchant_body['merchantDisplayName']

        if 'merchantAddress' in merchant_body:
            address = Address()
            address.parse_rsp_body(merchant_body['merchantAddress'])
            self.__merchant_address = address

        if 'merchantRegisterDate' in merchant_body:
            self.__merchant_register_date = merchant_body['merchantRegisterDate']

        if 'merchantStatus' in merchant_body:
            self.__merchant_status = merchant_body['merchantStatus']
