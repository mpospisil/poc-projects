import connection_restapi_client_poc
from connection_restapi_client_poc.rest import ApiException
from pprint import pprint
import os
import requests
from urllib.parse import urljoin
import json


baseUrl = "http://localhost:5000"

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = connection_restapi_client_poc.Configuration(
    host = baseUrl
)

dir_path = os.path.dirname(os.path.realpath(__file__))
project_file_path = os.path.join(dir_path, '..\..\projects', 'HSS_norm_cond.ideaCon')
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
            
             # get calculation API for the active project
            api_calculation = connection_restapi_client_poc.CalculationApi(api_client)

            # run stress-strain CBFEM analysis for the connection id = 1
            calcParams = connection_restapi_client_poc.IdeaStatiCaApiConnectionModelConCalculationParameterIdeaStatiCaApi()
            calcParams.connection_ids = [connection1.id]

            # run stress-strain analysis for the connection
            con1_cbfem_results = api_calculation.api1_projects_project_id_calculate_post(project_id, calcParams)
            pprint(con1_cbfem_results)

            # get detailed results
            results_text = api_calculation.api1_projects_project_id_rawresults_text_post(project_id, calcParams)
            #pprint(results_text)

            raw_results = json.loads(results_text)
            pprint(raw_results)

            detailed_results = api_calculation.api1_projects_project_id_results_post(project_id, calcParams)
            pprint(detailed_results)

            # get connection setup
            connection_setup =  api_project.api1_projects_project_id_connection_setup_get(project_id)
            pprint(connection_setup)

            # modify setup
            connection_setup.hss_limit_plastic_strain = 0.02
            modifiedSetup = api_project.api1_projects_project_id_connection_setup_put(project_id, connection_setup)

            # recalculate connection
            recalculate_results = api_calculation.api1_projects_project_id_calculate_post(project_id, calcParams)
            pprint(recalculate_results)

        except Exception as ee:
            print("Exception when calling CalculationApi->api1_projects_project_id_calculate_post: %s\n" % ee)

        finally:
            # close the active project on the backend
            closeProjectResult = api_project.api1_projects_project_id_close_get(project_id)

    except Exception as e:
        print("Exception when calling ProjectApi->api1_connect_client_get: %s\n" % e)