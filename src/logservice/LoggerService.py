from gyld.sdk.logservice.ILoggerService import ILoggerService
import logging
from datetime import datetime


class LoggerService(ILoggerService):

    def __init__(self, name="athena", folder="logs"):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)
        self.folder = folder
        self.config()

    def config(self) -> None:
        formatter = logging.Formatter('%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
        LOG_FILENAME = datetime.now().strftime(f'{self.folder}/logfile_Steam_Data_Generator_%Y_%m_%d.log')
        file_handler = logging.FileHandler(LOG_FILENAME)
        file_handler.setLevel(logging.INFO)
        file_handler.setFormatter(formatter)

        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.DEBUG)
        console_handler.setFormatter(formatter)

        self.logger.addHandler(file_handler)
        self.logger.addHandler(console_handler)

    def info(self, message) -> None:
        self.logger.info(message)

    def debug(self, message) -> None:
        self.logger.debug(message)

    def warning(self, message) -> None:
        self.logger.warning(message)

    def error(self, message) -> None:
        self.logger.error(message)
