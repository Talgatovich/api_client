# coding: utf-8

"""
    MDES Digital Enablement API

    These APIs are designed as RPC style stateless web services where each API endpoint represents an operation to be performed.  All request and response payloads are sent in the JSON (JavaScript Object Notation) data-interchange format. Each endpoint in the API specifies the HTTP Method used to access it. All strings in request and response objects are to be UTF-8 encoded.  Each API URI includes the major and minor version of API that it conforms to.  This will allow multiple concurrent versions of the API to be deployed simultaneously. <br><br> **Authentication** <br><br> Mastercard uses OAuth 1.0a with body hash extension for authenticating the API clients. This requires every request that you send to  Mastercard to be signed with an RSA private key. A private-public RSA key pair must be generated consisting of: <br><br> 1. A private key for the OAuth signature for API requests. It is recommended to keep the private key in a password-protected or hardware keystore. <br> 2. A public key is shared with Mastercard during the project setup process through either a certificate signing request (CSR) or the API Key Generator. Mastercard will use the public key to verify the OAuth signature that is provided on every API call.<br>  An OAUTH1.0a signer library is available on [GitHub](https://github.com/Mastercard/oauth1-signer-java) <br><br> **Encryption** <br><br> All communications between Issuer web service and the Mastercard gateway is encrypted using TLS. <br><br> **Additional Encryption of Sensitive Data** <br><br> In addition to the OAuth authentication, when using MDES Digital Enablement Service, any PCI sensitive and all account holder Personally Identifiable Information (PII) data must be encrypted. This requirement applies to the API fields containing encryptedData. Sensitive data is encrypted using a symmetric session (one-time-use) key. The symmetric session key is then wrapped with an RSA Public Key supplied by Mastercard during API setup phase (the Customer Encryption Key). <br>  Java Client Encryption Library available on [GitHub](https://github.com/Mastercard/client-encryption-java) 

    The version of the OpenAPI document: 1.3.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.transact_response_schema import TransactResponseSchema

class TestTransactResponseSchema(unittest.TestCase):
    """TransactResponseSchema unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TransactResponseSchema:
        """Test TransactResponseSchema
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TransactResponseSchema`
        """
        model = TransactResponseSchema()
        if include_optional:
            return TransactResponseSchema(
                response_id = '',
                response_host = 'site2.payment-app-provider.com',
                encrypted_payload = openapi_client.models.encrypted_payload_transact.encryptedPayloadTransact(
                    public_key_fingerprint = '4c4ead5927f0df8117f178eea9308daa58e27c2b', 
                    encrypted_key = 'A1B2C3D4E5F6112233445566', 
                    oaep_hashing_algorithm = 'SHA512', 
                    iv = 'NA', 
                    encrypted_data = openapi_client.models.transact_encrypted_data.transactEncryptedData(
                        account_number = '5480981500100002', 
                        application_expiry_date = '210931', 
                        pan_sequence_number = '01', 
                        track2_equivalent = '5480981500100002D18112011000000000000F', 
                        de48se43_data = '11223344556677889900112233445566778899', ), )
            )
        else:
            return TransactResponseSchema(
        )
        """

    def testTransactResponseSchema(self):
        """Test TransactResponseSchema"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
