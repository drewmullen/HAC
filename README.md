# HAC
H`VAC` A`uto` C`lient`

This is a temporary repo while i work on the initial version of the HVAC Auto Client (HAC), a hashicorp vault python client generated from OpenAPI 3.0 spec

How the client was generated:
```
$ cat config.json
{
  "packageName":"hashicorp_vault_client",
  "projectName":"hashicorp_vault_client",
  "packageVersion":"0.0.1"
}

git clone https://github.com/swagger-api/swagger-codegen
cd swagger-codegen
git checkout 3.0.0
mvn clean package
java -jar modules/swagger-codegen-cli/target/swagger-codegen-cli.jar generate \
   -i vault-spec.json \
   -l python \
   -o hashicorp_vault_client \
   -c config.json
```
