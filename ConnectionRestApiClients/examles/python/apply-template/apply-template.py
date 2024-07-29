import connection_restapi_client_poc
from connection_restapi_client_poc.rest import ApiException
from pprint import pprint
import os
import requests
from urllib.parse import urljoin
import json
from connection_restapi_client_poc.models.idea_stati_ca_plugin_api_connection_rest_model_model_template_con_template_mapping_get_param_idea_stati_ca_plugin import IdeaStatiCaPluginApiConnectionRestModelModelTemplateConTemplateMappingGetParamIdeaStatiCaPlugin
from connection_restapi_client_poc.models.idea_stati_ca_plugin_api_connection_rest_model_model_template_template_conversions_idea_stati_ca_plugin import IdeaStatiCaPluginApiConnectionRestModelModelTemplateTemplateConversionsIdeaStatiCaPlugin
from connection_restapi_client_poc.models.idea_stati_ca_plugin_api_connection_rest_model_model_template_con_template_apply_param_idea_stati_ca_plugin import IdeaStatiCaPluginApiConnectionRestModelModelTemplateConTemplateApplyParamIdeaStatiCaPlugin

baseUrl = "http://localhost:5000"

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = connection_restapi_client_poc.Configuration(
    host = baseUrl
)

dir_path = os.path.dirname(os.path.realpath(__file__))
project_file_path = os.path.join(dir_path, '..\..\projects', 'corner-empty.ideaCon')
print(project_file_path)

with open(project_file_path, 'rb') as file:
    byte_array = file.read()

# Enter a context with an instance of the API client
with connection_restapi_client_poc.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_project = connection_restapi_client_poc.ProjectApi(api_client)

    try:
        clientId = api_project.api1_connect_client_get()
        print("The response of ProjectApi->api1_connect_client_get:\n")
        pprint(clientId)

        # Add your ClientId to HTTP header
        api_client.default_headers['ClientId'] = clientId
        api_client.default_headers['Content-Type'] = 'application/json'


        # temporary workaround to upload the project file
        # it should be done directly by client later
        url = urljoin(baseUrl, 'api/1/projects/open')

        # Prepare headers if necessary (optional)
        headers = {
            "Content-Type": "application/octet-stream",
            "ClientId": clientId
        }

        # Send the POST request with the byte array
        response = requests.post(url, data=byte_array, headers=headers)
        print(response.status_code)

        if response.status_code == 200:
            # Parse the JSON response
            json_response = response.json()       
            # Get the projectId of the uploaded project from the response 
            project_id = json_response["projectId"]
        else:
            print("Error uploading the project file")
            raise Exception("Error uploading the project file")

        try:
            # Get the project data
            project_data = api_project.api1_projects_project_id_project_data_get(project_id)
            pprint(project_data)

            # Get API for connections in the project
            api_connection = connection_restapi_client_poc.ConnectionApi(api_client)

            # Get list of all connections in the project
            connections_in_project = api_connection.api1_projects_project_id_connections_get(project_id)

            # first connection in the project 
            connection1 = connections_in_project[0]

            pprint(connection1)
            
            api_template = connection_restapi_client_poc.TemplateApi(api_client)

            templateParam = IdeaStatiCaPluginApiConnectionRestModelModelTemplateConTemplateMappingGetParamIdeaStatiCaPlugin()

            template_file_name = os.path.join(dir_path, '..\..\projects', 'template-I-corner.contemp')
            with open(template_file_name, 'r', encoding='utf-16') as file:
                templateParam.template = file.read()

            # get the default mapping for the selected template and connection  
            default_mapping = api_template.api1_projects_project_id_connections_connection_id_apply_mapping_post(project_id, connection1.id, templateParam)
            pprint(default_mapping)

            # TODO
            # Modify mapping
          
            # Apply the template to the connection with the modified mapping
            applyTemplateData = connection_restapi_client_poc.IdeaStatiCaPluginApiConnectionRestModelModelTemplateConTemplateApplyParamIdeaStatiCaPlugin()
            applyTemplateData.connection_template = templateParam.template
            applyTemplateData.mapping = default_mapping

            applyTemplateResult = api_template.api1_projects_project_id_connections_connection_id_apply_template_post(project_id, connection1.id, applyTemplateData)
 
            pprint(applyTemplateResult)

            # get calculation API for the active project
            api_calculation = connection_restapi_client_poc.CalculationApi(api_client)             

            # run stress-strain CBFEM analysis for the connection id = 1
            calcParams = connection_restapi_client_poc.IdeaStatiCaPluginApiConnectionRestModelModelConnectionConCalculationParameterIdeaStatiCaPlugin()
            calcParams.connection_ids = [connection1.id]

            # run stress-strain analysis for the connection
            con1_cbfem_results1 = api_calculation.api1_projects_project_id_calculate_post(project_id, calcParams)
            pprint(con1_cbfem_results1)

            # modify loading



            # it doesn't work why ? wrong coding ?

            # # download modified ideacon file
            # projectDataStream = api_project.api1_projects_project_id_download_get(project_id)
            # updatedProject_file_path = os.path.join(dir_path, '..\..\projects', 'corner-updated.ideaCon')
            # with open(updatedProject_file_path, 'wb') as file:
            #     file.write(projectDataStream.read())


        except Exception as ee:
            print("Exception when calling CalculationApi->api1_projects_project_id_calculate_post: %s\n" % ee)

        finally:
            # close the active project on the backend
            closeProjectResult = api_project.api1_projects_project_id_close_get(project_id)

    except Exception as e:
        print("Exception when calling ProjectApi->api1_connect_client_get: %s\n" % e)