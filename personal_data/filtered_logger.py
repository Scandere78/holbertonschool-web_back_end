#!/usr/bin/env python3
"""Module that provides a function to obfuscate sensitive data in logs."""
import re
import logging
from typing import List
import os
import mysql.connector
from mysql.connector.connection import MySQLConnection

PII_FIELDS = ("name", "email", "phone", "ssn", "password")


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


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """Initialize the formatter with fields to redact"""
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """Format the log record, redacting sensitive fields"""
        original_message = super().format(record)
        return filter_datum(self.fields, self.REDACTION,
                            original_message, self.SEPARATOR)


def get_logger() -> logging.Logger:
    """
    Creates and configures a logger to redact PII in logs.

    Returns:
        logging.Logger: Configured logger named 'user_data'
    """

    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(RedactingFormatter(fields=PII_FIELDS))
    logger.addHandler(stream_handler)
    return logger

def get_db() -> MySQLConnection:
    """
    Connects to a MySQL database using credentials from environment variables.

    Returns:
        MySQLConnection: A MySQL database connection object
    """
    return mysql.connector.connect(
        user=os.getenv("PERSONAL_DATA_DB_USERNAME", "root"),
        password=os.getenv("PERSONAL_DATA_DB_PASSWORD", ""),
        host=os.getenv("PERSONAL_DATA_DB_HOST", "localhost"),
        database=os.getenv("PERSONAL_DATA_DB_NAME")
    )
