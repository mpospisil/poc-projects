import webserviceapi_client
from webserviceapi_client.rest import ApiException
from pprint import pprint
import os

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webserviceapi_client.Configuration(
    host = "http://localhost:5258"
)


dir_path = os.path.dirname(os.path.realpath(__file__))
project_file_path = os.path.join(dir_path, 'HSS_norm_cond.ideaCon')
print(project_file_path)

with open(project_file_path, 'rb') as file:
    byte_array = file.read()


# Enter a context with an instance of the API client
with webserviceapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webserviceapi_client.ServiceApiApi(api_client)
    file = None # bytearray |  (optional)

    try:
        res = api_instance.api_service_api_upload_post(file=byte_array)
        print(res)
        
    except Exception as e:
        print("Exception when calling ServiceApiApi->api_service_api_upload_post: %s\n" % e)