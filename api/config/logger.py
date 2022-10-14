"""
Logger config
"""

import os
from loguru import logger

logs_dir = os.path.join(os.path.dirname(__file__), "logs")


def full_path(file_name):
    """
    fn for getting full path
    """
    return os.path.join(logs_dir, file_name)


logger.add(
    full_path("info.log"),
    format="{time} {message}",
    level="INFO",
    enqueue=True,
    colorize=True,
)
logger.add(
    full_path("error.log"),
    format="{time} {message}",
    level="ERROR",
    enqueue=True,
    colorize=True,
)
