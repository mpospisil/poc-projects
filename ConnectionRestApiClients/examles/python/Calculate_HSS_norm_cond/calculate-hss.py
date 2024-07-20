import connection_restapi_client_poc
from connection_restapi_client_poc.rest import ApiException
from pprint import pprint
import os
import requests
from urllib.parse import urljoin


baseUrl = "http://localhost:5193"

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
            open_project_data = api_project.api1_projects_project_id_project_data_get(project_id)
            pprint(open_project_data)


            
        finally:
            closeProjectResult = api_project.api1_projects_project_id_close_get(project_id)

    except Exception as e:
        print("Exception when calling ProjectApi->api1_connect_client_get: %s\n" % e)