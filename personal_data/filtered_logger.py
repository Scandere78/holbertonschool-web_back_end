#!/usr/bin/env python3
"""Module that provides a function to obfuscate sensitive data in logs."""
import re
from typing import List


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """
    Obfuscate specified fields in a log message.

    Args:
        fields (List[str]): List of fields to redact (e.g., ["password"]).
        redaction (str): The string to replace the sensitive data with.
        message (str): The log message containing the data to be filtered.
        separator (str): The character separating the fields in the message.

    Returns:
        str: The log message with sensitive fields redacted.
    """
    pattern = rf'({"|".join(fields)})=.*?{re.escape(separator)}'
    return re.sub(pattern,
                  lambda m: f"{m.group(1)}={redaction}{separator}",
                  message)
