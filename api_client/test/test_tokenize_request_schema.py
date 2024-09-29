# coding: utf-8

"""
    MDES Digital Enablement API

    These APIs are designed as RPC style stateless web services where each API endpoint represents an operation to be performed.  All request and response payloads are sent in the JSON (JavaScript Object Notation) data-interchange format. Each endpoint in the API specifies the HTTP Method used to access it. All strings in request and response objects are to be UTF-8 encoded.  Each API URI includes the major and minor version of API that it conforms to.  This will allow multiple concurrent versions of the API to be deployed simultaneously. <br><br> **Authentication** <br><br> Mastercard uses OAuth 1.0a with body hash extension for authenticating the API clients. This requires every request that you send to  Mastercard to be signed with an RSA private key. A private-public RSA key pair must be generated consisting of: <br><br> 1. A private key for the OAuth signature for API requests. It is recommended to keep the private key in a password-protected or hardware keystore. <br> 2. A public key is shared with Mastercard during the project setup process through either a certificate signing request (CSR) or the API Key Generator. Mastercard will use the public key to verify the OAuth signature that is provided on every API call.<br>  An OAUTH1.0a signer library is available on [GitHub](https://github.com/Mastercard/oauth1-signer-java) <br><br> **Encryption** <br><br> All communications between Issuer web service and the Mastercard gateway is encrypted using TLS. <br><br> **Additional Encryption of Sensitive Data** <br><br> In addition to the OAuth authentication, when using MDES Digital Enablement Service, any PCI sensitive and all account holder Personally Identifiable Information (PII) data must be encrypted. This requirement applies to the API fields containing encryptedData. Sensitive data is encrypted using a symmetric session (one-time-use) key. The symmetric session key is then wrapped with an RSA Public Key supplied by Mastercard during API setup phase (the Customer Encryption Key). <br>  Java Client Encryption Library available on [GitHub](https://github.com/Mastercard/client-encryption-java) 

    The version of the OpenAPI document: 1.3.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.tokenize_request_schema import TokenizeRequestSchema

class TestTokenizeRequestSchema(unittest.TestCase):
    """TokenizeRequestSchema unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TokenizeRequestSchema:
        """Test TokenizeRequestSchema
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TokenizeRequestSchema`
        """
        model = TokenizeRequestSchema()
        if include_optional:
            return TokenizeRequestSchema(
                response_host = 'site1.your-server.com',
                request_id = '123456',
                token_type = 'CLOUD',
                token_requestor_id = '98765432101',
                task_id = '123456',
                funding_account_info = openapi_client.models.funding_account_info.fundingAccountInfo(
                    pan_unique_reference = '', 
                    token_unique_reference = '', 
                    encrypted_payload = openapi_client.models.funding_account_info_encrypted_payload.fundingAccountInfo-EncryptedPayload(
                        public_key_fingerprint = '4c4ead5927f0df8117f178eea9308daa58e27c2b', 
                        encrypted_key = 'A1B2C3D4E5F6112233445566', 
                        oaep_hashing_algorithm = 'SHA512', 
                        iv = 'NA', 
                        encrypted_data = openapi_client.models.funding_account_data.FundingAccountData(
                            card_account_data = openapi_client.models.card_account_data_inbound.CardAccountData_inbound(
                                account_number = '5123456789012345', 
                                expiry_month = '09', 
                                expiry_year = '21', 
                                security_code = '123', ), 
                            account_holder_data = openapi_client.models.account_holder_data.accountHolderData(
                                account_holder_name = '', 
                                account_holder_address = openapi_client.models.billing_address.billingAddress(
                                    line1 = '100 1st Street', 
                                    line2 = 'Apt. 4B', 
                                    city = 'St. Louis', 
                                    country_subdivision = 'MO', 
                                    postal_code = '61000', 
                                    country = 'USA', ), 
                                consumer_identifier = '', 
                                account_holder_email_address = '', 
                                account_holder_mobile_phone_number = openapi_client.models.phone_number.PhoneNumber(
                                    country_dial_in_code = 44, 
                                    phone_number = 1.337, ), ), 
                            source = 'ACCOUNT_ON_FILE', ), ), ),
                consumer_language = 'en',
                tokenization_authentication_value = 'RHVtbXkgYmFzZSA2NCBkYXRhIC0gdGhpcyBpcyBub3QgYSByZWFsIFRBViBleGFtcGxl',
                decisioning_data = openapi_client.models.decisioning_data.DecisioningData(
                    recommendation = 'APPROVED', 
                    recommendation_algorithm_version = '01', 
                    device_score = '1', 
                    account_score = '1', 
                    recommendation_reasons = [
                        'LONG_ACCOUNT_TENURE'
                        ], 
                    device_current_location = '38.63,-90.25', 
                    device_ip_address = '127.0.0.1', 
                    mobile_number_suffix = '3456', 
                    account_id_hash = '', )
            )
        else:
            return TokenizeRequestSchema(
                token_type = 'CLOUD',
                token_requestor_id = '98765432101',
                task_id = '123456',
                funding_account_info = openapi_client.models.funding_account_info.fundingAccountInfo(
                    pan_unique_reference = '', 
                    token_unique_reference = '', 
                    encrypted_payload = openapi_client.models.funding_account_info_encrypted_payload.fundingAccountInfo-EncryptedPayload(
                        public_key_fingerprint = '4c4ead5927f0df8117f178eea9308daa58e27c2b', 
                        encrypted_key = 'A1B2C3D4E5F6112233445566', 
                        oaep_hashing_algorithm = 'SHA512', 
                        iv = 'NA', 
                        encrypted_data = openapi_client.models.funding_account_data.FundingAccountData(
                            card_account_data = openapi_client.models.card_account_data_inbound.CardAccountData_inbound(
                                account_number = '5123456789012345', 
                                expiry_month = '09', 
                                expiry_year = '21', 
                                security_code = '123', ), 
                            account_holder_data = openapi_client.models.account_holder_data.accountHolderData(
                                account_holder_name = '', 
                                account_holder_address = openapi_client.models.billing_address.billingAddress(
                                    line1 = '100 1st Street', 
                                    line2 = 'Apt. 4B', 
                                    city = 'St. Louis', 
                                    country_subdivision = 'MO', 
                                    postal_code = '61000', 
                                    country = 'USA', ), 
                                consumer_identifier = '', 
                                account_holder_email_address = '', 
                                account_holder_mobile_phone_number = openapi_client.models.phone_number.PhoneNumber(
                                    country_dial_in_code = 44, 
                                    phone_number = 1.337, ), ), 
                            source = 'ACCOUNT_ON_FILE', ), ), ),
        )
        """

    def testTokenizeRequestSchema(self):
        """Test TokenizeRequestSchema"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
