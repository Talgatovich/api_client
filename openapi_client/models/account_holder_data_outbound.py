# coding: utf-8

"""
    MDES Digital Enablement API

    These APIs are designed as RPC style stateless web services where each API endpoint represents an operation to be performed.  All request and response payloads are sent in the JSON (JavaScript Object Notation) data-interchange format. Each endpoint in the API specifies the HTTP Method used to access it. All strings in request and response objects are to be UTF-8 encoded.  Each API URI includes the major and minor version of API that it conforms to.  This will allow multiple concurrent versions of the API to be deployed simultaneously. <br><br> **Authentication** <br><br> Mastercard uses OAuth 1.0a with body hash extension for authenticating the API clients. This requires every request that you send to  Mastercard to be signed with an RSA private key. A private-public RSA key pair must be generated consisting of: <br><br> 1. A private key for the OAuth signature for API requests. It is recommended to keep the private key in a password-protected or hardware keystore. <br> 2. A public key is shared with Mastercard during the project setup process through either a certificate signing request (CSR) or the API Key Generator. Mastercard will use the public key to verify the OAuth signature that is provided on every API call.<br>  An OAUTH1.0a signer library is available on [GitHub](https://github.com/Mastercard/oauth1-signer-java) <br><br> **Encryption** <br><br> All communications between Issuer web service and the Mastercard gateway is encrypted using TLS. <br><br> **Additional Encryption of Sensitive Data** <br><br> In addition to the OAuth authentication, when using MDES Digital Enablement Service, any PCI sensitive and all account holder Personally Identifiable Information (PII) data must be encrypted. This requirement applies to the API fields containing encryptedData. Sensitive data is encrypted using a symmetric session (one-time-use) key. The symmetric session key is then wrapped with an RSA Public Key supplied by Mastercard during API setup phase (the Customer Encryption Key). <br>  Java Client Encryption Library available on [GitHub](https://github.com/Mastercard/client-encryption-java) 

    The version of the OpenAPI document: 1.3.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from openapi_client.models.billing_address import BillingAddress
from openapi_client.models.phone_number import PhoneNumber
from typing import Optional, Set
from typing_extensions import Self

class AccountHolderDataOutbound(BaseModel):
    """
    **(CONDITIONAL)** Present in tokenize response if supported by the Merchant, if using a pushAccountReceipt and if there is account holder data associated with the pushAccountReceipt in case that the issuer decision is APPROVED. Refer to MDES Token Connect Token Requestor Implementation Guide and Specification  for more details. 
    """ # noqa: E501
    account_holder_name: Optional[Annotated[str, Field(strict=True, max_length=27)]] = Field(default=None, description="**(OPTIONAL)** The name of the cardholder ", alias="accountHolderName")
    account_holder_address: Optional[BillingAddress] = Field(default=None, alias="accountHolderAddress")
    account_holder_email_address: Optional[Annotated[str, Field(strict=True, max_length=320)]] = Field(default=None, description="**(OPTIONAL)** The e-mail address of the Account Holder ", alias="accountHolderEmailAddress")
    account_holder_mobile_phone_number: Optional[PhoneNumber] = Field(default=None, alias="accountHolderMobilePhoneNumber")
    __properties: ClassVar[List[str]] = ["accountHolderName", "accountHolderAddress", "accountHolderEmailAddress", "accountHolderMobilePhoneNumber"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of AccountHolderDataOutbound from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of account_holder_address
        if self.account_holder_address:
            _dict['accountHolderAddress'] = self.account_holder_address.to_dict()
        # override the default output from pydantic by calling `to_dict()` of account_holder_mobile_phone_number
        if self.account_holder_mobile_phone_number:
            _dict['accountHolderMobilePhoneNumber'] = self.account_holder_mobile_phone_number.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AccountHolderDataOutbound from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "accountHolderName": obj.get("accountHolderName"),
            "accountHolderAddress": BillingAddress.from_dict(obj["accountHolderAddress"]) if obj.get("accountHolderAddress") is not None else None,
            "accountHolderEmailAddress": obj.get("accountHolderEmailAddress"),
            "accountHolderMobilePhoneNumber": PhoneNumber.from_dict(obj["accountHolderMobilePhoneNumber"]) if obj.get("accountHolderMobilePhoneNumber") is not None else None
        })
        return _obj


