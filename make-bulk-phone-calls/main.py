import os
from rapida import (
    ConnectionConfig,
    create_bulk_phone_call,
    CreatePhoneCallRequest,
    CreateBulkPhoneCallRequest,
    AssistantDefinition,
)
from pprint import pprint

connectionConfig = ConnectionConfig.default_connection_config(
    ConnectionConfig.with_sdk(os.getenv("RAPIDA_PROJECT_KEY"))
)

# connectionConfig = ConnectionConfig.default_connection_config(
#     ConnectionConfig.with_personal_token(
#         authorization=os.getenv("AUTH_TOKEN"),
#         auth_id=os.getenv("AUTH_ID"),
#         project_id=os.getenv("PROJECT_ID"),
#     )
# )

call = CreatePhoneCallRequest(
    assistant=AssistantDefinition(assistantId={ASSISTANT_ID}),
    toNumber="{TO_PHONE}",
)
response = create_bulk_phone_call(
    client_cfg=connectionConfig,
    request=CreateBulkPhoneCallRequest(
        phoneCalls=[call],
    ),
)
pprint.pprint(response)
