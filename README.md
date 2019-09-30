# HAC
H`VAC` A`uto` C`lient`

This is a temporary repo while i work on the initial version of the HVAC Auto Client (HAC), a hashicorp vault python client generated from OpenAPI 3.0 spec

Testing in hashicorp_vault_client/client.py
```
import hashicorp_vault_client
from hashicorp_vault_client.api.system_api import SystemApi

vault_url = 'http://127.0.0.1:8205'

client = SystemApi()
print(client.get_sys_health(vault_url))
```

Error output:
```
python hashicorp_vault_client/client.py
Traceback (most recent call last):
  File "hashicorp_vault_client/client.py", line 7, in <module>
    print(client.get_sys_health(vault_url))
TypeError: get_sys_health() takes 1 positional argument but 2 were given
```

