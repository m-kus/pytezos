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

logger = logging.getLogger('pytezos')
