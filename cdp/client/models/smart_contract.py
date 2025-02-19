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

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing_extensions import Self

from cdp.client.models.smart_contract_options import SmartContractOptions
from cdp.client.models.smart_contract_type import SmartContractType
from cdp.client.models.transaction import Transaction


class SmartContract(BaseModel):
    """Represents a smart contract on the blockchain"""

    smart_contract_id: StrictStr = Field(description="The unique identifier of the smart contract")
    network_id: StrictStr = Field(description="The name of the blockchain network")
    wallet_id: StrictStr = Field(
        description="The ID of the wallet that deployed the smart contract"
    )
    contract_address: StrictStr = Field(description="The EVM address of the smart contract")
    deployer_address: StrictStr = Field(
        description="The EVM address of the account that deployed the smart contract"
    )
    type: SmartContractType
    options: SmartContractOptions
    abi: StrictStr = Field(description="The JSON-encoded ABI of the contract")
    transaction: Transaction
    __properties: ClassVar[list[str]] = [
        "smart_contract_id",
        "network_id",
        "wallet_id",
        "contract_address",
        "deployer_address",
        "type",
        "options",
        "abi",
        "transaction",
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
        """Create an instance of SmartContract from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of options
        if self.options:
            _dict["options"] = self.options.to_dict()
        # override the default output from pydantic by calling `to_dict()` of transaction
        if self.transaction:
            _dict["transaction"] = self.transaction.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict[str, Any] | None) -> Self | None:
        """Create an instance of SmartContract from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "smart_contract_id": obj.get("smart_contract_id"),
                "network_id": obj.get("network_id"),
                "wallet_id": obj.get("wallet_id"),
                "contract_address": obj.get("contract_address"),
                "deployer_address": obj.get("deployer_address"),
                "type": obj.get("type"),
                "options": SmartContractOptions.from_dict(obj["options"])
                if obj.get("options") is not None
                else None,
                "abi": obj.get("abi"),
                "transaction": Transaction.from_dict(obj["transaction"])
                if obj.get("transaction") is not None
                else None,
            }
        )
        return _obj
