from rapida import (
    ConnectionConfig,
    Criteria,
    GetAllAssistantRequest,
    GetAssistantRequest,
    Paginate,
    get_assistant,
    get_all_assistant,
)
from pprint import pprint


def fetch_assistant():
    connection_config = ConnectionConfig.default_connection_config(
        ConnectionConfig.with_sdk(
            "9eaaf1742be1ea0b3040ac34902e22b1182d3339127e939e499464715d472600"
        )
    ).with_local()
    response = get_assistant(
        client_cfg=connection_config,
        request=GetAssistantRequest(id=2223006263292198912),
    )
    pprint(response)


def get_all_assistant_list():
    connection_config = ConnectionConfig.default_connection_config(
        ConnectionConfig.with_sdk(
            "9eaaf1742be1ea0b3040ac34902e22b1182d3339127e939e499464715d472600"
        )
    ).with_local()
    response = get_all_assistant(
        client_cfg=connection_config,
        request=GetAllAssistantRequest(
            paginate=Paginate(page=0, pageSize=20),
            criterias=[Criteria(key="KEY", value="VALUE", logic="should")],
        ),
    )
    pprint(response)


if __name__ == "__main__":
    # get_all_endpoint_log_list()
    get_all_assistant_list()
