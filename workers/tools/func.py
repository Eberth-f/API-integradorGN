# -*- coding: utf-8 -*-

import logging


def get_logger(
        file_name,
        fmt='%(asctime)-15s - %(levelname)s - %(message)s',
        datefmt='%m/%d/%Y %H:%M:%S',
        rotate=False,
        logger_name=__name__
):

    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.INFO)

    formatter = logging.Formatter(
        fmt=fmt,
        datefmt=datefmt
    )

    if rotate:
        fh = logging.handlers.TimedRotatingFileHandler(
            file_name,
            when='midnight',
            backupCount=100,
            encoding='utf-8'
        )
    else:
        fh = logging.FileHandler(file_name, 'w', 'utf-8')

    fh.setFormatter(formatter)
    logger.addHandler(fh)
    logger.propagate = False

    ch = logging.StreamHandler()
    ch.setFormatter(formatter)
    logger.addHandler(ch)

    return logger
