import logging
import logging.config
import sys


LOG_LEVEL = 'DEBUG'
LOG_HANDLERS = ['console']

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '[%(levelname)s - %(created)s] file:%(module)s.py, func:%(funcName)s, ln:%(lineno)s: %(message)s'
        },
        'simple': {
            'format': '%(message)s'
        }
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
            'stream': sys.stderr
        },
    },
    'loggers': {
        'skaio_logger': {
            'handlers': LOG_HANDLERS,
            'level': LOG_LEVEL,
            'propagate': True,
        },
    }
}
logging.config.dictConfig(LOGGING)


def get_logger():
    logger = logging.getLogger('skaio_logger')
    logger.setLevel(LOG_LEVEL)
    return logger


log = get_logger()
