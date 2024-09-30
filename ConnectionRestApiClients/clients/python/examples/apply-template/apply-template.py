import sys
import os
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
project_file_path = os.path.join(dir_path, '..\projects', 'corner-empty.ideaCon')
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
        
        api_template = connection_restapi_client_poc.TemplateApi(is_client.client)

        templateParam =  connection_restapi_client_poc.ConTemplateMappingGetParam() # ConTemplateMappingGetParam | Data of the template to get default mapping (optional)

        template_file_name = os.path.join(dir_path, '..\projects', 'template-I-corner.contemp')
        with open(template_file_name, 'r', encoding='utf-16') as file:
            templateParam.template = file.read()

        # get the default mapping for the selected template and connection  
        default_mapping = api_template.get_default_template_mapping(is_client.project_id, connection1.id, templateParam)
        pprint(default_mapping)

        # TODO
        # Modify mapping

        # Apply the template to the connection with the modified mapping
        applyTemplateData =  connection_restapi_client_poc.ConTemplateApplyParam() # ConTemplateApplyParam | Template to apply (optional)
        applyTemplateData.connection_template = templateParam.template
        applyTemplateData.mapping = default_mapping

        applyTemplateResult = api_template.apply_template(is_client.project_id, connection1.id, applyTemplateData)

        pprint(applyTemplateResult)

        # get calculation API for the active project
        api_calculation = connection_restapi_client_poc.CalculationApi(is_client.client)            

        # run stress-strain CBFEM analysis for the connection id = 1
        calcParams =  connection_restapi_client_poc.ConCalculationParameter() # ConCalculationParameter | List of connections to calculate and a type of CBFEM analysis (optional)
        calcParams.connection_ids = [connection1.id]

        # run stress-strain analysis for the connection
        con1_cbfem_results1 = api_calculation.calculate(is_client.project_id, calcParams)
        pprint(con1_cbfem_results1)

    except Exception as e:
        print("Operation failed : %s\n" % e)



