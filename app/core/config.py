JWT_SECRET_KEY = '693364d5ccaf48dd5ad582fef7bd190591401694551819386b62ee9bd41ccf01'
ALGORITHM = "HS256"

logging_config = {
    "version": 1,
    "formatters": {
        "custom-json": {
            "class": "pythonjsonlogger.jsonlogger.JsonFormatter",
            "format": "%(asctime)s %(process)s %(levelname)s %(name)s %(module)s %(funcName)s %(lineno)s"
        }
    },
    "handlers": {
        "elastic-search": {
            "level": "INFO",
            "class": "app.log.elastic_handler.ElasticHandler",
            "formatter": "custom-json",
        },
    },
    "loggers": {
        "elastic-logger": {
            "level": "INFO",
            "handlers": ["elastic-search"],
            "propagate": True
        },
    },
}
