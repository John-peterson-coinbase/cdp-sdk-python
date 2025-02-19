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

from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing_extensions import Self


class SponsoredSend(BaseModel):
    """An onchain sponsored gasless send."""

    to_address_id: StrictStr = Field(description="The onchain address of the recipient")
    raw_typed_data: StrictStr = Field(description="The raw typed data for the sponsored send")
    typed_data_hash: StrictStr = Field(
        description="The typed data hash for the sponsored send. This is the typed data hash that needs to be signed by the sender."
    )
    signature: StrictStr | None = Field(
        default=None, description="The signed hash of the sponsored send typed data."
    )
    transaction_hash: StrictStr | None = Field(
        default=None, description="The hash of the onchain sponsored send transaction"
    )
    transaction_link: StrictStr | None = Field(
        default=None,
        description="The link to view the transaction on a block explorer. This is optional and may not be present for all transactions.",
    )
    status: StrictStr = Field(description="The status of the sponsored send")
    __properties: ClassVar[list[str]] = [
        "to_address_id",
        "raw_typed_data",
        "typed_data_hash",
        "signature",
        "transaction_hash",
        "transaction_link",
        "status",
    ]

    @field_validator("status")
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(["pending", "signed", "submitted", "complete", "failed"]):
            raise ValueError(
                "must be one of enum values ('pending', 'signed', 'submitted', 'complete', 'failed')"
            )
        return value

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
        """Create an instance of SponsoredSend from a JSON string"""
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
        """Create an instance of SponsoredSend from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "to_address_id": obj.get("to_address_id"),
                "raw_typed_data": obj.get("raw_typed_data"),
                "typed_data_hash": obj.get("typed_data_hash"),
                "signature": obj.get("signature"),
                "transaction_hash": obj.get("transaction_hash"),
                "transaction_link": obj.get("transaction_link"),
                "status": obj.get("status"),
            }
        )
        return _obj
