#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging


def get_logger(name):
    """Returns logger which logs to console and /var/log/syslog

    Returns:
        logger -- Logger that can be used for logging
    """
    logger = logging.getLogger(name)
    if not logger.handlers:
        logger.setLevel(logging.INFO)

        log_formatter = logging.Formatter("%(asctime)s -- %(message)s")

        sys_handler = logging.FileHandler('/var/log/syslog')
        sys_handler.setFormatter(log_formatter)
        logger.addHandler(sys_handler)

        console_handler = logging.StreamHandler()
        console_handler.setFormatter(log_formatter)
        logger.addHandler(console_handler)

    return logger
