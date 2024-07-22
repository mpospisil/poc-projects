# Build python client from Open API 

docker run --rm -v "${PWD}:/local" openapitools/openapi-generator-cli generate -i /local/swagger.json -g python -o /local/clients/python --additional-properties=packageName=connection_restapi_client_poc,packageVersion=1.0.0

