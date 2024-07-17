docker run --rm -v "${PWD}:/local" openapitools/openapi-generator-cli generate -i /local/swagger.json -g python -o /local/clients/python

