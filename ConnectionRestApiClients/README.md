# Build python client from Open API 

docker run --rm -v "${PWD}:/local" openapitools/openapi-generator-cli generate -i /local/swagger.json -g python -o /local/clients/python --additional-properties=packageName=connection_restapi_client_poc,packageVersion=1.2.0

# Build python client from Open API with custom template
docker run --rm -v "${PWD}:/local" openapitools/openapi-generator-cli generate -i /local/swagger.json -g python -t /local/templates/python -o /local/clients/python --additional-properties=packageName=connection_restapi_client_poc,packageVersion=1.2.0

# Build c# client from Open API with custom template
docker run --rm -v "${PWD}:/local" openapitools/openapi-generator-cli generate -i /local/swagger.json -g csharp -t /local/templates/csharp -o /local/clients/csharp --global-property apiTests=false,modelTests=false --additional-properties=packageName=connection_restapi_client_poc,projectGuid=89E67D42-C718-410B-89D4-104151F3EC0D,targetFramework='netstandard2.0;netstandard2.1',nullableReferenceTypes=false,netCoreProjectFile=true,packageVersion=24.1.0

# Build typescript-node client from Open API
docker run --rm -v "${PWD}:/local" openapitools/openapi-generator-cli generate -i /local/swagger.json -g typescript-node -o /local/clients/typescript-node/src --additional-properties=packageName=connection_restapi_client_poc,packageVersion=1.2.0

# Install connection_restapi_client_poc from directory

Open directory _.\ConnectionRestApiClients\clients\python_ in the cmd.exe
run _pip install ._

# Get author template
docker run --rm -v "${PWD}:/local" openapitools/openapi-generator-cli author template -g python -o /local/template/
docker run --rm -v "${PWD}:/local" openapitools/openapi-generator-cli author template -g csharp -o /local/template/

# Build and publish node.js package
```sh
npm install
npm run build
npm login
npm publish
```

