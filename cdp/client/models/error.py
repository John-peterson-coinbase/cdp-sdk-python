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
from typing import Annotated, Any, ClassVar

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing_extensions import Self


class Error(BaseModel):
    """An error response from the Coinbase Developer Platform API"""

    code: Annotated[str, Field(strict=True, max_length=5000)] = Field(
        description="A short string representing the reported error. Can be use to handle errors programmatically."
    )
    message: Annotated[str, Field(strict=True, max_length=5000)] = Field(
        description="A human-readable message providing more details about the error."
    )
    correlation_id: StrictStr | None = Field(
        default=None,
        description="A unique identifier for the request that generated the error. This can be used to help debug issues with the API.",
    )
    __properties: ClassVar[list[str]] = ["code", "message", "correlation_id"]

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
        """Create an instance of Error from a JSON string"""
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
        """Create an instance of Error from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "code": obj.get("code"),
                "message": obj.get("message"),
                "correlation_id": obj.get("correlation_id"),
            }
        )
        return _obj
