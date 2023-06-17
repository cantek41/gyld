import json

from src.data.DataBase import DataBase
from src.logservice.ILoggerService import ILoggerService


class DataBaseContainer:
    def __init__(self, path="", logger=ILoggerService):
        self.logger = logger
        config = open(path)
        self.param = json.load(config)
        self.data_base_bot = DataBase(self.param["BOT"], self.logger)
        self.data_base_warehouse = DataBase(self.param["WAREHOUSE"], self.logger)
        self.data_base_mining = DataBase(self.param["TEMP"], self.logger)
