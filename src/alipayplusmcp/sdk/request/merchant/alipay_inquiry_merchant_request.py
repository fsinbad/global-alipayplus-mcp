import json

from alipayplusmcp.sdk.model.AlipayPlusPathConstant import AlipayPlusPathConstants
from alipayplusmcp.sdk.request.alipay_request import AlipayRequest

# https://docs.alipayplus.com/alipayplus/alipayplus/api_acq/inquiry_registration_status?role=ACQP
class AlipayInquiryMerchantRequest(AlipayRequest):

    def __init__(self):
        super(AlipayInquiryMerchantRequest, self).__init__(AlipayPlusPathConstants.INQUIRY_MERCHANT_PATH)
        self.__reference_merchant_id = None
        self.__reference_store_id = None
        self.__registration_request_id = None

    @property
    def reference_merchant_id(self):
        return self.__reference_merchant_id

    @reference_merchant_id.setter
    def reference_merchant_id(self, value):
        self.__reference_merchant_id = value

    @property
    def reference_store_id(self):
        return self.__reference_store_id

    @reference_store_id.setter
    def reference_store_id(self, value):
        self.__reference_store_id = value

    @property
    def registration_request_id(self):
        return self.__registration_request_id

    @registration_request_id.setter
    def registration_request_id(self, value):
        self.__registration_request_id = value

    def to_aps_json(self):
        params = dict()
        if hasattr(self, "reference_merchant_id") and self.reference_merchant_id:
            params['referenceMerchantId'] = self.reference_merchant_id

        if hasattr(self, "reference_store_id") and self.reference_store_id:
            params['referenceStoreId'] = self.reference_store_id

        if hasattr(self, "registration_request_id") and self.registration_request_id:
            params['registrationRequestId'] = self.registration_request_id

        json_str = json.dumps(obj=params, indent=3)
        return json_str
