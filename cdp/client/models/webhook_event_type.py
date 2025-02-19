"""Coinbase Platform API

This is the OpenAPI 3.0 specification for the Coinbase Platform APIs, used in conjunction with the Coinbase Platform SDKs.

The version of the OpenAPI document: 0.0.1-alpha
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""

from __future__ import annotations

import json
from enum import Enum

from typing_extensions import Self


class WebhookEventType(str, Enum):
    """WebhookEventType"""

    """
    allowed enum values
    """
    UNSPECIFIED = "unspecified"
    ERC20_TRANSFER = "erc20_transfer"
    ERC721_TRANSFER = "erc721_transfer"
    WALLET_ACTIVITY = "wallet_activity"

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of WebhookEventType from a JSON string"""
        return cls(json.loads(json_str))
