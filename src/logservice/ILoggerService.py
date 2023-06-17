from abc import ABCMeta, abstractmethod


class ILoggerService(metaclass=ABCMeta):

    # set up logging to file - see previous section for more details
    @abstractmethod
    def config(self) -> None:
        pass

    @abstractmethod
    def info(self, message) -> None:
        pass

    @abstractmethod
    def debug(self, message) -> None:
        pass

    @abstractmethod
    def warning(self, message) -> None:
        pass

    @abstractmethod
    def error(self, message) -> None:
        pass
