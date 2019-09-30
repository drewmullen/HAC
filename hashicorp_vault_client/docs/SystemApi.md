# hashicorp_vault_client.SystemApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_sys_audit_path**](SystemApi.md#delete_sys_audit_path) | **DELETE** /sys/audit/{path} | Disable the audit device at the given path.
[**delete_sys_auth_path**](SystemApi.md#delete_sys_auth_path) | **DELETE** /sys/auth/{path} | Disable the auth method at the given auth path
[**delete_sys_config_auditing_request_headers_header**](SystemApi.md#delete_sys_config_auditing_request_headers_header) | **DELETE** /sys/config/auditing/request-headers/{header} | Disable auditing of the given request header.
[**delete_sys_config_control_group**](SystemApi.md#delete_sys_config_control_group) | **DELETE** /sys/config/control-group | Configure control group global settings.
[**delete_sys_config_cors**](SystemApi.md#delete_sys_config_cors) | **DELETE** /sys/config/cors | Remove any CORS settings.
[**delete_sys_config_ui_headers_header**](SystemApi.md#delete_sys_config_ui_headers_header) | **DELETE** /sys/config/ui/headers/{header} | Remove a UI header.
[**delete_sys_generate_root**](SystemApi.md#delete_sys_generate_root) | **DELETE** /sys/generate-root | Cancels any in-progress root generation attempt.
[**delete_sys_generate_root_attempt**](SystemApi.md#delete_sys_generate_root_attempt) | **DELETE** /sys/generate-root/attempt | Cancels any in-progress root generation attempt.
[**delete_sys_mfa_method_duo_name**](SystemApi.md#delete_sys_mfa_method_duo_name) | **DELETE** /sys/mfa/method/duo/{name} | Defines or updates a Duo MFA method.
[**delete_sys_mfa_method_okta_name**](SystemApi.md#delete_sys_mfa_method_okta_name) | **DELETE** /sys/mfa/method/okta/{name} | Defines or updates an Okta MFA method.
[**delete_sys_mfa_method_pingid_name**](SystemApi.md#delete_sys_mfa_method_pingid_name) | **DELETE** /sys/mfa/method/pingid/{name} | Defines or updates a PingID MFA method.
[**delete_sys_mfa_method_totp_name**](SystemApi.md#delete_sys_mfa_method_totp_name) | **DELETE** /sys/mfa/method/totp/{name} | Defines or updates a TOTP MFA method.
[**delete_sys_mounts_path**](SystemApi.md#delete_sys_mounts_path) | **DELETE** /sys/mounts/{path} | Disable the mount point specified at the given path.
[**delete_sys_namespaces_path**](SystemApi.md#delete_sys_namespaces_path) | **DELETE** /sys/namespaces/{path} | 
[**delete_sys_plugins_catalog_name**](SystemApi.md#delete_sys_plugins_catalog_name) | **DELETE** /sys/plugins/catalog/{name} | Remove the plugin with the given name.
[**delete_sys_plugins_catalog_type_name**](SystemApi.md#delete_sys_plugins_catalog_type_name) | **DELETE** /sys/plugins/catalog/{type}/{name} | Remove the plugin with the given name.
[**delete_sys_policies_acl_name**](SystemApi.md#delete_sys_policies_acl_name) | **DELETE** /sys/policies/acl/{name} | Delete the ACL policy with the given name.
[**delete_sys_policies_egp_name**](SystemApi.md#delete_sys_policies_egp_name) | **DELETE** /sys/policies/egp/{name} | Read, Modify, or Delete an access control policy.
[**delete_sys_policies_rgp_name**](SystemApi.md#delete_sys_policies_rgp_name) | **DELETE** /sys/policies/rgp/{name} | Read, Modify, or Delete an access control policy.
[**delete_sys_policy_name**](SystemApi.md#delete_sys_policy_name) | **DELETE** /sys/policy/{name} | Delete the policy with the given name.
[**delete_sys_rekey_backup**](SystemApi.md#delete_sys_rekey_backup) | **DELETE** /sys/rekey/backup | Delete the backup copy of PGP-encrypted unseal keys.
[**delete_sys_rekey_init**](SystemApi.md#delete_sys_rekey_init) | **DELETE** /sys/rekey/init | Cancels any in-progress rekey.
[**delete_sys_rekey_recovery_key_backup**](SystemApi.md#delete_sys_rekey_recovery_key_backup) | **DELETE** /sys/rekey/recovery-key-backup | Allows fetching or deleting the backup of the rotated unseal keys.
[**delete_sys_rekey_verify**](SystemApi.md#delete_sys_rekey_verify) | **DELETE** /sys/rekey/verify | Cancel any in-progress rekey verification operation.
[**delete_sys_replication_performance_primary_mount_filter_id**](SystemApi.md#delete_sys_replication_performance_primary_mount_filter_id) | **DELETE** /sys/replication/performance/primary/mount-filter/{id} | 
[**get_sys_audit**](SystemApi.md#get_sys_audit) | **GET** /sys/audit | List the enabled audit devices.
[**get_sys_auth**](SystemApi.md#get_sys_auth) | **GET** /sys/auth | List the currently enabled credential backends.
[**get_sys_auth_path_tune**](SystemApi.md#get_sys_auth_path_tune) | **GET** /sys/auth/{path}/tune | Reads the given auth path&#x27;s configuration.
[**get_sys_config_auditing_request_headers**](SystemApi.md#get_sys_config_auditing_request_headers) | **GET** /sys/config/auditing/request-headers | List the request headers that are configured to be audited.
[**get_sys_config_auditing_request_headers_header**](SystemApi.md#get_sys_config_auditing_request_headers_header) | **GET** /sys/config/auditing/request-headers/{header} | List the information for the given request header.
[**get_sys_config_control_group**](SystemApi.md#get_sys_config_control_group) | **GET** /sys/config/control-group | Configure control group global settings.
[**get_sys_config_cors**](SystemApi.md#get_sys_config_cors) | **GET** /sys/config/cors | Return the current CORS settings.
[**get_sys_config_ui_headers**](SystemApi.md#get_sys_config_ui_headers) | **GET** /sys/config/ui/headers/ | Return a list of configured UI headers.
[**get_sys_config_ui_headers_header**](SystemApi.md#get_sys_config_ui_headers_header) | **GET** /sys/config/ui/headers/{header} | Return the given UI header&#x27;s configuration
[**get_sys_generate_root**](SystemApi.md#get_sys_generate_root) | **GET** /sys/generate-root | Read the configuration and progress of the current root generation attempt.
[**get_sys_generate_root_attempt**](SystemApi.md#get_sys_generate_root_attempt) | **GET** /sys/generate-root/attempt | Read the configuration and progress of the current root generation attempt.
[**get_sys_health**](SystemApi.md#get_sys_health) | **GET** /sys/health | Returns the health status of Vault.
[**get_sys_init**](SystemApi.md#get_sys_init) | **GET** /sys/init | Returns the initialization status of Vault.
[**get_sys_internal_specs_openapi**](SystemApi.md#get_sys_internal_specs_openapi) | **GET** /sys/internal/specs/openapi | Generate an OpenAPI 3 document of all mounted paths.
[**get_sys_internal_ui_mounts**](SystemApi.md#get_sys_internal_ui_mounts) | **GET** /sys/internal/ui/mounts | Lists all enabled and visible auth and secrets mounts.
[**get_sys_internal_ui_mounts_path**](SystemApi.md#get_sys_internal_ui_mounts_path) | **GET** /sys/internal/ui/mounts/{path} | Return information about the given mount.
[**get_sys_key_status**](SystemApi.md#get_sys_key_status) | **GET** /sys/key-status | Provides information about the backend encryption key.
[**get_sys_leader**](SystemApi.md#get_sys_leader) | **GET** /sys/leader | Returns the high availability status and current leader instance of Vault.
[**get_sys_leases_lookup**](SystemApi.md#get_sys_leases_lookup) | **GET** /sys/leases/lookup/ | Returns a list of lease ids.
[**get_sys_leases_lookup_prefix**](SystemApi.md#get_sys_leases_lookup_prefix) | **GET** /sys/leases/lookup/{prefix} | Returns a list of lease ids.
[**get_sys_license**](SystemApi.md#get_sys_license) | **GET** /sys/license | The path responds to the following HTTP methods.      GET /         Returns information on the installed license      POST         Sets the license for the server
[**get_sys_metrics**](SystemApi.md#get_sys_metrics) | **GET** /sys/metrics | Export the metrics aggregated for telemetry purpose.
[**get_sys_mfa_method**](SystemApi.md#get_sys_mfa_method) | **GET** /sys/mfa/method | Lists all the available MFA methods by their name.
[**get_sys_mfa_method_duo_name**](SystemApi.md#get_sys_mfa_method_duo_name) | **GET** /sys/mfa/method/duo/{name} | Defines or updates a Duo MFA method.
[**get_sys_mfa_method_okta_name**](SystemApi.md#get_sys_mfa_method_okta_name) | **GET** /sys/mfa/method/okta/{name} | Defines or updates an Okta MFA method.
[**get_sys_mfa_method_pingid_name**](SystemApi.md#get_sys_mfa_method_pingid_name) | **GET** /sys/mfa/method/pingid/{name} | Defines or updates a PingID MFA method.
[**get_sys_mfa_method_totp_name**](SystemApi.md#get_sys_mfa_method_totp_name) | **GET** /sys/mfa/method/totp/{name} | Defines or updates a TOTP MFA method.
[**get_sys_mfa_method_totp_name_generate**](SystemApi.md#get_sys_mfa_method_totp_name_generate) | **GET** /sys/mfa/method/totp/{name}/generate | Generates a TOTP secret for the given method name on the entity of the   calling token.
[**get_sys_mounts**](SystemApi.md#get_sys_mounts) | **GET** /sys/mounts | List the currently mounted backends.
[**get_sys_mounts_path_tune**](SystemApi.md#get_sys_mounts_path_tune) | **GET** /sys/mounts/{path}/tune | Tune backend configuration parameters for this mount.
[**get_sys_namespaces**](SystemApi.md#get_sys_namespaces) | **GET** /sys/namespaces | 
[**get_sys_namespaces_path**](SystemApi.md#get_sys_namespaces_path) | **GET** /sys/namespaces/{path} | 
[**get_sys_plugins_catalog**](SystemApi.md#get_sys_plugins_catalog) | **GET** /sys/plugins/catalog | Lists all the plugins known to Vault
[**get_sys_plugins_catalog_name**](SystemApi.md#get_sys_plugins_catalog_name) | **GET** /sys/plugins/catalog/{name} | Return the configuration data for the plugin with the given name.
[**get_sys_plugins_catalog_type**](SystemApi.md#get_sys_plugins_catalog_type) | **GET** /sys/plugins/catalog/{type} | List the plugins in the catalog.
[**get_sys_plugins_catalog_type_name**](SystemApi.md#get_sys_plugins_catalog_type_name) | **GET** /sys/plugins/catalog/{type}/{name} | Return the configuration data for the plugin with the given name.
[**get_sys_policies_acl**](SystemApi.md#get_sys_policies_acl) | **GET** /sys/policies/acl | List the configured access control policies.
[**get_sys_policies_acl_name**](SystemApi.md#get_sys_policies_acl_name) | **GET** /sys/policies/acl/{name} | Retrieve information about the named ACL policy.
[**get_sys_policies_egp**](SystemApi.md#get_sys_policies_egp) | **GET** /sys/policies/egp | List the configured access control policies.
[**get_sys_policies_egp_name**](SystemApi.md#get_sys_policies_egp_name) | **GET** /sys/policies/egp/{name} | Read, Modify, or Delete an access control policy.
[**get_sys_policies_rgp**](SystemApi.md#get_sys_policies_rgp) | **GET** /sys/policies/rgp | List the configured access control policies.
[**get_sys_policies_rgp_name**](SystemApi.md#get_sys_policies_rgp_name) | **GET** /sys/policies/rgp/{name} | Read, Modify, or Delete an access control policy.
[**get_sys_policy**](SystemApi.md#get_sys_policy) | **GET** /sys/policy | List the configured access control policies.
[**get_sys_policy_name**](SystemApi.md#get_sys_policy_name) | **GET** /sys/policy/{name} | Retrieve the policy body for the named policy.
[**get_sys_rekey_backup**](SystemApi.md#get_sys_rekey_backup) | **GET** /sys/rekey/backup | Return the backup copy of PGP-encrypted unseal keys.
[**get_sys_rekey_init**](SystemApi.md#get_sys_rekey_init) | **GET** /sys/rekey/init | Reads the configuration and progress of the current rekey attempt.
[**get_sys_rekey_recovery_key_backup**](SystemApi.md#get_sys_rekey_recovery_key_backup) | **GET** /sys/rekey/recovery-key-backup | Allows fetching or deleting the backup of the rotated unseal keys.
[**get_sys_rekey_verify**](SystemApi.md#get_sys_rekey_verify) | **GET** /sys/rekey/verify | Read the configuration and progress of the current rekey verification attempt.
[**get_sys_replication_dr_secondary_license**](SystemApi.md#get_sys_replication_dr_secondary_license) | **GET** /sys/replication/dr/secondary/license | The path responds to the following HTTP methods.      GET /         Returns information on the installed license      POST         Sets the license for the server
[**get_sys_replication_dr_status**](SystemApi.md#get_sys_replication_dr_status) | **GET** /sys/replication/dr/status | 
[**get_sys_replication_performance_primary_mount_filter_id**](SystemApi.md#get_sys_replication_performance_primary_mount_filter_id) | **GET** /sys/replication/performance/primary/mount-filter/{id} | 
[**get_sys_replication_performance_status**](SystemApi.md#get_sys_replication_performance_status) | **GET** /sys/replication/performance/status | 
[**get_sys_replication_status**](SystemApi.md#get_sys_replication_status) | **GET** /sys/replication/status | 
[**get_sys_seal_status**](SystemApi.md#get_sys_seal_status) | **GET** /sys/seal-status | Check the seal status of a Vault.
[**get_sys_wrapping_lookup**](SystemApi.md#get_sys_wrapping_lookup) | **GET** /sys/wrapping/lookup | Look up wrapping properties for the requester&#x27;s token.
[**post_sys_audit_hash_path**](SystemApi.md#post_sys_audit_hash_path) | **POST** /sys/audit-hash/{path} | The hash of the given string via the given audit backend
[**post_sys_audit_path**](SystemApi.md#post_sys_audit_path) | **POST** /sys/audit/{path} | Enable a new audit device at the supplied path.
[**post_sys_auth_path**](SystemApi.md#post_sys_auth_path) | **POST** /sys/auth/{path} | Enables a new auth method.
[**post_sys_auth_path_tune**](SystemApi.md#post_sys_auth_path_tune) | **POST** /sys/auth/{path}/tune | Tune configuration parameters for a given auth path.
[**post_sys_capabilities**](SystemApi.md#post_sys_capabilities) | **POST** /sys/capabilities | Fetches the capabilities of the given token on the given path.
[**post_sys_capabilities_accessor**](SystemApi.md#post_sys_capabilities_accessor) | **POST** /sys/capabilities-accessor | Fetches the capabilities of the token associated with the given token, on the given path.
[**post_sys_capabilities_self**](SystemApi.md#post_sys_capabilities_self) | **POST** /sys/capabilities-self | Fetches the capabilities of the given token on the given path.
[**post_sys_config_auditing_request_headers_header**](SystemApi.md#post_sys_config_auditing_request_headers_header) | **POST** /sys/config/auditing/request-headers/{header} | Enable auditing of a header.
[**post_sys_config_control_group**](SystemApi.md#post_sys_config_control_group) | **POST** /sys/config/control-group | Configure control group global settings.
[**post_sys_config_cors**](SystemApi.md#post_sys_config_cors) | **POST** /sys/config/cors | Configure the CORS settings.
[**post_sys_config_ui_headers_header**](SystemApi.md#post_sys_config_ui_headers_header) | **POST** /sys/config/ui/headers/{header} | Configure the values to be returned for the UI header.
[**post_sys_control_group_authorize**](SystemApi.md#post_sys_control_group_authorize) | **POST** /sys/control-group/authorize | Authorize a control group request
[**post_sys_control_group_request**](SystemApi.md#post_sys_control_group_request) | **POST** /sys/control-group/request | Check the status of a control group request
[**post_sys_generate_root**](SystemApi.md#post_sys_generate_root) | **POST** /sys/generate-root | Initializes a new root generation attempt.
[**post_sys_generate_root_attempt**](SystemApi.md#post_sys_generate_root_attempt) | **POST** /sys/generate-root/attempt | Initializes a new root generation attempt.
[**post_sys_generate_root_update**](SystemApi.md#post_sys_generate_root_update) | **POST** /sys/generate-root/update | Enter a single master key share to progress the root generation attempt.
[**post_sys_init**](SystemApi.md#post_sys_init) | **POST** /sys/init | Initialize a new Vault.
[**post_sys_leases_lookup**](SystemApi.md#post_sys_leases_lookup) | **POST** /sys/leases/lookup | Retrieve lease metadata.
[**post_sys_leases_renew**](SystemApi.md#post_sys_leases_renew) | **POST** /sys/leases/renew | Renews a lease, requesting to extend the lease.
[**post_sys_leases_renew_url_lease_id**](SystemApi.md#post_sys_leases_renew_url_lease_id) | **POST** /sys/leases/renew/{url_lease_id} | Renews a lease, requesting to extend the lease.
[**post_sys_leases_revoke**](SystemApi.md#post_sys_leases_revoke) | **POST** /sys/leases/revoke | Revokes a lease immediately.
[**post_sys_leases_revoke_force_prefix**](SystemApi.md#post_sys_leases_revoke_force_prefix) | **POST** /sys/leases/revoke-force/{prefix} | Revokes all secrets or tokens generated under a given prefix immediately
[**post_sys_leases_revoke_prefix_prefix**](SystemApi.md#post_sys_leases_revoke_prefix_prefix) | **POST** /sys/leases/revoke-prefix/{prefix} | Revokes all secrets (via a lease ID prefix) or tokens (via the tokens&#x27; path property) generated under a given prefix immediately.
[**post_sys_leases_revoke_url_lease_id**](SystemApi.md#post_sys_leases_revoke_url_lease_id) | **POST** /sys/leases/revoke/{url_lease_id} | Revokes a lease immediately.
[**post_sys_leases_tidy**](SystemApi.md#post_sys_leases_tidy) | **POST** /sys/leases/tidy | This endpoint performs cleanup tasks that can be run if certain error conditions have occurred.
[**post_sys_license**](SystemApi.md#post_sys_license) | **POST** /sys/license | The path responds to the following HTTP methods.      GET /         Returns information on the installed license      POST         Sets the license for the server
[**post_sys_mfa_method_duo_name**](SystemApi.md#post_sys_mfa_method_duo_name) | **POST** /sys/mfa/method/duo/{name} | Defines or updates a Duo MFA method.
[**post_sys_mfa_method_okta_name**](SystemApi.md#post_sys_mfa_method_okta_name) | **POST** /sys/mfa/method/okta/{name} | Defines or updates an Okta MFA method.
[**post_sys_mfa_method_pingid_name**](SystemApi.md#post_sys_mfa_method_pingid_name) | **POST** /sys/mfa/method/pingid/{name} | Defines or updates a PingID MFA method.
[**post_sys_mfa_method_totp_name**](SystemApi.md#post_sys_mfa_method_totp_name) | **POST** /sys/mfa/method/totp/{name} | Defines or updates a TOTP MFA method.
[**post_sys_mfa_method_totp_name_admin_destroy**](SystemApi.md#post_sys_mfa_method_totp_name_admin_destroy) | **POST** /sys/mfa/method/totp/{name}/admin-destroy | Deletes the TOTP secret for the given method name on the given entity.
[**post_sys_mfa_method_totp_name_admin_generate**](SystemApi.md#post_sys_mfa_method_totp_name_admin_generate) | **POST** /sys/mfa/method/totp/{name}/admin-generate | Generates a TOTP secret for the given method name on the given entity.
[**post_sys_mounts_path**](SystemApi.md#post_sys_mounts_path) | **POST** /sys/mounts/{path} | Enable a new secrets engine at the given path.
[**post_sys_mounts_path_tune**](SystemApi.md#post_sys_mounts_path_tune) | **POST** /sys/mounts/{path}/tune | Tune backend configuration parameters for this mount.
[**post_sys_namespaces_path**](SystemApi.md#post_sys_namespaces_path) | **POST** /sys/namespaces/{path} | 
[**post_sys_plugins_catalog_name**](SystemApi.md#post_sys_plugins_catalog_name) | **POST** /sys/plugins/catalog/{name} | Register a new plugin, or updates an existing one with the supplied name.
[**post_sys_plugins_catalog_type_name**](SystemApi.md#post_sys_plugins_catalog_type_name) | **POST** /sys/plugins/catalog/{type}/{name} | Register a new plugin, or updates an existing one with the supplied name.
[**post_sys_plugins_reload_backend**](SystemApi.md#post_sys_plugins_reload_backend) | **POST** /sys/plugins/reload/backend | Reload mounted plugin backends.
[**post_sys_policies_acl_name**](SystemApi.md#post_sys_policies_acl_name) | **POST** /sys/policies/acl/{name} | Add a new or update an existing ACL policy.
[**post_sys_policies_egp_name**](SystemApi.md#post_sys_policies_egp_name) | **POST** /sys/policies/egp/{name} | Read, Modify, or Delete an access control policy.
[**post_sys_policies_rgp_name**](SystemApi.md#post_sys_policies_rgp_name) | **POST** /sys/policies/rgp/{name} | Read, Modify, or Delete an access control policy.
[**post_sys_policy_name**](SystemApi.md#post_sys_policy_name) | **POST** /sys/policy/{name} | Add a new or update an existing policy.
[**post_sys_rekey_init**](SystemApi.md#post_sys_rekey_init) | **POST** /sys/rekey/init | Initializes a new rekey attempt.
[**post_sys_rekey_update**](SystemApi.md#post_sys_rekey_update) | **POST** /sys/rekey/update | Enter a single master key share to progress the rekey of the Vault.
[**post_sys_rekey_verify**](SystemApi.md#post_sys_rekey_verify) | **POST** /sys/rekey/verify | Enter a single new key share to progress the rekey verification operation.
[**post_sys_remount**](SystemApi.md#post_sys_remount) | **POST** /sys/remount | Move the mount point of an already-mounted backend.
[**post_sys_renew**](SystemApi.md#post_sys_renew) | **POST** /sys/renew | Renews a lease, requesting to extend the lease.
[**post_sys_renew_url_lease_id**](SystemApi.md#post_sys_renew_url_lease_id) | **POST** /sys/renew/{url_lease_id} | Renews a lease, requesting to extend the lease.
[**post_sys_replication_dr_primary_demote**](SystemApi.md#post_sys_replication_dr_primary_demote) | **POST** /sys/replication/dr/primary/demote | 
[**post_sys_replication_dr_primary_disable**](SystemApi.md#post_sys_replication_dr_primary_disable) | **POST** /sys/replication/dr/primary/disable | 
[**post_sys_replication_dr_primary_enable**](SystemApi.md#post_sys_replication_dr_primary_enable) | **POST** /sys/replication/dr/primary/enable | 
[**post_sys_replication_dr_primary_revoke_secondary**](SystemApi.md#post_sys_replication_dr_primary_revoke_secondary) | **POST** /sys/replication/dr/primary/revoke-secondary | 
[**post_sys_replication_dr_primary_secondary_token**](SystemApi.md#post_sys_replication_dr_primary_secondary_token) | **POST** /sys/replication/dr/primary/secondary-token | 
[**post_sys_replication_dr_secondary_disable**](SystemApi.md#post_sys_replication_dr_secondary_disable) | **POST** /sys/replication/dr/secondary/disable | 
[**post_sys_replication_dr_secondary_enable**](SystemApi.md#post_sys_replication_dr_secondary_enable) | **POST** /sys/replication/dr/secondary/enable | 
[**post_sys_replication_dr_secondary_generate_public_key**](SystemApi.md#post_sys_replication_dr_secondary_generate_public_key) | **POST** /sys/replication/dr/secondary/generate-public-key | 
[**post_sys_replication_dr_secondary_license**](SystemApi.md#post_sys_replication_dr_secondary_license) | **POST** /sys/replication/dr/secondary/license | The path responds to the following HTTP methods.      GET /         Returns information on the installed license      POST         Sets the license for the server
[**post_sys_replication_dr_secondary_operation_token_delete**](SystemApi.md#post_sys_replication_dr_secondary_operation_token_delete) | **POST** /sys/replication/dr/secondary/operation-token/delete | 
[**post_sys_replication_dr_secondary_promote**](SystemApi.md#post_sys_replication_dr_secondary_promote) | **POST** /sys/replication/dr/secondary/promote | 
[**post_sys_replication_dr_secondary_reindex**](SystemApi.md#post_sys_replication_dr_secondary_reindex) | **POST** /sys/replication/dr/secondary/reindex | 
[**post_sys_replication_dr_secondary_update_primary**](SystemApi.md#post_sys_replication_dr_secondary_update_primary) | **POST** /sys/replication/dr/secondary/update-primary | 
[**post_sys_replication_performance_primary_demote**](SystemApi.md#post_sys_replication_performance_primary_demote) | **POST** /sys/replication/performance/primary/demote | 
[**post_sys_replication_performance_primary_disable**](SystemApi.md#post_sys_replication_performance_primary_disable) | **POST** /sys/replication/performance/primary/disable | 
[**post_sys_replication_performance_primary_enable**](SystemApi.md#post_sys_replication_performance_primary_enable) | **POST** /sys/replication/performance/primary/enable | 
[**post_sys_replication_performance_primary_mount_filter_id**](SystemApi.md#post_sys_replication_performance_primary_mount_filter_id) | **POST** /sys/replication/performance/primary/mount-filter/{id} | 
[**post_sys_replication_performance_primary_revoke_secondary**](SystemApi.md#post_sys_replication_performance_primary_revoke_secondary) | **POST** /sys/replication/performance/primary/revoke-secondary | 
[**post_sys_replication_performance_primary_secondary_token**](SystemApi.md#post_sys_replication_performance_primary_secondary_token) | **POST** /sys/replication/performance/primary/secondary-token | 
[**post_sys_replication_performance_secondary_disable**](SystemApi.md#post_sys_replication_performance_secondary_disable) | **POST** /sys/replication/performance/secondary/disable | 
[**post_sys_replication_performance_secondary_enable**](SystemApi.md#post_sys_replication_performance_secondary_enable) | **POST** /sys/replication/performance/secondary/enable | 
[**post_sys_replication_performance_secondary_generate_public_key**](SystemApi.md#post_sys_replication_performance_secondary_generate_public_key) | **POST** /sys/replication/performance/secondary/generate-public-key | 
[**post_sys_replication_performance_secondary_promote**](SystemApi.md#post_sys_replication_performance_secondary_promote) | **POST** /sys/replication/performance/secondary/promote | 
[**post_sys_replication_performance_secondary_update_primary**](SystemApi.md#post_sys_replication_performance_secondary_update_primary) | **POST** /sys/replication/performance/secondary/update-primary | 
[**post_sys_replication_primary_demote**](SystemApi.md#post_sys_replication_primary_demote) | **POST** /sys/replication/primary/demote | 
[**post_sys_replication_primary_disable**](SystemApi.md#post_sys_replication_primary_disable) | **POST** /sys/replication/primary/disable | 
[**post_sys_replication_primary_enable**](SystemApi.md#post_sys_replication_primary_enable) | **POST** /sys/replication/primary/enable | 
[**post_sys_replication_primary_revoke_secondary**](SystemApi.md#post_sys_replication_primary_revoke_secondary) | **POST** /sys/replication/primary/revoke-secondary | 
[**post_sys_replication_primary_secondary_token**](SystemApi.md#post_sys_replication_primary_secondary_token) | **POST** /sys/replication/primary/secondary-token | 
[**post_sys_replication_recover**](SystemApi.md#post_sys_replication_recover) | **POST** /sys/replication/recover | 
[**post_sys_replication_reindex**](SystemApi.md#post_sys_replication_reindex) | **POST** /sys/replication/reindex | 
[**post_sys_replication_secondary_disable**](SystemApi.md#post_sys_replication_secondary_disable) | **POST** /sys/replication/secondary/disable | 
[**post_sys_replication_secondary_enable**](SystemApi.md#post_sys_replication_secondary_enable) | **POST** /sys/replication/secondary/enable | 
[**post_sys_replication_secondary_promote**](SystemApi.md#post_sys_replication_secondary_promote) | **POST** /sys/replication/secondary/promote | 
[**post_sys_replication_secondary_update_primary**](SystemApi.md#post_sys_replication_secondary_update_primary) | **POST** /sys/replication/secondary/update-primary | 
[**post_sys_revoke**](SystemApi.md#post_sys_revoke) | **POST** /sys/revoke | Revokes a lease immediately.
[**post_sys_revoke_force_prefix**](SystemApi.md#post_sys_revoke_force_prefix) | **POST** /sys/revoke-force/{prefix} | Revokes all secrets or tokens generated under a given prefix immediately
[**post_sys_revoke_prefix_prefix**](SystemApi.md#post_sys_revoke_prefix_prefix) | **POST** /sys/revoke-prefix/{prefix} | Revokes all secrets (via a lease ID prefix) or tokens (via the tokens&#x27; path property) generated under a given prefix immediately.
[**post_sys_revoke_url_lease_id**](SystemApi.md#post_sys_revoke_url_lease_id) | **POST** /sys/revoke/{url_lease_id} | Revokes a lease immediately.
[**post_sys_rotate**](SystemApi.md#post_sys_rotate) | **POST** /sys/rotate | Rotates the backend encryption key used to persist data.
[**post_sys_seal**](SystemApi.md#post_sys_seal) | **POST** /sys/seal | Seal the Vault.
[**post_sys_step_down**](SystemApi.md#post_sys_step_down) | **POST** /sys/step-down | Cause the node to give up active status.
[**post_sys_tools_hash**](SystemApi.md#post_sys_tools_hash) | **POST** /sys/tools/hash | Generate a hash sum for input data
[**post_sys_tools_hash_urlalgorithm**](SystemApi.md#post_sys_tools_hash_urlalgorithm) | **POST** /sys/tools/hash/{urlalgorithm} | Generate a hash sum for input data
[**post_sys_tools_random**](SystemApi.md#post_sys_tools_random) | **POST** /sys/tools/random | Generate random bytes
[**post_sys_tools_random_urlbytes**](SystemApi.md#post_sys_tools_random_urlbytes) | **POST** /sys/tools/random/{urlbytes} | Generate random bytes
[**post_sys_unseal**](SystemApi.md#post_sys_unseal) | **POST** /sys/unseal | Unseal the Vault.
[**post_sys_wrapping_lookup**](SystemApi.md#post_sys_wrapping_lookup) | **POST** /sys/wrapping/lookup | Look up wrapping properties for the given token.
[**post_sys_wrapping_rewrap**](SystemApi.md#post_sys_wrapping_rewrap) | **POST** /sys/wrapping/rewrap | Rotates a response-wrapped token.
[**post_sys_wrapping_unwrap**](SystemApi.md#post_sys_wrapping_unwrap) | **POST** /sys/wrapping/unwrap | Unwraps a response-wrapped token.
[**post_sys_wrapping_wrap**](SystemApi.md#post_sys_wrapping_wrap) | **POST** /sys/wrapping/wrap | Response-wraps an arbitrary JSON object.

# **delete_sys_audit_path**
> delete_sys_audit_path(path)

Disable the audit device at the given path.

### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.SystemApi()
path = 'path_example' # str | The name of the backend. Cannot be delimited. Example: \"mysql\"

try:
    # Disable the audit device at the given path.
    api_instance.delete_sys_audit_path(path)
except ApiException as e:
    print("Exception when calling SystemApi->delete_sys_audit_path: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| The name of the backend. Cannot be delimited. Example: \&quot;mysql\&quot; | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_sys_auth_path**
> delete_sys_auth_path(path)

Disable the auth method at the given auth path

### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.SystemApi()
path = 'path_example' # str | The path to mount to. Cannot be delimited. Example: \"user\"

try:
    # Disable the auth method at the given auth path
    api_instance.delete_sys_auth_path(path)
except ApiException as e:
    print("Exception when calling SystemApi->delete_sys_auth_path: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| The path to mount to. Cannot be delimited. Example: \&quot;user\&quot; | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_sys_config_auditing_request_headers_header**
> delete_sys_config_auditing_request_headers_header(header)

Disable auditing of the given request header.

### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.SystemApi()
header = 'header_example' # str | 

try:
    # Disable auditing of the given request header.
    api_instance.delete_sys_config_auditing_request_headers_header(header)
except ApiException as e:
    print("Exception when calling SystemApi->delete_sys_config_auditing_request_headers_header: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **header** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_sys_config_control_group**
> delete_sys_config_control_group()

Configure control group global settings.

### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.SystemApi()

try:
    # Configure control group global settings.
    api_instance.delete_sys_config_control_group()
except ApiException as e:
    print("Exception when calling SystemApi->delete_sys_config_control_group: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_sys_config_cors**
> delete_sys_config_cors()

Remove any CORS settings.

### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.SystemApi()

try:
    # Remove any CORS settings.
    api_instance.delete_sys_config_cors()
except ApiException as e:
    print("Exception when calling SystemApi->delete_sys_config_cors: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_sys_config_ui_headers_header**
> delete_sys_config_ui_headers_header(header)

Remove a UI header.

### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.SystemApi()
header = 'header_example' # str | The name of the header.

try:
    # Remove a UI header.
    api_instance.delete_sys_config_ui_headers_header(header)
except ApiException as e:
    print("Exception when calling SystemApi->delete_sys_config_ui_headers_header: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **header** | **str**| The name of the header. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_sys_generate_root**
> delete_sys_generate_root()

Cancels any in-progress root generation attempt.

### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.SystemApi()

try:
    # Cancels any in-progress root generation attempt.
    api_instance.delete_sys_generate_root()
except ApiException as e:
    print("Exception when calling SystemApi->delete_sys_generate_root: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_sys_generate_root_attempt**
> delete_sys_generate_root_attempt()

Cancels any in-progress root generation attempt.

### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.SystemApi()

try:
    # Cancels any in-progress root generation attempt.
    api_instance.delete_sys_generate_root_attempt()
except ApiException as e:
    print("Exception when calling SystemApi->delete_sys_generate_root_attempt: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_sys_mfa_method_duo_name**
> delete_sys_mfa_method_duo_name(name)

Defines or updates a Duo MFA method.

### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.SystemApi()
name = 'name_example' # str | Name of the MFA method.

try:
    # Defines or updates a Duo MFA method.
    api_instance.delete_sys_mfa_method_duo_name(name)
except ApiException as e:
    print("Exception when calling SystemApi->delete_sys_mfa_method_duo_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the MFA method. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_sys_mfa_method_okta_name**
> delete_sys_mfa_method_okta_name(name)

Defines or updates an Okta MFA method.

### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.SystemApi()
name = 'name_example' # str | Name of the MFA method.

try:
    # Defines or updates an Okta MFA method.
    api_instance.delete_sys_mfa_method_okta_name(name)
except ApiException as e:
    print("Exception when calling SystemApi->delete_sys_mfa_method_okta_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the MFA method. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_sys_mfa_method_pingid_name**
> delete_sys_mfa_method_pingid_name(name)

Defines or updates a PingID MFA method.

### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.SystemApi()
name = 'name_example' # str | Name of the MFA method.

try:
    # Defines or updates a PingID MFA method.
    api_instance.delete_sys_mfa_method_pingid_name(name)
except ApiException as e:
    print("Exception when calling SystemApi->delete_sys_mfa_method_pingid_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the MFA method. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_sys_mfa_method_totp_name**
> delete_sys_mfa_method_totp_name(name)

Defines or updates a TOTP MFA method.

### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.SystemApi()
name = 'name_example' # str | Name of the MFA method.

try:
    # Defines or updates a TOTP MFA method.
    api_instance.delete_sys_mfa_method_totp_name(name)
except ApiException as e:
    print("Exception when calling SystemApi->delete_sys_mfa_method_totp_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the MFA method. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_sys_mounts_path**
> delete_sys_mounts_path(path)

Disable the mount point specified at the given path.

### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.SystemApi()
path = 'path_example' # str | The path to mount to. Example: \"aws/east\"

try:
    # Disable the mount point specified at the given path.
    api_instance.delete_sys_mounts_path(path)
except ApiException as e:
    print("Exception when calling SystemApi->delete_sys_mounts_path: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| The path to mount to. Example: \&quot;aws/east\&quot; | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_sys_namespaces_path**
> delete_sys_namespaces_path(path)



### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.SystemApi()
path = 'path_example' # str | Path of the namespace.

try:
    api_instance.delete_sys_namespaces_path(path)
except ApiException as e:
    print("Exception when calling SystemApi->delete_sys_namespaces_path: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| Path of the namespace. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_sys_plugins_catalog_name**
> delete_sys_plugins_catalog_name(name)

Remove the plugin with the given name.

### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.SystemApi()
name = 'name_example' # str | The name of the plugin

try:
    # Remove the plugin with the given name.
    api_instance.delete_sys_plugins_catalog_name(name)
except ApiException as e:
    print("Exception when calling SystemApi->delete_sys_plugins_catalog_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the plugin | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_sys_plugins_catalog_type_name**
> delete_sys_plugins_catalog_type_name(name, type)

Remove the plugin with the given name.

### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.SystemApi()
name = 'name_example' # str | The name of the plugin
type = 'type_example' # str | The type of the plugin, may be auth, secret, or database

try:
    # Remove the plugin with the given name.
    api_instance.delete_sys_plugins_catalog_type_name(name, type)
except ApiException as e:
    print("Exception when calling SystemApi->delete_sys_plugins_catalog_type_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the plugin | 
 **type** | **str**| The type of the plugin, may be auth, secret, or database | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_sys_policies_acl_name**
> delete_sys_policies_acl_name(name)

Delete the ACL policy with the given name.

### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.SystemApi()
name = 'name_example' # str | The name of the policy. Example: \"ops\"

try:
    # Delete the ACL policy with the given name.
    api_instance.delete_sys_policies_acl_name(name)
except ApiException as e:
    print("Exception when calling SystemApi->delete_sys_policies_acl_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the policy. Example: \&quot;ops\&quot; | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_sys_policies_egp_name**
> delete_sys_policies_egp_name(name)

Read, Modify, or Delete an access control policy.

### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.SystemApi()
name = 'name_example' # str | The name of the policy. Example: \"ops\"

try:
    # Read, Modify, or Delete an access control policy.
    api_instance.delete_sys_policies_egp_name(name)
except ApiException as e:
    print("Exception when calling SystemApi->delete_sys_policies_egp_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the policy. Example: \&quot;ops\&quot; | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_sys_policies_rgp_name**
> delete_sys_policies_rgp_name(name)

Read, Modify, or Delete an access control policy.

### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.SystemApi()
name = 'name_example' # str | The name of the policy. Example: \"ops\"

try:
    # Read, Modify, or Delete an access control policy.
    api_instance.delete_sys_policies_rgp_name(name)
except ApiException as e:
    print("Exception when calling SystemApi->delete_sys_policies_rgp_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the policy. Example: \&quot;ops\&quot; | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_sys_policy_name**
> delete_sys_policy_name(name)

Delete the policy with the given name.

### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.SystemApi()
name = 'name_example' # str | The name of the policy. Example: \"ops\"

try:
    # Delete the policy with the given name.
    api_instance.delete_sys_policy_name(name)
except ApiException as e:
    print("Exception when calling SystemApi->delete_sys_policy_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the policy. Example: \&quot;ops\&quot; | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_sys_rekey_backup**
> delete_sys_rekey_backup()

Delete the backup copy of PGP-encrypted unseal keys.

### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.SystemApi()

try:
    # Delete the backup copy of PGP-encrypted unseal keys.
    api_instance.delete_sys_rekey_backup()
except ApiException as e:
    print("Exception when calling SystemApi->delete_sys_rekey_backup: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_sys_rekey_init**
> delete_sys_rekey_init()

Cancels any in-progress rekey.

This clears the rekey settings as well as any progress made. This must be called to change the parameters of the rekey. Note: verification is still a part of a rekey. If rekeying is canceled during the verification flow, the current unseal keys remain valid.

### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.SystemApi()

try:
    # Cancels any in-progress rekey.
    api_instance.delete_sys_rekey_init()
except ApiException as e:
    print("Exception when calling SystemApi->delete_sys_rekey_init: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_sys_rekey_recovery_key_backup**
> delete_sys_rekey_recovery_key_backup()

Allows fetching or deleting the backup of the rotated unseal keys.

### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.SystemApi()

try:
    # Allows fetching or deleting the backup of the rotated unseal keys.
    api_instance.delete_sys_rekey_recovery_key_backup()
except ApiException as e:
    print("Exception when calling SystemApi->delete_sys_rekey_recovery_key_backup: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_sys_rekey_verify**
> delete_sys_rekey_verify()

Cancel any in-progress rekey verification operation.

This clears any progress made and resets the nonce. Unlike a `DELETE` against `sys/rekey/init`, this only resets the current verification operation, not the entire rekey atttempt.

### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.SystemApi()

try:
    # Cancel any in-progress rekey verification operation.
    api_instance.delete_sys_rekey_verify()
except ApiException as e:
    print("Exception when calling SystemApi->delete_sys_rekey_verify: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_sys_replication_performance_primary_mount_filter_id**
> delete_sys_replication_performance_primary_mount_filter_id(id)



### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.SystemApi()
id = 'id_example' # str | The opaque identifier used to identify the secondary.

try:
    api_instance.delete_sys_replication_performance_primary_mount_filter_id(id)
except ApiException as e:
    print("Exception when calling SystemApi->delete_sys_replication_performance_primary_mount_filter_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The opaque identifier used to identify the secondary. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sys_audit**
> get_sys_audit()

List the enabled audit devices.

### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.SystemApi()

try:
    # List the enabled audit devices.
    api_instance.get_sys_audit()
except ApiException as e:
    print("Exception when calling SystemApi->get_sys_audit: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sys_auth**
> get_sys_auth()

List the currently enabled credential backends.

### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.SystemApi()

try:
    # List the currently enabled credential backends.
    api_instance.get_sys_auth()
except ApiException as e:
    print("Exception when calling SystemApi->get_sys_auth: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sys_auth_path_tune**
> get_sys_auth_path_tune(path)

Reads the given auth path's configuration.

This endpoint requires sudo capability on the final path, but the same functionality can be achieved without sudo via `sys/mounts/auth/[auth-path]/tune`.

### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.SystemApi()
path = 'path_example' # str | Tune the configuration parameters for an auth path.

try:
    # Reads the given auth path's configuration.
    api_instance.get_sys_auth_path_tune(path)
except ApiException as e:
    print("Exception when calling SystemApi->get_sys_auth_path_tune: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| Tune the configuration parameters for an auth path. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sys_config_auditing_request_headers**
> get_sys_config_auditing_request_headers()

List the request headers that are configured to be audited.

### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.SystemApi()

try:
    # List the request headers that are configured to be audited.
    api_instance.get_sys_config_auditing_request_headers()
except ApiException as e:
    print("Exception when calling SystemApi->get_sys_config_auditing_request_headers: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sys_config_auditing_request_headers_header**
> get_sys_config_auditing_request_headers_header(header)

List the information for the given request header.

### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.SystemApi()
header = 'header_example' # str | 

try:
    # List the information for the given request header.
    api_instance.get_sys_config_auditing_request_headers_header(header)
except ApiException as e:
    print("Exception when calling SystemApi->get_sys_config_auditing_request_headers_header: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **header** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sys_config_control_group**
> get_sys_config_control_group()

Configure control group global settings.

### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.SystemApi()

try:
    # Configure control group global settings.
    api_instance.get_sys_config_control_group()
except ApiException as e:
    print("Exception when calling SystemApi->get_sys_config_control_group: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sys_config_cors**
> get_sys_config_cors()

Return the current CORS settings.

### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.SystemApi()

try:
    # Return the current CORS settings.
    api_instance.get_sys_config_cors()
except ApiException as e:
    print("Exception when calling SystemApi->get_sys_config_cors: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sys_config_ui_headers**
> get_sys_config_ui_headers(list=list)

Return a list of configured UI headers.

### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.SystemApi()
list = 'list_example' # str | Return a list if `true` (optional)

try:
    # Return a list of configured UI headers.
    api_instance.get_sys_config_ui_headers(list=list)
except ApiException as e:
    print("Exception when calling SystemApi->get_sys_config_ui_headers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list** | **str**| Return a list if &#x60;true&#x60; | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sys_config_ui_headers_header**
> get_sys_config_ui_headers_header(header)

Return the given UI header's configuration

### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.SystemApi()
header = 'header_example' # str | The name of the header.

try:
    # Return the given UI header's configuration
    api_instance.get_sys_config_ui_headers_header(header)
except ApiException as e:
    print("Exception when calling SystemApi->get_sys_config_ui_headers_header: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **header** | **str**| The name of the header. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sys_generate_root**
> get_sys_generate_root()

Read the configuration and progress of the current root generation attempt.

### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.SystemApi()

try:
    # Read the configuration and progress of the current root generation attempt.
    api_instance.get_sys_generate_root()
except ApiException as e:
    print("Exception when calling SystemApi->get_sys_generate_root: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sys_generate_root_attempt**
> get_sys_generate_root_attempt()

Read the configuration and progress of the current root generation attempt.

### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.SystemApi()

try:
    # Read the configuration and progress of the current root generation attempt.
    api_instance.get_sys_generate_root_attempt()
except ApiException as e:
    print("Exception when calling SystemApi->get_sys_generate_root_attempt: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sys_health**
> get_sys_health()

Returns the health status of Vault.

### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.SystemApi()

try:
    # Returns the health status of Vault.
    api_instance.get_sys_health()
except ApiException as e:
    print("Exception when calling SystemApi->get_sys_health: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sys_init**
> get_sys_init()

Returns the initialization status of Vault.

### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.SystemApi()

try:
    # Returns the initialization status of Vault.
    api_instance.get_sys_init()
except ApiException as e:
    print("Exception when calling SystemApi->get_sys_init: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sys_internal_specs_openapi**
> get_sys_internal_specs_openapi()

Generate an OpenAPI 3 document of all mounted paths.

### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.SystemApi()

try:
    # Generate an OpenAPI 3 document of all mounted paths.
    api_instance.get_sys_internal_specs_openapi()
except ApiException as e:
    print("Exception when calling SystemApi->get_sys_internal_specs_openapi: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sys_internal_ui_mounts**
> get_sys_internal_ui_mounts()

Lists all enabled and visible auth and secrets mounts.

### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.SystemApi()

try:
    # Lists all enabled and visible auth and secrets mounts.
    api_instance.get_sys_internal_ui_mounts()
except ApiException as e:
    print("Exception when calling SystemApi->get_sys_internal_ui_mounts: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sys_internal_ui_mounts_path**
> get_sys_internal_ui_mounts_path(path)

Return information about the given mount.

### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.SystemApi()
path = 'path_example' # str | The path of the mount.

try:
    # Return information about the given mount.
    api_instance.get_sys_internal_ui_mounts_path(path)
except ApiException as e:
    print("Exception when calling SystemApi->get_sys_internal_ui_mounts_path: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| The path of the mount. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sys_key_status**
> get_sys_key_status()

Provides information about the backend encryption key.

### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.SystemApi()

try:
    # Provides information about the backend encryption key.
    api_instance.get_sys_key_status()
except ApiException as e:
    print("Exception when calling SystemApi->get_sys_key_status: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sys_leader**
> get_sys_leader()

Returns the high availability status and current leader instance of Vault.

### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.SystemApi()

try:
    # Returns the high availability status and current leader instance of Vault.
    api_instance.get_sys_leader()
except ApiException as e:
    print("Exception when calling SystemApi->get_sys_leader: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sys_leases_lookup**
> get_sys_leases_lookup(list=list)

Returns a list of lease ids.

### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.SystemApi()
list = 'list_example' # str | Return a list if `true` (optional)

try:
    # Returns a list of lease ids.
    api_instance.get_sys_leases_lookup(list=list)
except ApiException as e:
    print("Exception when calling SystemApi->get_sys_leases_lookup: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list** | **str**| Return a list if &#x60;true&#x60; | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sys_leases_lookup_prefix**
> get_sys_leases_lookup_prefix(prefix, list=list)

Returns a list of lease ids.

### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.SystemApi()
prefix = 'prefix_example' # str | The path to list leases under. Example: \"aws/creds/deploy\"
list = 'list_example' # str | Return a list if `true` (optional)

try:
    # Returns a list of lease ids.
    api_instance.get_sys_leases_lookup_prefix(prefix, list=list)
except ApiException as e:
    print("Exception when calling SystemApi->get_sys_leases_lookup_prefix: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **prefix** | **str**| The path to list leases under. Example: \&quot;aws/creds/deploy\&quot; | 
 **list** | **str**| Return a list if &#x60;true&#x60; | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sys_license**
> get_sys_license()

The path responds to the following HTTP methods.      GET /         Returns information on the installed license      POST         Sets the license for the server

### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.SystemApi()

try:
    # The path responds to the following HTTP methods.      GET /         Returns information on the installed license      POST         Sets the license for the server
    api_instance.get_sys_license()
except ApiException as e:
    print("Exception when calling SystemApi->get_sys_license: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sys_metrics**
> get_sys_metrics(format=format)

Export the metrics aggregated for telemetry purpose.

### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.SystemApi()
format = 'format_example' # str | Format to export metrics into. Currently accepts only \"prometheus\". (optional)

try:
    # Export the metrics aggregated for telemetry purpose.
    api_instance.get_sys_metrics(format=format)
except ApiException as e:
    print("Exception when calling SystemApi->get_sys_metrics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**| Format to export metrics into. Currently accepts only \&quot;prometheus\&quot;. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sys_mfa_method**
> get_sys_mfa_method(list=list)

Lists all the available MFA methods by their name.

### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.SystemApi()
list = 'list_example' # str | Return a list if `true` (optional)

try:
    # Lists all the available MFA methods by their name.
    api_instance.get_sys_mfa_method(list=list)
except ApiException as e:
    print("Exception when calling SystemApi->get_sys_mfa_method: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list** | **str**| Return a list if &#x60;true&#x60; | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sys_mfa_method_duo_name**
> get_sys_mfa_method_duo_name(name)

Defines or updates a Duo MFA method.

### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.SystemApi()
name = 'name_example' # str | Name of the MFA method.

try:
    # Defines or updates a Duo MFA method.
    api_instance.get_sys_mfa_method_duo_name(name)
except ApiException as e:
    print("Exception when calling SystemApi->get_sys_mfa_method_duo_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the MFA method. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sys_mfa_method_okta_name**
> get_sys_mfa_method_okta_name(name)

Defines or updates an Okta MFA method.

### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.SystemApi()
name = 'name_example' # str | Name of the MFA method.

try:
    # Defines or updates an Okta MFA method.
    api_instance.get_sys_mfa_method_okta_name(name)
except ApiException as e:
    print("Exception when calling SystemApi->get_sys_mfa_method_okta_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the MFA method. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sys_mfa_method_pingid_name**
> get_sys_mfa_method_pingid_name(name)

Defines or updates a PingID MFA method.

### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.SystemApi()
name = 'name_example' # str | Name of the MFA method.

try:
    # Defines or updates a PingID MFA method.
    api_instance.get_sys_mfa_method_pingid_name(name)
except ApiException as e:
    print("Exception when calling SystemApi->get_sys_mfa_method_pingid_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the MFA method. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sys_mfa_method_totp_name**
> get_sys_mfa_method_totp_name(name)

Defines or updates a TOTP MFA method.

### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.SystemApi()
name = 'name_example' # str | Name of the MFA method.

try:
    # Defines or updates a TOTP MFA method.
    api_instance.get_sys_mfa_method_totp_name(name)
except ApiException as e:
    print("Exception when calling SystemApi->get_sys_mfa_method_totp_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the MFA method. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sys_mfa_method_totp_name_generate**
> get_sys_mfa_method_totp_name_generate(name)

Generates a TOTP secret for the given method name on the entity of the   calling token.

### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.SystemApi()
name = 'name_example' # str | Name of the MFA method.

try:
    # Generates a TOTP secret for the given method name on the entity of the   calling token.
    api_instance.get_sys_mfa_method_totp_name_generate(name)
except ApiException as e:
    print("Exception when calling SystemApi->get_sys_mfa_method_totp_name_generate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the MFA method. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sys_mounts**
> get_sys_mounts()

List the currently mounted backends.

### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.SystemApi()

try:
    # List the currently mounted backends.
    api_instance.get_sys_mounts()
except ApiException as e:
    print("Exception when calling SystemApi->get_sys_mounts: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sys_mounts_path_tune**
> get_sys_mounts_path_tune(path)

Tune backend configuration parameters for this mount.

### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.SystemApi()
path = 'path_example' # str | The path to mount to. Example: \"aws/east\"

try:
    # Tune backend configuration parameters for this mount.
    api_instance.get_sys_mounts_path_tune(path)
except ApiException as e:
    print("Exception when calling SystemApi->get_sys_mounts_path_tune: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| The path to mount to. Example: \&quot;aws/east\&quot; | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sys_namespaces**
> get_sys_namespaces(list=list)



### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.SystemApi()
list = 'list_example' # str | Return a list if `true` (optional)

try:
    api_instance.get_sys_namespaces(list=list)
except ApiException as e:
    print("Exception when calling SystemApi->get_sys_namespaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list** | **str**| Return a list if &#x60;true&#x60; | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sys_namespaces_path**
> get_sys_namespaces_path(path)



### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.SystemApi()
path = 'path_example' # str | Path of the namespace.

try:
    api_instance.get_sys_namespaces_path(path)
except ApiException as e:
    print("Exception when calling SystemApi->get_sys_namespaces_path: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| Path of the namespace. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sys_plugins_catalog**
> get_sys_plugins_catalog()

Lists all the plugins known to Vault

### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.SystemApi()

try:
    # Lists all the plugins known to Vault
    api_instance.get_sys_plugins_catalog()
except ApiException as e:
    print("Exception when calling SystemApi->get_sys_plugins_catalog: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sys_plugins_catalog_name**
> get_sys_plugins_catalog_name(name)

Return the configuration data for the plugin with the given name.

### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.SystemApi()
name = 'name_example' # str | The name of the plugin

try:
    # Return the configuration data for the plugin with the given name.
    api_instance.get_sys_plugins_catalog_name(name)
except ApiException as e:
    print("Exception when calling SystemApi->get_sys_plugins_catalog_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the plugin | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sys_plugins_catalog_type**
> get_sys_plugins_catalog_type(type, list=list)

List the plugins in the catalog.

### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.SystemApi()
type = 'type_example' # str | The type of the plugin, may be auth, secret, or database
list = 'list_example' # str | Return a list if `true` (optional)

try:
    # List the plugins in the catalog.
    api_instance.get_sys_plugins_catalog_type(type, list=list)
except ApiException as e:
    print("Exception when calling SystemApi->get_sys_plugins_catalog_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| The type of the plugin, may be auth, secret, or database | 
 **list** | **str**| Return a list if &#x60;true&#x60; | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sys_plugins_catalog_type_name**
> get_sys_plugins_catalog_type_name(name, type)

Return the configuration data for the plugin with the given name.

### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.SystemApi()
name = 'name_example' # str | The name of the plugin
type = 'type_example' # str | The type of the plugin, may be auth, secret, or database

try:
    # Return the configuration data for the plugin with the given name.
    api_instance.get_sys_plugins_catalog_type_name(name, type)
except ApiException as e:
    print("Exception when calling SystemApi->get_sys_plugins_catalog_type_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the plugin | 
 **type** | **str**| The type of the plugin, may be auth, secret, or database | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sys_policies_acl**
> get_sys_policies_acl(list=list)

List the configured access control policies.

### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.SystemApi()
list = 'list_example' # str | Return a list if `true` (optional)

try:
    # List the configured access control policies.
    api_instance.get_sys_policies_acl(list=list)
except ApiException as e:
    print("Exception when calling SystemApi->get_sys_policies_acl: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list** | **str**| Return a list if &#x60;true&#x60; | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sys_policies_acl_name**
> get_sys_policies_acl_name(name)

Retrieve information about the named ACL policy.

### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.SystemApi()
name = 'name_example' # str | The name of the policy. Example: \"ops\"

try:
    # Retrieve information about the named ACL policy.
    api_instance.get_sys_policies_acl_name(name)
except ApiException as e:
    print("Exception when calling SystemApi->get_sys_policies_acl_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the policy. Example: \&quot;ops\&quot; | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sys_policies_egp**
> get_sys_policies_egp(list=list)

List the configured access control policies.

### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.SystemApi()
list = 'list_example' # str | Return a list if `true` (optional)

try:
    # List the configured access control policies.
    api_instance.get_sys_policies_egp(list=list)
except ApiException as e:
    print("Exception when calling SystemApi->get_sys_policies_egp: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list** | **str**| Return a list if &#x60;true&#x60; | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sys_policies_egp_name**
> get_sys_policies_egp_name(name)

Read, Modify, or Delete an access control policy.

### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.SystemApi()
name = 'name_example' # str | The name of the policy. Example: \"ops\"

try:
    # Read, Modify, or Delete an access control policy.
    api_instance.get_sys_policies_egp_name(name)
except ApiException as e:
    print("Exception when calling SystemApi->get_sys_policies_egp_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the policy. Example: \&quot;ops\&quot; | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sys_policies_rgp**
> get_sys_policies_rgp(list=list)

List the configured access control policies.

### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.SystemApi()
list = 'list_example' # str | Return a list if `true` (optional)

try:
    # List the configured access control policies.
    api_instance.get_sys_policies_rgp(list=list)
except ApiException as e:
    print("Exception when calling SystemApi->get_sys_policies_rgp: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list** | **str**| Return a list if &#x60;true&#x60; | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sys_policies_rgp_name**
> get_sys_policies_rgp_name(name)

Read, Modify, or Delete an access control policy.

### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.SystemApi()
name = 'name_example' # str | The name of the policy. Example: \"ops\"

try:
    # Read, Modify, or Delete an access control policy.
    api_instance.get_sys_policies_rgp_name(name)
except ApiException as e:
    print("Exception when calling SystemApi->get_sys_policies_rgp_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the policy. Example: \&quot;ops\&quot; | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sys_policy**
> get_sys_policy(list=list)

List the configured access control policies.

### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.SystemApi()
list = 'list_example' # str | Return a list if `true` (optional)

try:
    # List the configured access control policies.
    api_instance.get_sys_policy(list=list)
except ApiException as e:
    print("Exception when calling SystemApi->get_sys_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list** | **str**| Return a list if &#x60;true&#x60; | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sys_policy_name**
> get_sys_policy_name(name)

Retrieve the policy body for the named policy.

### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.SystemApi()
name = 'name_example' # str | The name of the policy. Example: \"ops\"

try:
    # Retrieve the policy body for the named policy.
    api_instance.get_sys_policy_name(name)
except ApiException as e:
    print("Exception when calling SystemApi->get_sys_policy_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the policy. Example: \&quot;ops\&quot; | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sys_rekey_backup**
> get_sys_rekey_backup()

Return the backup copy of PGP-encrypted unseal keys.

### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.SystemApi()

try:
    # Return the backup copy of PGP-encrypted unseal keys.
    api_instance.get_sys_rekey_backup()
except ApiException as e:
    print("Exception when calling SystemApi->get_sys_rekey_backup: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sys_rekey_init**
> get_sys_rekey_init()

Reads the configuration and progress of the current rekey attempt.

### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.SystemApi()

try:
    # Reads the configuration and progress of the current rekey attempt.
    api_instance.get_sys_rekey_init()
except ApiException as e:
    print("Exception when calling SystemApi->get_sys_rekey_init: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sys_rekey_recovery_key_backup**
> get_sys_rekey_recovery_key_backup()

Allows fetching or deleting the backup of the rotated unseal keys.

### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.SystemApi()

try:
    # Allows fetching or deleting the backup of the rotated unseal keys.
    api_instance.get_sys_rekey_recovery_key_backup()
except ApiException as e:
    print("Exception when calling SystemApi->get_sys_rekey_recovery_key_backup: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sys_rekey_verify**
> get_sys_rekey_verify()

Read the configuration and progress of the current rekey verification attempt.

### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.SystemApi()

try:
    # Read the configuration and progress of the current rekey verification attempt.
    api_instance.get_sys_rekey_verify()
except ApiException as e:
    print("Exception when calling SystemApi->get_sys_rekey_verify: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sys_replication_dr_secondary_license**
> get_sys_replication_dr_secondary_license()

The path responds to the following HTTP methods.      GET /         Returns information on the installed license      POST         Sets the license for the server

### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.SystemApi()

try:
    # The path responds to the following HTTP methods.      GET /         Returns information on the installed license      POST         Sets the license for the server
    api_instance.get_sys_replication_dr_secondary_license()
except ApiException as e:
    print("Exception when calling SystemApi->get_sys_replication_dr_secondary_license: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sys_replication_dr_status**
> get_sys_replication_dr_status()



### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.SystemApi()

try:
    api_instance.get_sys_replication_dr_status()
except ApiException as e:
    print("Exception when calling SystemApi->get_sys_replication_dr_status: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sys_replication_performance_primary_mount_filter_id**
> get_sys_replication_performance_primary_mount_filter_id(id)



### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.SystemApi()
id = 'id_example' # str | The opaque identifier used to identify the secondary.

try:
    api_instance.get_sys_replication_performance_primary_mount_filter_id(id)
except ApiException as e:
    print("Exception when calling SystemApi->get_sys_replication_performance_primary_mount_filter_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The opaque identifier used to identify the secondary. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sys_replication_performance_status**
> get_sys_replication_performance_status()



### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.SystemApi()

try:
    api_instance.get_sys_replication_performance_status()
except ApiException as e:
    print("Exception when calling SystemApi->get_sys_replication_performance_status: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sys_replication_status**
> get_sys_replication_status()



### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.SystemApi()

try:
    api_instance.get_sys_replication_status()
except ApiException as e:
    print("Exception when calling SystemApi->get_sys_replication_status: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sys_seal_status**
> get_sys_seal_status()

Check the seal status of a Vault.

### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.SystemApi()

try:
    # Check the seal status of a Vault.
    api_instance.get_sys_seal_status()
except ApiException as e:
    print("Exception when calling SystemApi->get_sys_seal_status: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sys_wrapping_lookup**
> get_sys_wrapping_lookup()

Look up wrapping properties for the requester's token.

### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.SystemApi()

try:
    # Look up wrapping properties for the requester's token.
    api_instance.get_sys_wrapping_lookup()
except ApiException as e:
    print("Exception when calling SystemApi->get_sys_wrapping_lookup: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_sys_audit_hash_path**
> post_sys_audit_hash_path(path, body=body)

The hash of the given string via the given audit backend

### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.SystemApi()
path = 'path_example' # str | The name of the backend. Cannot be delimited. Example: \"mysql\"
body = hashicorp_vault_client.Body41() # Body41 |  (optional)

try:
    # The hash of the given string via the given audit backend
    api_instance.post_sys_audit_hash_path(path, body=body)
except ApiException as e:
    print("Exception when calling SystemApi->post_sys_audit_hash_path: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| The name of the backend. Cannot be delimited. Example: \&quot;mysql\&quot; | 
 **body** | [**Body41**](Body41.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_sys_audit_path**
> post_sys_audit_path(path, body=body)

Enable a new audit device at the supplied path.

### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.SystemApi()
path = 'path_example' # str | The name of the backend. Cannot be delimited. Example: \"mysql\"
body = hashicorp_vault_client.Body42() # Body42 |  (optional)

try:
    # Enable a new audit device at the supplied path.
    api_instance.post_sys_audit_path(path, body=body)
except ApiException as e:
    print("Exception when calling SystemApi->post_sys_audit_path: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| The name of the backend. Cannot be delimited. Example: \&quot;mysql\&quot; | 
 **body** | [**Body42**](Body42.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_sys_auth_path**
> post_sys_auth_path(path, body=body)

Enables a new auth method.

After enabling, the auth method can be accessed and configured via the auth path specified as part of the URL. This auth path will be nested under the auth prefix.  For example, enable the \"foo\" auth method will make it accessible at /auth/foo.

### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.SystemApi()
path = 'path_example' # str | The path to mount to. Cannot be delimited. Example: \"user\"
body = hashicorp_vault_client.Body43() # Body43 |  (optional)

try:
    # Enables a new auth method.
    api_instance.post_sys_auth_path(path, body=body)
except ApiException as e:
    print("Exception when calling SystemApi->post_sys_auth_path: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| The path to mount to. Cannot be delimited. Example: \&quot;user\&quot; | 
 **body** | [**Body43**](Body43.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_sys_auth_path_tune**
> post_sys_auth_path_tune(path, body=body)

Tune configuration parameters for a given auth path.

This endpoint requires sudo capability on the final path, but the same functionality can be achieved without sudo via `sys/mounts/auth/[auth-path]/tune`.

### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.SystemApi()
path = 'path_example' # str | Tune the configuration parameters for an auth path.
body = hashicorp_vault_client.Body44() # Body44 |  (optional)

try:
    # Tune configuration parameters for a given auth path.
    api_instance.post_sys_auth_path_tune(path, body=body)
except ApiException as e:
    print("Exception when calling SystemApi->post_sys_auth_path_tune: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| Tune the configuration parameters for an auth path. | 
 **body** | [**Body44**](Body44.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_sys_capabilities**
> post_sys_capabilities(body=body)

Fetches the capabilities of the given token on the given path.

### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.SystemApi()
body = hashicorp_vault_client.Body45() # Body45 |  (optional)

try:
    # Fetches the capabilities of the given token on the given path.
    api_instance.post_sys_capabilities(body=body)
except ApiException as e:
    print("Exception when calling SystemApi->post_sys_capabilities: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body45**](Body45.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_sys_capabilities_accessor**
> post_sys_capabilities_accessor(body=body)

Fetches the capabilities of the token associated with the given token, on the given path.

### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.SystemApi()
body = hashicorp_vault_client.Body46() # Body46 |  (optional)

try:
    # Fetches the capabilities of the token associated with the given token, on the given path.
    api_instance.post_sys_capabilities_accessor(body=body)
except ApiException as e:
    print("Exception when calling SystemApi->post_sys_capabilities_accessor: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body46**](Body46.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_sys_capabilities_self**
> post_sys_capabilities_self(body=body)

Fetches the capabilities of the given token on the given path.

### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.SystemApi()
body = hashicorp_vault_client.Body47() # Body47 |  (optional)

try:
    # Fetches the capabilities of the given token on the given path.
    api_instance.post_sys_capabilities_self(body=body)
except ApiException as e:
    print("Exception when calling SystemApi->post_sys_capabilities_self: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body47**](Body47.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_sys_config_auditing_request_headers_header**
> post_sys_config_auditing_request_headers_header(header, body=body)

Enable auditing of a header.

### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.SystemApi()
header = 'header_example' # str | 
body = hashicorp_vault_client.Body48() # Body48 |  (optional)

try:
    # Enable auditing of a header.
    api_instance.post_sys_config_auditing_request_headers_header(header, body=body)
except ApiException as e:
    print("Exception when calling SystemApi->post_sys_config_auditing_request_headers_header: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **header** | **str**|  | 
 **body** | [**Body48**](Body48.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_sys_config_control_group**
> post_sys_config_control_group(body=body)

Configure control group global settings.

### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.SystemApi()
body = hashicorp_vault_client.Body49() # Body49 |  (optional)

try:
    # Configure control group global settings.
    api_instance.post_sys_config_control_group(body=body)
except ApiException as e:
    print("Exception when calling SystemApi->post_sys_config_control_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body49**](Body49.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_sys_config_cors**
> post_sys_config_cors(body=body)

Configure the CORS settings.

### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.SystemApi()
body = hashicorp_vault_client.Body50() # Body50 |  (optional)

try:
    # Configure the CORS settings.
    api_instance.post_sys_config_cors(body=body)
except ApiException as e:
    print("Exception when calling SystemApi->post_sys_config_cors: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body50**](Body50.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_sys_config_ui_headers_header**
> post_sys_config_ui_headers_header(header, body=body)

Configure the values to be returned for the UI header.

### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.SystemApi()
header = 'header_example' # str | The name of the header.
body = hashicorp_vault_client.Body51() # Body51 |  (optional)

try:
    # Configure the values to be returned for the UI header.
    api_instance.post_sys_config_ui_headers_header(header, body=body)
except ApiException as e:
    print("Exception when calling SystemApi->post_sys_config_ui_headers_header: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **header** | **str**| The name of the header. | 
 **body** | [**Body51**](Body51.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_sys_control_group_authorize**
> post_sys_control_group_authorize(body=body)

Authorize a control group request

### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.SystemApi()
body = hashicorp_vault_client.Body52() # Body52 |  (optional)

try:
    # Authorize a control group request
    api_instance.post_sys_control_group_authorize(body=body)
except ApiException as e:
    print("Exception when calling SystemApi->post_sys_control_group_authorize: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body52**](Body52.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_sys_control_group_request**
> post_sys_control_group_request(body=body)

Check the status of a control group request

### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.SystemApi()
body = hashicorp_vault_client.Body53() # Body53 |  (optional)

try:
    # Check the status of a control group request
    api_instance.post_sys_control_group_request(body=body)
except ApiException as e:
    print("Exception when calling SystemApi->post_sys_control_group_request: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body53**](Body53.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_sys_generate_root**
> post_sys_generate_root(body=body)

Initializes a new root generation attempt.

Only a single root generation attempt can take place at a time. One (and only one) of otp or pgp_key are required.

### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.SystemApi()
body = hashicorp_vault_client.Body54() # Body54 |  (optional)

try:
    # Initializes a new root generation attempt.
    api_instance.post_sys_generate_root(body=body)
except ApiException as e:
    print("Exception when calling SystemApi->post_sys_generate_root: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body54**](Body54.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_sys_generate_root_attempt**
> post_sys_generate_root_attempt(body=body)

Initializes a new root generation attempt.

Only a single root generation attempt can take place at a time. One (and only one) of otp or pgp_key are required.

### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.SystemApi()
body = hashicorp_vault_client.Body55() # Body55 |  (optional)

try:
    # Initializes a new root generation attempt.
    api_instance.post_sys_generate_root_attempt(body=body)
except ApiException as e:
    print("Exception when calling SystemApi->post_sys_generate_root_attempt: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body55**](Body55.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_sys_generate_root_update**
> post_sys_generate_root_update(body=body)

Enter a single master key share to progress the root generation attempt.

If the threshold number of master key shares is reached, Vault will complete the root generation and issue the new token. Otherwise, this API must be called multiple times until that threshold is met. The attempt nonce must be provided with each call.

### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.SystemApi()
body = hashicorp_vault_client.Body56() # Body56 |  (optional)

try:
    # Enter a single master key share to progress the root generation attempt.
    api_instance.post_sys_generate_root_update(body=body)
except ApiException as e:
    print("Exception when calling SystemApi->post_sys_generate_root_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body56**](Body56.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_sys_init**
> post_sys_init(body=body)

Initialize a new Vault.

The Vault must not have been previously initialized. The recovery options, as well as the stored shares option, are only available when using Vault HSM.

### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.SystemApi()
body = hashicorp_vault_client.Body57() # Body57 |  (optional)

try:
    # Initialize a new Vault.
    api_instance.post_sys_init(body=body)
except ApiException as e:
    print("Exception when calling SystemApi->post_sys_init: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body57**](Body57.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_sys_leases_lookup**
> post_sys_leases_lookup(body=body)

Retrieve lease metadata.

### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.SystemApi()
body = hashicorp_vault_client.Body58() # Body58 |  (optional)

try:
    # Retrieve lease metadata.
    api_instance.post_sys_leases_lookup(body=body)
except ApiException as e:
    print("Exception when calling SystemApi->post_sys_leases_lookup: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body58**](Body58.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_sys_leases_renew**
> post_sys_leases_renew(body=body)

Renews a lease, requesting to extend the lease.

### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.SystemApi()
body = hashicorp_vault_client.Body59() # Body59 |  (optional)

try:
    # Renews a lease, requesting to extend the lease.
    api_instance.post_sys_leases_renew(body=body)
except ApiException as e:
    print("Exception when calling SystemApi->post_sys_leases_renew: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body59**](Body59.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_sys_leases_renew_url_lease_id**
> post_sys_leases_renew_url_lease_id(url_lease_id, body=body)

Renews a lease, requesting to extend the lease.

### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.SystemApi()
url_lease_id = 'url_lease_id_example' # str | The lease identifier to renew. This is included with a lease.
body = hashicorp_vault_client.Body60() # Body60 |  (optional)

try:
    # Renews a lease, requesting to extend the lease.
    api_instance.post_sys_leases_renew_url_lease_id(url_lease_id, body=body)
except ApiException as e:
    print("Exception when calling SystemApi->post_sys_leases_renew_url_lease_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **url_lease_id** | **str**| The lease identifier to renew. This is included with a lease. | 
 **body** | [**Body60**](Body60.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_sys_leases_revoke**
> post_sys_leases_revoke(body=body)

Revokes a lease immediately.

### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.SystemApi()
body = hashicorp_vault_client.Body61() # Body61 |  (optional)

try:
    # Revokes a lease immediately.
    api_instance.post_sys_leases_revoke(body=body)
except ApiException as e:
    print("Exception when calling SystemApi->post_sys_leases_revoke: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body61**](Body61.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_sys_leases_revoke_force_prefix**
> post_sys_leases_revoke_force_prefix(prefix)

Revokes all secrets or tokens generated under a given prefix immediately

Unlike `/sys/leases/revoke-prefix`, this path ignores backend errors encountered during revocation. This is potentially very dangerous and should only be used in specific emergency situations where errors in the backend or the connected backend service prevent normal revocation.  By ignoring these errors, Vault abdicates responsibility for ensuring that the issued credentials or secrets are properly revoked and/or cleaned up. Access to this endpoint should be tightly controlled.

### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.SystemApi()
prefix = 'prefix_example' # str | The path to revoke keys under. Example: \"prod/aws/ops\"

try:
    # Revokes all secrets or tokens generated under a given prefix immediately
    api_instance.post_sys_leases_revoke_force_prefix(prefix)
except ApiException as e:
    print("Exception when calling SystemApi->post_sys_leases_revoke_force_prefix: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **prefix** | **str**| The path to revoke keys under. Example: \&quot;prod/aws/ops\&quot; | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_sys_leases_revoke_prefix_prefix**
> post_sys_leases_revoke_prefix_prefix(prefix, body=body)

Revokes all secrets (via a lease ID prefix) or tokens (via the tokens' path property) generated under a given prefix immediately.

### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.SystemApi()
prefix = 'prefix_example' # str | The path to revoke keys under. Example: \"prod/aws/ops\"
body = hashicorp_vault_client.Body62() # Body62 |  (optional)

try:
    # Revokes all secrets (via a lease ID prefix) or tokens (via the tokens' path property) generated under a given prefix immediately.
    api_instance.post_sys_leases_revoke_prefix_prefix(prefix, body=body)
except ApiException as e:
    print("Exception when calling SystemApi->post_sys_leases_revoke_prefix_prefix: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **prefix** | **str**| The path to revoke keys under. Example: \&quot;prod/aws/ops\&quot; | 
 **body** | [**Body62**](Body62.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_sys_leases_revoke_url_lease_id**
> post_sys_leases_revoke_url_lease_id(url_lease_id, body=body)

Revokes a lease immediately.

### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.SystemApi()
url_lease_id = 'url_lease_id_example' # str | The lease identifier to renew. This is included with a lease.
body = hashicorp_vault_client.Body63() # Body63 |  (optional)

try:
    # Revokes a lease immediately.
    api_instance.post_sys_leases_revoke_url_lease_id(url_lease_id, body=body)
except ApiException as e:
    print("Exception when calling SystemApi->post_sys_leases_revoke_url_lease_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **url_lease_id** | **str**| The lease identifier to renew. This is included with a lease. | 
 **body** | [**Body63**](Body63.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_sys_leases_tidy**
> post_sys_leases_tidy()

This endpoint performs cleanup tasks that can be run if certain error conditions have occurred.

### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.SystemApi()

try:
    # This endpoint performs cleanup tasks that can be run if certain error conditions have occurred.
    api_instance.post_sys_leases_tidy()
except ApiException as e:
    print("Exception when calling SystemApi->post_sys_leases_tidy: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_sys_license**
> post_sys_license(body=body)

The path responds to the following HTTP methods.      GET /         Returns information on the installed license      POST         Sets the license for the server

### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.SystemApi()
body = hashicorp_vault_client.Body64() # Body64 |  (optional)

try:
    # The path responds to the following HTTP methods.      GET /         Returns information on the installed license      POST         Sets the license for the server
    api_instance.post_sys_license(body=body)
except ApiException as e:
    print("Exception when calling SystemApi->post_sys_license: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body64**](Body64.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_sys_mfa_method_duo_name**
> post_sys_mfa_method_duo_name(name, body=body)

Defines or updates a Duo MFA method.

### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.SystemApi()
name = 'name_example' # str | Name of the MFA method.
body = hashicorp_vault_client.Body65() # Body65 |  (optional)

try:
    # Defines or updates a Duo MFA method.
    api_instance.post_sys_mfa_method_duo_name(name, body=body)
except ApiException as e:
    print("Exception when calling SystemApi->post_sys_mfa_method_duo_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the MFA method. | 
 **body** | [**Body65**](Body65.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_sys_mfa_method_okta_name**
> post_sys_mfa_method_okta_name(name, body=body)

Defines or updates an Okta MFA method.

### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.SystemApi()
name = 'name_example' # str | Name of the MFA method.
body = hashicorp_vault_client.Body66() # Body66 |  (optional)

try:
    # Defines or updates an Okta MFA method.
    api_instance.post_sys_mfa_method_okta_name(name, body=body)
except ApiException as e:
    print("Exception when calling SystemApi->post_sys_mfa_method_okta_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the MFA method. | 
 **body** | [**Body66**](Body66.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_sys_mfa_method_pingid_name**
> post_sys_mfa_method_pingid_name(name, body=body)

Defines or updates a PingID MFA method.

### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.SystemApi()
name = 'name_example' # str | Name of the MFA method.
body = hashicorp_vault_client.Body67() # Body67 |  (optional)

try:
    # Defines or updates a PingID MFA method.
    api_instance.post_sys_mfa_method_pingid_name(name, body=body)
except ApiException as e:
    print("Exception when calling SystemApi->post_sys_mfa_method_pingid_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the MFA method. | 
 **body** | [**Body67**](Body67.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_sys_mfa_method_totp_name**
> post_sys_mfa_method_totp_name(name, body=body)

Defines or updates a TOTP MFA method.

### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.SystemApi()
name = 'name_example' # str | Name of the MFA method.
body = hashicorp_vault_client.Body68() # Body68 |  (optional)

try:
    # Defines or updates a TOTP MFA method.
    api_instance.post_sys_mfa_method_totp_name(name, body=body)
except ApiException as e:
    print("Exception when calling SystemApi->post_sys_mfa_method_totp_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the MFA method. | 
 **body** | [**Body68**](Body68.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_sys_mfa_method_totp_name_admin_destroy**
> post_sys_mfa_method_totp_name_admin_destroy(name, body=body)

Deletes the TOTP secret for the given method name on the given entity.

### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.SystemApi()
name = 'name_example' # str | Name of the MFA method.
body = hashicorp_vault_client.Body69() # Body69 |  (optional)

try:
    # Deletes the TOTP secret for the given method name on the given entity.
    api_instance.post_sys_mfa_method_totp_name_admin_destroy(name, body=body)
except ApiException as e:
    print("Exception when calling SystemApi->post_sys_mfa_method_totp_name_admin_destroy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the MFA method. | 
 **body** | [**Body69**](Body69.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_sys_mfa_method_totp_name_admin_generate**
> post_sys_mfa_method_totp_name_admin_generate(name, body=body)

Generates a TOTP secret for the given method name on the given entity.

### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.SystemApi()
name = 'name_example' # str | Name of the MFA method.
body = hashicorp_vault_client.Body70() # Body70 |  (optional)

try:
    # Generates a TOTP secret for the given method name on the given entity.
    api_instance.post_sys_mfa_method_totp_name_admin_generate(name, body=body)
except ApiException as e:
    print("Exception when calling SystemApi->post_sys_mfa_method_totp_name_admin_generate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the MFA method. | 
 **body** | [**Body70**](Body70.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_sys_mounts_path**
> post_sys_mounts_path(path, body=body)

Enable a new secrets engine at the given path.

### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.SystemApi()
path = 'path_example' # str | The path to mount to. Example: \"aws/east\"
body = hashicorp_vault_client.Body71() # Body71 |  (optional)

try:
    # Enable a new secrets engine at the given path.
    api_instance.post_sys_mounts_path(path, body=body)
except ApiException as e:
    print("Exception when calling SystemApi->post_sys_mounts_path: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| The path to mount to. Example: \&quot;aws/east\&quot; | 
 **body** | [**Body71**](Body71.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_sys_mounts_path_tune**
> post_sys_mounts_path_tune(path, body=body)

Tune backend configuration parameters for this mount.

### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.SystemApi()
path = 'path_example' # str | The path to mount to. Example: \"aws/east\"
body = hashicorp_vault_client.Body72() # Body72 |  (optional)

try:
    # Tune backend configuration parameters for this mount.
    api_instance.post_sys_mounts_path_tune(path, body=body)
except ApiException as e:
    print("Exception when calling SystemApi->post_sys_mounts_path_tune: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| The path to mount to. Example: \&quot;aws/east\&quot; | 
 **body** | [**Body72**](Body72.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_sys_namespaces_path**
> post_sys_namespaces_path(path)



### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.SystemApi()
path = 'path_example' # str | Path of the namespace.

try:
    api_instance.post_sys_namespaces_path(path)
except ApiException as e:
    print("Exception when calling SystemApi->post_sys_namespaces_path: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| Path of the namespace. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_sys_plugins_catalog_name**
> post_sys_plugins_catalog_name(name, body=body)

Register a new plugin, or updates an existing one with the supplied name.

### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.SystemApi()
name = 'name_example' # str | The name of the plugin
body = hashicorp_vault_client.Body73() # Body73 |  (optional)

try:
    # Register a new plugin, or updates an existing one with the supplied name.
    api_instance.post_sys_plugins_catalog_name(name, body=body)
except ApiException as e:
    print("Exception when calling SystemApi->post_sys_plugins_catalog_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the plugin | 
 **body** | [**Body73**](Body73.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_sys_plugins_catalog_type_name**
> post_sys_plugins_catalog_type_name(name, type, body=body)

Register a new plugin, or updates an existing one with the supplied name.

### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.SystemApi()
name = 'name_example' # str | The name of the plugin
type = 'type_example' # str | The type of the plugin, may be auth, secret, or database
body = hashicorp_vault_client.Body74() # Body74 |  (optional)

try:
    # Register a new plugin, or updates an existing one with the supplied name.
    api_instance.post_sys_plugins_catalog_type_name(name, type, body=body)
except ApiException as e:
    print("Exception when calling SystemApi->post_sys_plugins_catalog_type_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the plugin | 
 **type** | **str**| The type of the plugin, may be auth, secret, or database | 
 **body** | [**Body74**](Body74.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_sys_plugins_reload_backend**
> post_sys_plugins_reload_backend(body=body)

Reload mounted plugin backends.

Either the plugin name (`plugin`) or the desired plugin backend mounts (`mounts`) must be provided, but not both. In the case that the plugin name is provided, all mounted paths that use that plugin backend will be reloaded.

### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.SystemApi()
body = hashicorp_vault_client.Body75() # Body75 |  (optional)

try:
    # Reload mounted plugin backends.
    api_instance.post_sys_plugins_reload_backend(body=body)
except ApiException as e:
    print("Exception when calling SystemApi->post_sys_plugins_reload_backend: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body75**](Body75.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_sys_policies_acl_name**
> post_sys_policies_acl_name(name, body=body)

Add a new or update an existing ACL policy.

### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.SystemApi()
name = 'name_example' # str | The name of the policy. Example: \"ops\"
body = hashicorp_vault_client.Body76() # Body76 |  (optional)

try:
    # Add a new or update an existing ACL policy.
    api_instance.post_sys_policies_acl_name(name, body=body)
except ApiException as e:
    print("Exception when calling SystemApi->post_sys_policies_acl_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the policy. Example: \&quot;ops\&quot; | 
 **body** | [**Body76**](Body76.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_sys_policies_egp_name**
> post_sys_policies_egp_name(name, body=body)

Read, Modify, or Delete an access control policy.

### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.SystemApi()
name = 'name_example' # str | The name of the policy. Example: \"ops\"
body = hashicorp_vault_client.Body77() # Body77 |  (optional)

try:
    # Read, Modify, or Delete an access control policy.
    api_instance.post_sys_policies_egp_name(name, body=body)
except ApiException as e:
    print("Exception when calling SystemApi->post_sys_policies_egp_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the policy. Example: \&quot;ops\&quot; | 
 **body** | [**Body77**](Body77.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_sys_policies_rgp_name**
> post_sys_policies_rgp_name(name, body=body)

Read, Modify, or Delete an access control policy.

### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.SystemApi()
name = 'name_example' # str | The name of the policy. Example: \"ops\"
body = hashicorp_vault_client.Body78() # Body78 |  (optional)

try:
    # Read, Modify, or Delete an access control policy.
    api_instance.post_sys_policies_rgp_name(name, body=body)
except ApiException as e:
    print("Exception when calling SystemApi->post_sys_policies_rgp_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the policy. Example: \&quot;ops\&quot; | 
 **body** | [**Body78**](Body78.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_sys_policy_name**
> post_sys_policy_name(name, body=body)

Add a new or update an existing policy.

### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.SystemApi()
name = 'name_example' # str | The name of the policy. Example: \"ops\"
body = hashicorp_vault_client.Body79() # Body79 |  (optional)

try:
    # Add a new or update an existing policy.
    api_instance.post_sys_policy_name(name, body=body)
except ApiException as e:
    print("Exception when calling SystemApi->post_sys_policy_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the policy. Example: \&quot;ops\&quot; | 
 **body** | [**Body79**](Body79.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_sys_rekey_init**
> post_sys_rekey_init(body=body)

Initializes a new rekey attempt.

Only a single rekey attempt can take place at a time, and changing the parameters of a rekey requires canceling and starting a new rekey, which will also provide a new nonce.

### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.SystemApi()
body = hashicorp_vault_client.Body80() # Body80 |  (optional)

try:
    # Initializes a new rekey attempt.
    api_instance.post_sys_rekey_init(body=body)
except ApiException as e:
    print("Exception when calling SystemApi->post_sys_rekey_init: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body80**](Body80.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_sys_rekey_update**
> post_sys_rekey_update(body=body)

Enter a single master key share to progress the rekey of the Vault.

### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.SystemApi()
body = hashicorp_vault_client.Body81() # Body81 |  (optional)

try:
    # Enter a single master key share to progress the rekey of the Vault.
    api_instance.post_sys_rekey_update(body=body)
except ApiException as e:
    print("Exception when calling SystemApi->post_sys_rekey_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body81**](Body81.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_sys_rekey_verify**
> post_sys_rekey_verify(body=body)

Enter a single new key share to progress the rekey verification operation.

### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.SystemApi()
body = hashicorp_vault_client.Body82() # Body82 |  (optional)

try:
    # Enter a single new key share to progress the rekey verification operation.
    api_instance.post_sys_rekey_verify(body=body)
except ApiException as e:
    print("Exception when calling SystemApi->post_sys_rekey_verify: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body82**](Body82.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_sys_remount**
> post_sys_remount(body=body)

Move the mount point of an already-mounted backend.

### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.SystemApi()
body = hashicorp_vault_client.Body83() # Body83 |  (optional)

try:
    # Move the mount point of an already-mounted backend.
    api_instance.post_sys_remount(body=body)
except ApiException as e:
    print("Exception when calling SystemApi->post_sys_remount: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body83**](Body83.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_sys_renew**
> post_sys_renew(body=body)

Renews a lease, requesting to extend the lease.

### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.SystemApi()
body = hashicorp_vault_client.Body84() # Body84 |  (optional)

try:
    # Renews a lease, requesting to extend the lease.
    api_instance.post_sys_renew(body=body)
except ApiException as e:
    print("Exception when calling SystemApi->post_sys_renew: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body84**](Body84.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_sys_renew_url_lease_id**
> post_sys_renew_url_lease_id(url_lease_id, body=body)

Renews a lease, requesting to extend the lease.

### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.SystemApi()
url_lease_id = 'url_lease_id_example' # str | The lease identifier to renew. This is included with a lease.
body = hashicorp_vault_client.Body85() # Body85 |  (optional)

try:
    # Renews a lease, requesting to extend the lease.
    api_instance.post_sys_renew_url_lease_id(url_lease_id, body=body)
except ApiException as e:
    print("Exception when calling SystemApi->post_sys_renew_url_lease_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **url_lease_id** | **str**| The lease identifier to renew. This is included with a lease. | 
 **body** | [**Body85**](Body85.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_sys_replication_dr_primary_demote**
> post_sys_replication_dr_primary_demote()



### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.SystemApi()

try:
    api_instance.post_sys_replication_dr_primary_demote()
except ApiException as e:
    print("Exception when calling SystemApi->post_sys_replication_dr_primary_demote: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_sys_replication_dr_primary_disable**
> post_sys_replication_dr_primary_disable()



### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.SystemApi()

try:
    api_instance.post_sys_replication_dr_primary_disable()
except ApiException as e:
    print("Exception when calling SystemApi->post_sys_replication_dr_primary_disable: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_sys_replication_dr_primary_enable**
> post_sys_replication_dr_primary_enable(body=body)



### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.SystemApi()
body = hashicorp_vault_client.Body86() # Body86 |  (optional)

try:
    api_instance.post_sys_replication_dr_primary_enable(body=body)
except ApiException as e:
    print("Exception when calling SystemApi->post_sys_replication_dr_primary_enable: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body86**](Body86.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_sys_replication_dr_primary_revoke_secondary**
> post_sys_replication_dr_primary_revoke_secondary(body=body)



### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.SystemApi()
body = hashicorp_vault_client.Body87() # Body87 |  (optional)

try:
    api_instance.post_sys_replication_dr_primary_revoke_secondary(body=body)
except ApiException as e:
    print("Exception when calling SystemApi->post_sys_replication_dr_primary_revoke_secondary: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body87**](Body87.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_sys_replication_dr_primary_secondary_token**
> post_sys_replication_dr_primary_secondary_token(body=body)



### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.SystemApi()
body = hashicorp_vault_client.Body88() # Body88 |  (optional)

try:
    api_instance.post_sys_replication_dr_primary_secondary_token(body=body)
except ApiException as e:
    print("Exception when calling SystemApi->post_sys_replication_dr_primary_secondary_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body88**](Body88.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_sys_replication_dr_secondary_disable**
> post_sys_replication_dr_secondary_disable()



### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.SystemApi()

try:
    api_instance.post_sys_replication_dr_secondary_disable()
except ApiException as e:
    print("Exception when calling SystemApi->post_sys_replication_dr_secondary_disable: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_sys_replication_dr_secondary_enable**
> post_sys_replication_dr_secondary_enable(body=body)



### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.SystemApi()
body = hashicorp_vault_client.Body89() # Body89 |  (optional)

try:
    api_instance.post_sys_replication_dr_secondary_enable(body=body)
except ApiException as e:
    print("Exception when calling SystemApi->post_sys_replication_dr_secondary_enable: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body89**](Body89.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_sys_replication_dr_secondary_generate_public_key**
> post_sys_replication_dr_secondary_generate_public_key()



### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.SystemApi()

try:
    api_instance.post_sys_replication_dr_secondary_generate_public_key()
except ApiException as e:
    print("Exception when calling SystemApi->post_sys_replication_dr_secondary_generate_public_key: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_sys_replication_dr_secondary_license**
> post_sys_replication_dr_secondary_license(body=body)

The path responds to the following HTTP methods.      GET /         Returns information on the installed license      POST         Sets the license for the server

### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.SystemApi()
body = hashicorp_vault_client.Body90() # Body90 |  (optional)

try:
    # The path responds to the following HTTP methods.      GET /         Returns information on the installed license      POST         Sets the license for the server
    api_instance.post_sys_replication_dr_secondary_license(body=body)
except ApiException as e:
    print("Exception when calling SystemApi->post_sys_replication_dr_secondary_license: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body90**](Body90.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_sys_replication_dr_secondary_operation_token_delete**
> post_sys_replication_dr_secondary_operation_token_delete(body=body)



### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.SystemApi()
body = hashicorp_vault_client.Body91() # Body91 |  (optional)

try:
    api_instance.post_sys_replication_dr_secondary_operation_token_delete(body=body)
except ApiException as e:
    print("Exception when calling SystemApi->post_sys_replication_dr_secondary_operation_token_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body91**](Body91.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_sys_replication_dr_secondary_promote**
> post_sys_replication_dr_secondary_promote(body=body)



### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.SystemApi()
body = hashicorp_vault_client.Body92() # Body92 |  (optional)

try:
    api_instance.post_sys_replication_dr_secondary_promote(body=body)
except ApiException as e:
    print("Exception when calling SystemApi->post_sys_replication_dr_secondary_promote: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body92**](Body92.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_sys_replication_dr_secondary_reindex**
> post_sys_replication_dr_secondary_reindex(body=body)



### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.SystemApi()
body = hashicorp_vault_client.Body93() # Body93 |  (optional)

try:
    api_instance.post_sys_replication_dr_secondary_reindex(body=body)
except ApiException as e:
    print("Exception when calling SystemApi->post_sys_replication_dr_secondary_reindex: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body93**](Body93.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_sys_replication_dr_secondary_update_primary**
> post_sys_replication_dr_secondary_update_primary(body=body)



### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.SystemApi()
body = hashicorp_vault_client.Body94() # Body94 |  (optional)

try:
    api_instance.post_sys_replication_dr_secondary_update_primary(body=body)
except ApiException as e:
    print("Exception when calling SystemApi->post_sys_replication_dr_secondary_update_primary: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body94**](Body94.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_sys_replication_performance_primary_demote**
> post_sys_replication_performance_primary_demote()



### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.SystemApi()

try:
    api_instance.post_sys_replication_performance_primary_demote()
except ApiException as e:
    print("Exception when calling SystemApi->post_sys_replication_performance_primary_demote: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_sys_replication_performance_primary_disable**
> post_sys_replication_performance_primary_disable()



### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.SystemApi()

try:
    api_instance.post_sys_replication_performance_primary_disable()
except ApiException as e:
    print("Exception when calling SystemApi->post_sys_replication_performance_primary_disable: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_sys_replication_performance_primary_enable**
> post_sys_replication_performance_primary_enable(body=body)



### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.SystemApi()
body = hashicorp_vault_client.Body95() # Body95 |  (optional)

try:
    api_instance.post_sys_replication_performance_primary_enable(body=body)
except ApiException as e:
    print("Exception when calling SystemApi->post_sys_replication_performance_primary_enable: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body95**](Body95.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_sys_replication_performance_primary_mount_filter_id**
> post_sys_replication_performance_primary_mount_filter_id(id, body=body)



### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.SystemApi()
id = 'id_example' # str | The opaque identifier used to identify the secondary.
body = hashicorp_vault_client.Body96() # Body96 |  (optional)

try:
    api_instance.post_sys_replication_performance_primary_mount_filter_id(id, body=body)
except ApiException as e:
    print("Exception when calling SystemApi->post_sys_replication_performance_primary_mount_filter_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The opaque identifier used to identify the secondary. | 
 **body** | [**Body96**](Body96.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_sys_replication_performance_primary_revoke_secondary**
> post_sys_replication_performance_primary_revoke_secondary(body=body)



### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.SystemApi()
body = hashicorp_vault_client.Body97() # Body97 |  (optional)

try:
    api_instance.post_sys_replication_performance_primary_revoke_secondary(body=body)
except ApiException as e:
    print("Exception when calling SystemApi->post_sys_replication_performance_primary_revoke_secondary: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body97**](Body97.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_sys_replication_performance_primary_secondary_token**
> post_sys_replication_performance_primary_secondary_token(body=body)



### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.SystemApi()
body = hashicorp_vault_client.Body98() # Body98 |  (optional)

try:
    api_instance.post_sys_replication_performance_primary_secondary_token(body=body)
except ApiException as e:
    print("Exception when calling SystemApi->post_sys_replication_performance_primary_secondary_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body98**](Body98.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_sys_replication_performance_secondary_disable**
> post_sys_replication_performance_secondary_disable()



### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.SystemApi()

try:
    api_instance.post_sys_replication_performance_secondary_disable()
except ApiException as e:
    print("Exception when calling SystemApi->post_sys_replication_performance_secondary_disable: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_sys_replication_performance_secondary_enable**
> post_sys_replication_performance_secondary_enable(body=body)



### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.SystemApi()
body = hashicorp_vault_client.Body99() # Body99 |  (optional)

try:
    api_instance.post_sys_replication_performance_secondary_enable(body=body)
except ApiException as e:
    print("Exception when calling SystemApi->post_sys_replication_performance_secondary_enable: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body99**](Body99.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_sys_replication_performance_secondary_generate_public_key**
> post_sys_replication_performance_secondary_generate_public_key()



### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.SystemApi()

try:
    api_instance.post_sys_replication_performance_secondary_generate_public_key()
except ApiException as e:
    print("Exception when calling SystemApi->post_sys_replication_performance_secondary_generate_public_key: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_sys_replication_performance_secondary_promote**
> post_sys_replication_performance_secondary_promote(body=body)



### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.SystemApi()
body = hashicorp_vault_client.Body100() # Body100 |  (optional)

try:
    api_instance.post_sys_replication_performance_secondary_promote(body=body)
except ApiException as e:
    print("Exception when calling SystemApi->post_sys_replication_performance_secondary_promote: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body100**](Body100.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_sys_replication_performance_secondary_update_primary**
> post_sys_replication_performance_secondary_update_primary(body=body)



### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.SystemApi()
body = hashicorp_vault_client.Body101() # Body101 |  (optional)

try:
    api_instance.post_sys_replication_performance_secondary_update_primary(body=body)
except ApiException as e:
    print("Exception when calling SystemApi->post_sys_replication_performance_secondary_update_primary: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body101**](Body101.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_sys_replication_primary_demote**
> post_sys_replication_primary_demote()



### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.SystemApi()

try:
    api_instance.post_sys_replication_primary_demote()
except ApiException as e:
    print("Exception when calling SystemApi->post_sys_replication_primary_demote: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_sys_replication_primary_disable**
> post_sys_replication_primary_disable()



### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.SystemApi()

try:
    api_instance.post_sys_replication_primary_disable()
except ApiException as e:
    print("Exception when calling SystemApi->post_sys_replication_primary_disable: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_sys_replication_primary_enable**
> post_sys_replication_primary_enable(body=body)



### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.SystemApi()
body = hashicorp_vault_client.Body102() # Body102 |  (optional)

try:
    api_instance.post_sys_replication_primary_enable(body=body)
except ApiException as e:
    print("Exception when calling SystemApi->post_sys_replication_primary_enable: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body102**](Body102.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_sys_replication_primary_revoke_secondary**
> post_sys_replication_primary_revoke_secondary(body=body)



### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.SystemApi()
body = hashicorp_vault_client.Body103() # Body103 |  (optional)

try:
    api_instance.post_sys_replication_primary_revoke_secondary(body=body)
except ApiException as e:
    print("Exception when calling SystemApi->post_sys_replication_primary_revoke_secondary: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body103**](Body103.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_sys_replication_primary_secondary_token**
> post_sys_replication_primary_secondary_token(body=body)



### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.SystemApi()
body = hashicorp_vault_client.Body104() # Body104 |  (optional)

try:
    api_instance.post_sys_replication_primary_secondary_token(body=body)
except ApiException as e:
    print("Exception when calling SystemApi->post_sys_replication_primary_secondary_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body104**](Body104.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_sys_replication_recover**
> post_sys_replication_recover()



### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.SystemApi()

try:
    api_instance.post_sys_replication_recover()
except ApiException as e:
    print("Exception when calling SystemApi->post_sys_replication_recover: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_sys_replication_reindex**
> post_sys_replication_reindex(body=body)



### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.SystemApi()
body = hashicorp_vault_client.Body105() # Body105 |  (optional)

try:
    api_instance.post_sys_replication_reindex(body=body)
except ApiException as e:
    print("Exception when calling SystemApi->post_sys_replication_reindex: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body105**](Body105.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_sys_replication_secondary_disable**
> post_sys_replication_secondary_disable()



### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.SystemApi()

try:
    api_instance.post_sys_replication_secondary_disable()
except ApiException as e:
    print("Exception when calling SystemApi->post_sys_replication_secondary_disable: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_sys_replication_secondary_enable**
> post_sys_replication_secondary_enable(body=body)



### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.SystemApi()
body = hashicorp_vault_client.Body106() # Body106 |  (optional)

try:
    api_instance.post_sys_replication_secondary_enable(body=body)
except ApiException as e:
    print("Exception when calling SystemApi->post_sys_replication_secondary_enable: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body106**](Body106.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_sys_replication_secondary_promote**
> post_sys_replication_secondary_promote(body=body)



### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.SystemApi()
body = hashicorp_vault_client.Body107() # Body107 |  (optional)

try:
    api_instance.post_sys_replication_secondary_promote(body=body)
except ApiException as e:
    print("Exception when calling SystemApi->post_sys_replication_secondary_promote: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body107**](Body107.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_sys_replication_secondary_update_primary**
> post_sys_replication_secondary_update_primary(body=body)



### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.SystemApi()
body = hashicorp_vault_client.Body108() # Body108 |  (optional)

try:
    api_instance.post_sys_replication_secondary_update_primary(body=body)
except ApiException as e:
    print("Exception when calling SystemApi->post_sys_replication_secondary_update_primary: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body108**](Body108.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_sys_revoke**
> post_sys_revoke(body=body)

Revokes a lease immediately.

### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.SystemApi()
body = hashicorp_vault_client.Body109() # Body109 |  (optional)

try:
    # Revokes a lease immediately.
    api_instance.post_sys_revoke(body=body)
except ApiException as e:
    print("Exception when calling SystemApi->post_sys_revoke: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body109**](Body109.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_sys_revoke_force_prefix**
> post_sys_revoke_force_prefix(prefix)

Revokes all secrets or tokens generated under a given prefix immediately

Unlike `/sys/leases/revoke-prefix`, this path ignores backend errors encountered during revocation. This is potentially very dangerous and should only be used in specific emergency situations where errors in the backend or the connected backend service prevent normal revocation.  By ignoring these errors, Vault abdicates responsibility for ensuring that the issued credentials or secrets are properly revoked and/or cleaned up. Access to this endpoint should be tightly controlled.

### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.SystemApi()
prefix = 'prefix_example' # str | The path to revoke keys under. Example: \"prod/aws/ops\"

try:
    # Revokes all secrets or tokens generated under a given prefix immediately
    api_instance.post_sys_revoke_force_prefix(prefix)
except ApiException as e:
    print("Exception when calling SystemApi->post_sys_revoke_force_prefix: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **prefix** | **str**| The path to revoke keys under. Example: \&quot;prod/aws/ops\&quot; | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_sys_revoke_prefix_prefix**
> post_sys_revoke_prefix_prefix(prefix, body=body)

Revokes all secrets (via a lease ID prefix) or tokens (via the tokens' path property) generated under a given prefix immediately.

### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.SystemApi()
prefix = 'prefix_example' # str | The path to revoke keys under. Example: \"prod/aws/ops\"
body = hashicorp_vault_client.Body110() # Body110 |  (optional)

try:
    # Revokes all secrets (via a lease ID prefix) or tokens (via the tokens' path property) generated under a given prefix immediately.
    api_instance.post_sys_revoke_prefix_prefix(prefix, body=body)
except ApiException as e:
    print("Exception when calling SystemApi->post_sys_revoke_prefix_prefix: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **prefix** | **str**| The path to revoke keys under. Example: \&quot;prod/aws/ops\&quot; | 
 **body** | [**Body110**](Body110.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_sys_revoke_url_lease_id**
> post_sys_revoke_url_lease_id(url_lease_id, body=body)

Revokes a lease immediately.

### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.SystemApi()
url_lease_id = 'url_lease_id_example' # str | The lease identifier to renew. This is included with a lease.
body = hashicorp_vault_client.Body111() # Body111 |  (optional)

try:
    # Revokes a lease immediately.
    api_instance.post_sys_revoke_url_lease_id(url_lease_id, body=body)
except ApiException as e:
    print("Exception when calling SystemApi->post_sys_revoke_url_lease_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **url_lease_id** | **str**| The lease identifier to renew. This is included with a lease. | 
 **body** | [**Body111**](Body111.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_sys_rotate**
> post_sys_rotate()

Rotates the backend encryption key used to persist data.

### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.SystemApi()

try:
    # Rotates the backend encryption key used to persist data.
    api_instance.post_sys_rotate()
except ApiException as e:
    print("Exception when calling SystemApi->post_sys_rotate: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_sys_seal**
> post_sys_seal()

Seal the Vault.

### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.SystemApi()

try:
    # Seal the Vault.
    api_instance.post_sys_seal()
except ApiException as e:
    print("Exception when calling SystemApi->post_sys_seal: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_sys_step_down**
> post_sys_step_down()

Cause the node to give up active status.

This endpoint forces the node to give up active status. If the node does not have active status, this endpoint does nothing. Note that the node will sleep for ten seconds before attempting to grab the active lock again, but if no standby nodes grab the active lock in the interim, the same node may become the active node again.

### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.SystemApi()

try:
    # Cause the node to give up active status.
    api_instance.post_sys_step_down()
except ApiException as e:
    print("Exception when calling SystemApi->post_sys_step_down: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_sys_tools_hash**
> post_sys_tools_hash(body=body)

Generate a hash sum for input data

### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.SystemApi()
body = hashicorp_vault_client.Body112() # Body112 |  (optional)

try:
    # Generate a hash sum for input data
    api_instance.post_sys_tools_hash(body=body)
except ApiException as e:
    print("Exception when calling SystemApi->post_sys_tools_hash: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body112**](Body112.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_sys_tools_hash_urlalgorithm**
> post_sys_tools_hash_urlalgorithm(urlalgorithm, body=body)

Generate a hash sum for input data

### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.SystemApi()
urlalgorithm = 'urlalgorithm_example' # str | Algorithm to use (POST URL parameter)
body = hashicorp_vault_client.Body113() # Body113 |  (optional)

try:
    # Generate a hash sum for input data
    api_instance.post_sys_tools_hash_urlalgorithm(urlalgorithm, body=body)
except ApiException as e:
    print("Exception when calling SystemApi->post_sys_tools_hash_urlalgorithm: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **urlalgorithm** | **str**| Algorithm to use (POST URL parameter) | 
 **body** | [**Body113**](Body113.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_sys_tools_random**
> post_sys_tools_random(body=body)

Generate random bytes

### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.SystemApi()
body = hashicorp_vault_client.Body114() # Body114 |  (optional)

try:
    # Generate random bytes
    api_instance.post_sys_tools_random(body=body)
except ApiException as e:
    print("Exception when calling SystemApi->post_sys_tools_random: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body114**](Body114.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_sys_tools_random_urlbytes**
> post_sys_tools_random_urlbytes(urlbytes, body=body)

Generate random bytes

### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.SystemApi()
urlbytes = 'urlbytes_example' # str | The number of bytes to generate (POST URL parameter)
body = hashicorp_vault_client.Body115() # Body115 |  (optional)

try:
    # Generate random bytes
    api_instance.post_sys_tools_random_urlbytes(urlbytes, body=body)
except ApiException as e:
    print("Exception when calling SystemApi->post_sys_tools_random_urlbytes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **urlbytes** | **str**| The number of bytes to generate (POST URL parameter) | 
 **body** | [**Body115**](Body115.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_sys_unseal**
> post_sys_unseal(body=body)

Unseal the Vault.

### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.SystemApi()
body = hashicorp_vault_client.Body116() # Body116 |  (optional)

try:
    # Unseal the Vault.
    api_instance.post_sys_unseal(body=body)
except ApiException as e:
    print("Exception when calling SystemApi->post_sys_unseal: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body116**](Body116.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_sys_wrapping_lookup**
> post_sys_wrapping_lookup(body=body)

Look up wrapping properties for the given token.

### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.SystemApi()
body = hashicorp_vault_client.Body117() # Body117 |  (optional)

try:
    # Look up wrapping properties for the given token.
    api_instance.post_sys_wrapping_lookup(body=body)
except ApiException as e:
    print("Exception when calling SystemApi->post_sys_wrapping_lookup: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body117**](Body117.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_sys_wrapping_rewrap**
> post_sys_wrapping_rewrap(body=body)

Rotates a response-wrapped token.

### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.SystemApi()
body = hashicorp_vault_client.Body118() # Body118 |  (optional)

try:
    # Rotates a response-wrapped token.
    api_instance.post_sys_wrapping_rewrap(body=body)
except ApiException as e:
    print("Exception when calling SystemApi->post_sys_wrapping_rewrap: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body118**](Body118.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_sys_wrapping_unwrap**
> post_sys_wrapping_unwrap(body=body)

Unwraps a response-wrapped token.

### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.SystemApi()
body = hashicorp_vault_client.Body119() # Body119 |  (optional)

try:
    # Unwraps a response-wrapped token.
    api_instance.post_sys_wrapping_unwrap(body=body)
except ApiException as e:
    print("Exception when calling SystemApi->post_sys_wrapping_unwrap: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body119**](Body119.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_sys_wrapping_wrap**
> post_sys_wrapping_wrap()

Response-wraps an arbitrary JSON object.

### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.SystemApi()

try:
    # Response-wraps an arbitrary JSON object.
    api_instance.post_sys_wrapping_wrap()
except ApiException as e:
    print("Exception when calling SystemApi->post_sys_wrapping_wrap: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

