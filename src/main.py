from dependency_injector import containers, providers
from data.DataBaseContainer import DataBaseContainer
from src.logservice.LoggerService import LoggerService
from src.services.CallModelService import CallModelService


class Container(containers.DeclarativeContainer):
    """
    Contaner go dependac
    """
    logger = providers.Singleton(LoggerService)
    data_base_container = providers.Singleton(DataBaseContainer,
                                              logger=logger,
                                              path = r"D:\GYLD\GIT\Artificial%20Intelligence\Bot\parameters.json"
                                              )
    call_model_service = providers.Factory(
        CallModelService,
        data_base=data_base_container,
        logger=logger
    )


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    """
    dfdf
    dfdf
    """
    container = Container()
    logger = container.logger()
    data_base_container = container.data_base_container()
    call_model_service = container.call_model_service()

    try:
        data = {"description": "Who is the Platon?"}
        call_model_service.call("http://10.200.205.139:8080/infere_bard_api", data)

    except Exception as ex:
        logger.error(ex)
        logger.error(ex)
