import dataclasses
import pandas as pd
from src.data.AbstractData import AbstractData
from src.logservice.ILoggerService import ILoggerService


@dataclasses.dataclass
class DataBase(AbstractData):

    def __init__(self, config, logger=ILoggerService):
        self.logger = logger
        self.server = config["server"]
        self.user_name = config["user_name"]
        self.key = config["key"]
        self.data_base = config["database"]
        if self.user_name == "":
            self.con_str = "mssql+pyodbc://" + self.server + "/" + self.data_base + "?driver=SQL Server?Trusted_Connection=yes"
        else:
            self.con_str = "mssql+pymssql://" + self.user_name + ":" + self.key + self.server + "/" + self.data_base

    def load(self, query, param=None) -> pd.DataFrame:
        self.logger.debug(self.con_str)
        return pd.read_sql(query, self.con_str)

    def save(self, data_frame: pd.DataFrame, data_table_name, param=None) -> None:
        param = self._pre_save(param)
        data_frame.to_sql(data_table_name, self.con_str, if_exists=param["if_exists"],
                          chunksize=param["chunksize"], index=False)

    def _pre_save(self, param):
        if param is None:
            param = {}
        if "if_exists" not in param.keys():
            param["if_exists"] = 'append'
        if "chunksize" not in param.keys():
            param["chunksize"] = 100
        return param
