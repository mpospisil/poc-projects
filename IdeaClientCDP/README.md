# Build python client from Open API 

docker run --rm -v "${PWD}:/local" openapitools/openapi-generator-cli generate -i /local/swagger.json -g python -o /local/clients/python --additional-properties=packageName=idea_cdp_client_poc,packageVersion=1.1.0

