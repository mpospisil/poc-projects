import sys
import os
import json
from pprint import pprint
from urllib.parse import urljoin

# Get the parent directory
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))

# Add the parent directory to sys.path
sys.path.append(parent_dir)

import connection_restapi_client_poc
import connection_restapi_client_poc.ideastatica_client as ideastatica_client

baseUrl = "http://localhost:5000"

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = connection_restapi_client_poc.Configuration(
    host = baseUrl
)

dir_path = os.path.dirname(os.path.realpath(__file__))
project_file_path = os.path.join(dir_path, '..\projects', 'HSS_norm_cond.ideaCon')
print(project_file_path)


# Enter a context with an instance of the API client
with ideastatica_client.IdeaStatiCaClient(configuration, project_file_path) as is_client:

    try:
        # Get the project data
        project_data = is_client.api_project.get_project_data(is_client.project_id)
        pprint(project_data)

        # Get API for connections in the project
        api_connection = connection_restapi_client_poc.ConnectionApi(is_client.client)
  
        # Get list of all connections in the project
        connections_in_project = api_connection.get_all_connections_data(is_client.project_id)

        # first connection in the project 
        connection1 = connections_in_project[0]

        pprint(connection1)
        
            # get calculation API for the active project
        api_calculation = connection_restapi_client_poc.CalculationApi(is_client.client)

        # run stress-strain CBFEM analysis for the connection id = 1
        calcParams = connection_restapi_client_poc.ConCalculationParameter() # ConCalculationParameter | List of connections to calculate and a type of CBFEM analysis (optional)
        calcParams.connection_ids = [connection1.id]

        # run stress-strain analysis for the connection
        con1_cbfem_results = api_calculation.calculate(is_client.project_id, calcParams)
        pprint(con1_cbfem_results)

        # TODO - fix serialization JSON
        
        # # get detailed results
        # results_text = api_calculation.get_raw_json_results(is_client.project_id, calcParams)
        # #pprint(results_text)

        # raw_results = json.loads(results_text)
        # pprint(raw_results)

        detailed_results = api_calculation.get_results(is_client.project_id, calcParams)
        pprint(detailed_results)

        # get connection setup
        connection_setup =  is_client.api_project.get_setup(is_client.project_id)
        pprint(connection_setup)

        # modify setup
        connection_setup.hss_limit_plastic_strain = 0.02
        modifiedSetup = is_client.api_project.update_setup(is_client.project_id, connection_setup)

        # recalculate connection
        recalculate_results = api_calculation.calculate(is_client.project_id, calcParams)
        pprint(recalculate_results)

    except Exception as e:
        print("Operation failed : %s\n" % e)

