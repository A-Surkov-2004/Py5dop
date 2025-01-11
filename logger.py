import logging


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Logger(metaclass=Singleton):
    instances = 0

    def __init__(self):
        Logger.instances += 1
        self.py_logger = logging.getLogger(__name__)
        self.py_logger.setLevel(logging.INFO)
        self.py_handler = logging.FileHandler(f"{__name__}.log", mode='w')
        self.py_formatter = logging.Formatter("%(name)s %(asctime)s %(levelname)s %(message)s")
        self.py_handler.setFormatter(self.py_formatter)
        self.py_logger.addHandler(self.py_handler)

    def info(self, string: str):
        self.py_logger.info(string)

    def warn(self, string: str):
        self.py_logger.warning(string)

    def error(self, string: str):
        self.py_logger.error(string)
