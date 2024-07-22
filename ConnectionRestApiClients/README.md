# Build python client from Open API 

docker run --rm -v "${PWD}:/local" openapitools/openapi-generator-cli generate -i /local/swagger.json -g python -o /local/clients/python --additional-properties=packageName=connection_restapi_client_poc,packageVersion=1.2.0

# Install connection_restapi_client_poc from directory

Open directory _.\ConnectionRestApiClients\clients\python_ in the cmd.exe
run _pip install ._
