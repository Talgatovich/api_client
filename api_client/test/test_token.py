# coding: utf-8

"""
    MDES Digital Enablement API

    These APIs are designed as RPC style stateless web services where each API endpoint represents an operation to be performed.  All request and response payloads are sent in the JSON (JavaScript Object Notation) data-interchange format. Each endpoint in the API specifies the HTTP Method used to access it. All strings in request and response objects are to be UTF-8 encoded.  Each API URI includes the major and minor version of API that it conforms to.  This will allow multiple concurrent versions of the API to be deployed simultaneously. <br><br> **Authentication** <br><br> Mastercard uses OAuth 1.0a with body hash extension for authenticating the API clients. This requires every request that you send to  Mastercard to be signed with an RSA private key. A private-public RSA key pair must be generated consisting of: <br><br> 1. A private key for the OAuth signature for API requests. It is recommended to keep the private key in a password-protected or hardware keystore. <br> 2. A public key is shared with Mastercard during the project setup process through either a certificate signing request (CSR) or the API Key Generator. Mastercard will use the public key to verify the OAuth signature that is provided on every API call.<br>  An OAUTH1.0a signer library is available on [GitHub](https://github.com/Mastercard/oauth1-signer-java) <br><br> **Encryption** <br><br> All communications between Issuer web service and the Mastercard gateway is encrypted using TLS. <br><br> **Additional Encryption of Sensitive Data** <br><br> In addition to the OAuth authentication, when using MDES Digital Enablement Service, any PCI sensitive and all account holder Personally Identifiable Information (PII) data must be encrypted. This requirement applies to the API fields containing encryptedData. Sensitive data is encrypted using a symmetric session (one-time-use) key. The symmetric session key is then wrapped with an RSA Public Key supplied by Mastercard during API setup phase (the Customer Encryption Key). <br>  Java Client Encryption Library available on [GitHub](https://github.com/Mastercard/client-encryption-java) 

    The version of the OpenAPI document: 1.3.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.token import Token

class TestToken(unittest.TestCase):
    """Token unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Token:
        """Test Token
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Token`
        """
        model = Token()
        if include_optional:
            return Token(
                token_unique_reference = 'DWSPMC000000000132d72d4fcb2f4136a0532d3093ff1a45',
                status = 'SUSPENDED',
                suspended_by = [
                    'CARDHOLDER'
                    ],
                status_timestamp = '',
                product_config = openapi_client.models.product_config.productConfig(
                    brand_logo_asset_id = '800200c9-629d-11e3-949a-0739d27e5a66', 
                    issuer_logo_asset_id = 'dbc55444-986a-4896-b41c-5d5e2dd431e2', 
                    is_co_branded = True, 
                    co_brand_name = 'Co brand partner', 
                    co_brand_logo_asset_id = 'dbc55444-496a-4896-b41c-5d5e2dd431e2', 
                    card_background_combined_asset_id = '739d27e5-629d-11e3-949a-0800200c9a66', 
                    card_background_asset_id = '456d27e5-629d-11e3-949a-0800200c9a66', 
                    icon_asset_id = '739d87e5-629d-11e3-949a-0800200c9a66', 
                    foreground_color = '0', 
                    issuer_name = 'Issuing Bank', 
                    short_description = 'Bank Rewards MasterCard', 
                    long_description = 'Bank Rewards MasterCard with the super duper rewards program', 
                    customer_service_url = 'https://bank.com/customerservice', 
                    customer_service_email = 'customerservice@bank.com', 
                    customer_service_phone_number = '1234567891', 
                    issuer_mobile_app = openapi_client.models.issuer_mobile_app.issuerMobileApp(), 
                    online_banking_login_url = 'bank.com', 
                    terms_and_conditions_url = 'https://bank.com/termsAndConditions', 
                    privacy_policy_url = 'https://bank.com/privacy', 
                    issuer_product_config_code = '123456', ),
                token_info = openapi_client.models.token_info.tokenInfo(
                    token_pan_suffix = '0001', 
                    account_pan_suffix = '0011', 
                    token_expiry = '921', 
                    account_pan_expiry = '921', 
                    dsrp_capable = 'true', 
                    token_assurance_level = 3, 
                    product_category = 'CREDIT', )
            )
        else:
            return Token(
        )
        """

    def testToken(self):
        """Test Token"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
