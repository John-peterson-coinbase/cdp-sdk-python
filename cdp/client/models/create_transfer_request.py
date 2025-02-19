"""Coinbase Platform API

This is the OpenAPI 3.0 specification for the Coinbase Platform APIs, used in conjunction with the Coinbase Platform SDKs.

The version of the OpenAPI document: 0.0.1-alpha
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""

from __future__ import annotations

import json
import pprint
import re  # noqa: F401
from typing import Any, ClassVar

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing_extensions import Self


class CreateTransferRequest(BaseModel):
    """CreateTransferRequest"""

    amount: StrictStr = Field(description="The amount to transfer")
    network_id: StrictStr = Field(description="The ID of the blockchain network")
    asset_id: StrictStr = Field(description="The ID of the asset to transfer")
    destination: StrictStr = Field(
        description="The destination address, which can be a 0x address, Basename, or ENS name"
    )
    gasless: StrictBool | None = Field(
        default=None, description="Whether the transfer uses sponsored gas"
    )
    __properties: ClassVar[list[str]] = [
        "amount",
        "network_id",
        "asset_id",
        "destination",
        "gasless",
    ]

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
    def from_json(cls, json_str: str) -> Self | None:
        """Create an instance of CreateTransferRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: set[str] = set([])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: dict[str, Any] | None) -> Self | None:
        """Create an instance of CreateTransferRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "amount": obj.get("amount"),
                "network_id": obj.get("network_id"),
                "asset_id": obj.get("asset_id"),
                "destination": obj.get("destination"),
                "gasless": obj.get("gasless"),
            }
        )
        return _obj
