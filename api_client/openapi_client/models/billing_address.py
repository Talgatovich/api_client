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
from typing import Optional, Set
from typing_extensions import Self

class BillingAddress(BaseModel):
    """
    BillingAddress
    """ # noqa: E501
    line1: Optional[Annotated[str, Field(strict=True, max_length=64)]] = Field(default=None, description="**(OPTIONAL)** The first line of the street address for the billing address. ")
    line2: Optional[Annotated[str, Field(strict=True, max_length=64)]] = Field(default=None, description="**(OPTIONAL)** The second line of the street address for the billing address. ")
    city: Optional[Annotated[str, Field(strict=True, max_length=32)]] = Field(default=None, description="**(OPTIONAL)** The city of the billing address. ")
    country_subdivision: Optional[Annotated[str, Field(strict=True, max_length=12)]] = Field(default=None, description="**(OPTIONAL)** The state or country subdivision of the billing address. ", alias="countrySubdivision")
    postal_code: Optional[Annotated[str, Field(strict=True, max_length=16)]] = Field(default=None, description="**(OPTIONAL)** The postal of code of the billing address. ", alias="postalCode")
    country: Optional[Annotated[str, Field(strict=True, max_length=3)]] = Field(default=None, description="**(OPTIONAL)** The country of the billing address. ")
    __properties: ClassVar[List[str]] = ["line1", "line2", "city", "countrySubdivision", "postalCode", "country"]

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
        """Create an instance of BillingAddress from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of BillingAddress from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "line1": obj.get("line1"),
            "line2": obj.get("line2"),
            "city": obj.get("city"),
            "countrySubdivision": obj.get("countrySubdivision"),
            "postalCode": obj.get("postalCode"),
            "country": obj.get("country")
        })
        return _obj


