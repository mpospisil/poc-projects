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
        clientId = api_project.connect_client()
        print("The response of ProjectApi->api1_connect_client_get:\n")
        pprint(clientId)

        # Add your ClientId to HTTP header
        api_client.default_headers['ClientId'] = clientId
        
        # Override the default Content-Type for this specific call
        uploadRes = api_project.upload_idea_con(idea_con_file=byte_array, _content_type='multipart/form-data')
        project_id = uploadRes.project_id

        try:
            # Get the project data
            project_data = api_project.get_project_data(project_id)
            pprint(project_data)

            # Get API for connections in the project
            api_connection = connection_restapi_client_poc.ConnectionApi(api_client)

            # Get list of all connections in the project
            connections_in_project = api_connection.get_all_connections_data(project_id)

            # first connection in the project 
            connection1 = connections_in_project[0]

            pprint(connection1)
            
             # get calculation API for the active project
            api_calculation = connection_restapi_client_poc.CalculationApi(api_client)

            # run stress-strain CBFEM analysis for the connection id = 1
            calcParams = connection_restapi_client_poc.ConCalculationParameter() # ConCalculationParameter | List of connections to calculate and a type of CBFEM analysis (optional)
            calcParams.connection_ids = [connection1.id]

            # run stress-strain analysis for the connection
            con1_cbfem_results = api_calculation.calculate(project_id, calcParams)
            pprint(con1_cbfem_results)

            # get detailed results
            results_text = api_calculation.get_raw_json_results(project_id, calcParams)
            #pprint(results_text)

            raw_results = json.loads(results_text)
            pprint(raw_results)

            detailed_results = api_calculation.get_results(project_id, calcParams)
            pprint(detailed_results)

            # get connection setup
            connection_setup =  api_project.get_setup(project_id)
            pprint(connection_setup)

            # modify setup
            connection_setup.hss_limit_plastic_strain = 0.02
            modifiedSetup = api_project.update_setup(project_id, connection_setup)

            # recalculate connection
            recalculate_results = api_calculation.calculate(project_id, calcParams)
            pprint(recalculate_results)

        except Exception as ee:
            print("Exception when calling CalculationApi: %s\n" % ee)

        finally:
            # close the active project on the backend
            closeProjectResult = api_project.close_project(project_id)

    except Exception as e:
        print("Exception when calling ProjectApi->api1_connect_client_get: %s\n" % e)