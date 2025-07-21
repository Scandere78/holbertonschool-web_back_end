#!/usr/bin/env python3
""" Module that provides a function to obfuscate sensitive data in logs """
import re
from typing import List


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    pattern = rf'({"|".join(fields)})=.*?{re.escape(separator)}'
    return re.sub(pattern,
                  lambda m: f"{m.group(1)}={redaction}{separator}",
                  message)
