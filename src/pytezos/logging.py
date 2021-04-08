import logging
import logging.config

DEFAULT_LOGGING_CONFIG = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'brief': {
            'format': '%(message)s',
        },
    },
    'handlers': {
        'default': {
            'class': 'logging.StreamHandler',
            'formatter': 'brief',
            'stream': 'ext://sys.stdout',
        }
    },
    'root': {
        'handlers': ['default'],
        'level': 'INFO',
        'propagate': False
    }
}


if not logging.getLogger().hasHandlers():
    logging.config.dictConfig(DEFAULT_LOGGING_CONFIG)

logger = logging.getLogger('pytezos')
