# Build python client from Open API 

docker run --rm -v "${PWD}:/local" openapitools/openapi-generator-cli generate -i /local/swagger.json -g python -o /local/clients/python --additional-properties=packageName=connection_restapi_client_poc,packageVersion=1.2.0

# Build python client from Open API with custom template
docker run --rm -v "${PWD}:/local" openapitools/openapi-generator-cli generate -i /local/swagger.json -g python -t /local/templates/python -o /local/clients/python --additional-properties=packageName=connection_restapi_client_poc,packageVersion=1.2.0

# Build typescript-node client from Open API
docker run --rm -v "${PWD}:/local" openapitools/openapi-generator-cli generate -i /local/swagger.json -g typescript-node -o /local/clients/typescript-node --additional-properties=packageName=connection_restapi_client_poc,packageVersion=24.0.5.0863

# Install connection_restapi_client_poc from directory

Open directory _.\ConnectionRestApiClients\clients\python_ in the cmd.exe
run _pip install ._

# Get author template
docker run --rm -v "${PWD}/template:/templates" openapitools/openapi-generator-cli author templates -g python -o ./template
