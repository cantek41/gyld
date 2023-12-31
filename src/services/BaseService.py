import abc

from gyld.sdk.data.DataBaseContainer import DataBaseContainer
from gyld.sdk.logservice.LoggerService import ILoggerService


class BaseService(metaclass=abc.ABCMeta):

    def __init__(self, data_base: DataBaseContainer, logger: ILoggerService, **kwargs):
        self.data_base_container = data_base
        self.data_base_bot = data_base
        self.data_base_bot = data_base.data_base_bot
        self.data_base_warehouse = data_base.data_base_warehouse
        self.data_base_mining = data_base.data_base_mining
        self.logger = logger
        self.bootstrap(**kwargs)

    def bootstrap(self, **kwargs):
        pass

    def run(self, **kwargs):
        raise NotImplemented
