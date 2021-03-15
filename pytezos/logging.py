import logging
import logging.config

DEFAULT_LOGGER_CONFIG = {
    'version': 1,
    'formatters': {
        'brief': {
            'format': '%(message)s',
        },
    },
    'loggers': {
        'urllib3.connectionpool': {
            'level': 'INFO',
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

logging.config.dictConfig(DEFAULT_LOGGER_CONFIG)
logger = logging.getLogger()
