import logging

def create_logger(conf_class=object):

    dict_config = {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'standard': {
                'format': '%(levelname)s - %(asctime)s - %(message)s'
            },
        },
        'handlers': {
            'default': {
                'class': 'logging.handlers.RotatingFileHandler',
                'level': 'INFO',
                'formatter': 'standard',
                'filename': 'logs/celery.log',
                'maxBytes': 1048576,  # 1 MB
                'backupCount': 5,
                'encoding': 'utf8'
            },
            "console": {
                "class": "logging.StreamHandler",
                "level": "ERROR",
                "formatter": "standard",
                "stream": "ext://sys.stdout"
            },
            'application': {
                'class': 'logging.handlers.RotatingFileHandler',
                'level': 'INFO',
                'formatter': 'standard',
                'filename': 'logs/celery_app.log',
                'maxBytes': 1048576, # 1 MB
                'backupCount': 5,
                'encoding': 'utf8'
            }
        },
        'loggers': {
            'applicationLogger': {
                'handlers': ['application'],
                'level': 'INFO',
                'propagate': False
            },
            '': {
                'handlers': ['default'],
                'level': 'DEBUG',
                'propagate': False
            }
        }
    }
    logging.config.dictConfig(dict_config)
    logger = logging.getLogger('applicationLogger')
    logger.info("Logger initialized")
    return logger