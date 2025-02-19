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

from pydantic import BaseModel, ConfigDict
from typing_extensions import Self

from cdp.client.models.balance import Balance


class StakingContextContext(BaseModel):
    """StakingContextContext"""

    stakeable_balance: Balance
    unstakeable_balance: Balance
    claimable_balance: Balance
    __properties: ClassVar[list[str]] = [
        "stakeable_balance",
        "unstakeable_balance",
        "claimable_balance",
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
        """Create an instance of StakingContextContext from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of stakeable_balance
        if self.stakeable_balance:
            _dict["stakeable_balance"] = self.stakeable_balance.to_dict()
        # override the default output from pydantic by calling `to_dict()` of unstakeable_balance
        if self.unstakeable_balance:
            _dict["unstakeable_balance"] = self.unstakeable_balance.to_dict()
        # override the default output from pydantic by calling `to_dict()` of claimable_balance
        if self.claimable_balance:
            _dict["claimable_balance"] = self.claimable_balance.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict[str, Any] | None) -> Self | None:
        """Create an instance of StakingContextContext from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "stakeable_balance": Balance.from_dict(obj["stakeable_balance"])
                if obj.get("stakeable_balance") is not None
                else None,
                "unstakeable_balance": Balance.from_dict(obj["unstakeable_balance"])
                if obj.get("unstakeable_balance") is not None
                else None,
                "claimable_balance": Balance.from_dict(obj["claimable_balance"])
                if obj.get("claimable_balance") is not None
                else None,
            }
        )
        return _obj
