import hashicorp_vault_client
from hashicorp_vault_client.api.system_api import SystemApi

vault_url = 'http://127.0.0.1:8205'

client = SystemApi()
print(client.get_sys_health(vault_url))

