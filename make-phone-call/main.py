import os
from rapida import (
    ConnectionConfig,
    create_phone_call,
    CreatePhoneCallRequest,
    AssistantDefinition,
)
from pprint import pprint

connectionConfig = ConnectionConfig.default_connection_config(
    ConnectionConfig.with_sdk(os.getenv("RAPIDA_PROJECT_KEY"))
)
call = CreatePhoneCallRequest(
    assistant=AssistantDefinition(assistantId={ASSISTANT_ID}),
    toNumber="{TO_PHONE}",
)
response = create_phone_call(client_cfg=connectionConfig, request=call)
pprint.pprint(response)
