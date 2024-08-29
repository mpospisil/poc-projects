import connection_restapi_client_poc
from connection_restapi_client_poc.rest import ApiException
from pprint import pprint
from urllib.parse import urljoin
import requests
import os
# Verify that your service is running on following URL
baseUrl = "http://localhost:5000"

dir_path = os.path.dirname(os.path.realpath(__file__))
project_file_path = os.path.join(dir_path, 'simple-project.ideaCon')
print(project_file_path)

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = connection_restapi_client_poc.Configuration(
    host = baseUrl
)

# Enter a context with an instance of the API client
with connection_restapi_client_poc.ApiClient(configuration) as api_client:
    # Create an instance of the API class
        
    api_instance = connection_restapi_client_poc.ProjectApi(api_client)
    clientId = api_instance.connect_client() 
    api_client.default_headers['ClientId'] = clientId
    
    with open(project_file_path, 'rb') as file:
        byte_array = file.read()
    
    uploadRes = api_instance.upload_idea_con(idea_con_file=byte_array, _content_type='multipart/form-data')
    project_id = uploadRes.project_id
        
    con_calculation_parameter = connection_restapi_client_poc.ConCalculationParameter()
    con_calculation_parameter.connection_ids = [1]
    
    report_instance = connection_restapi_client_poc.ReportApi(api_client)
    calculation_instance = connection_restapi_client_poc.CalculationApi(api_client)

    try:
        # Run CBFEM caluclation and return the summary of the results
        api_response = calculation_instance.calculate(project_id, con_calculation_parameter)
        print("The response of CalculationApi->calculate:\n")
        pprint(api_response)      
                
        # will be solved in bug
        reportPdf = report_instance.generate_pdf(project_id, 1)
        with open('output.pdf', 'wb') as file:
            file.write(reportPdf.content)
            
        pprint('PDF file saved successfully as output.pdf')
        
    except ApiException as e:
        print("Exception when calling CalculationApi->calculate: %s\n" % e)