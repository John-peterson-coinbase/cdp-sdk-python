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
from datetime import datetime
from typing import Any, ClassVar

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing_extensions import Self

from cdp.client.models.balance import Balance


class StakingBalance(BaseModel):
    """The staking balances for an address."""

    address: StrictStr = Field(
        description="The onchain address for which the staking balances are being fetched."
    )
    var_date: datetime = Field(
        description="The timestamp of the staking balance in UTC.", alias="date"
    )
    bonded_stake: Balance
    unbonded_balance: Balance
    participant_type: StrictStr = Field(description="The type of staking participation.")
    __properties: ClassVar[list[str]] = [
        "address",
        "date",
        "bonded_stake",
        "unbonded_balance",
        "participant_type",
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
        """Create an instance of StakingBalance from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of bonded_stake
        if self.bonded_stake:
            _dict["bonded_stake"] = self.bonded_stake.to_dict()
        # override the default output from pydantic by calling `to_dict()` of unbonded_balance
        if self.unbonded_balance:
            _dict["unbonded_balance"] = self.unbonded_balance.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict[str, Any] | None) -> Self | None:
        """Create an instance of StakingBalance from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "address": obj.get("address"),
                "date": obj.get("date"),
                "bonded_stake": Balance.from_dict(obj["bonded_stake"])
                if obj.get("bonded_stake") is not None
                else None,
                "unbonded_balance": Balance.from_dict(obj["unbonded_balance"])
                if obj.get("unbonded_balance") is not None
                else None,
                "participant_type": obj.get("participant_type"),
            }
        )
        return _obj
