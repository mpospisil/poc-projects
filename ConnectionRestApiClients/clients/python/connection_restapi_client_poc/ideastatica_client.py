from connection_restapi_client_poc import Configuration, ClientApi, CalculationApi, TemplateApi, ConnectionApi, ReportApi
import connection_restapi_client_poc.api_client as api_client
import connection_restapi_client_poc.api.project_ext_api as project_ext_api
from typing import Optional

class IdeaStatiCaClient:
    def __init__(self, configuration: Configuration, fileName: str):
        self.fileName = fileName
        self.configuration = configuration
        self.client: Optional[api_client.ApiClient] = None
        self.project_id: Optional[str] = None
        self.client_id: Optional[str] = None
        self.project: Optional[project_ext_api.ProjectExtApi] = None
        self.calculation: Optional[CalculationApi] = None
        self.template: Optional[TemplateApi] = None
        self.connection: Optional[ConnectionApi] = None
        self.report: Optional[ReportApi] = None

    def __enter__(self):
        with open(self.fileName, 'rb') as file:
            byte_array = file.read()

        # Initialize the client with the provided config
        self.client = api_client.ApiClient(self.configuration)

        client_api = ClientApi(self.client)
        self.client_id = client_api.connect_client()

        # Add your ClientId to HTTP header
        self.client.default_headers['ClientId'] = self.client_id        

        self.project = project_ext_api.ProjectExtApi(self.client)
        self.calculation = CalculationApi(self.client)
        self.template = TemplateApi(self.client)
        self.connection = ConnectionApi(self.client)
        self.report = ReportApi(self.client)

        # Override the default Content-Type for this specific call
        uploadRes = self.project.open_project(idea_con_file=byte_array, _content_type='multipart/form-data')
        self.project_id = uploadRes.project_id

        return self

    def __exit__(self, exc_type, exc_value, traceback):
        # Perform any necessary cleanup
        try:
            if self.project:
                self.project.close_project(self.project_id)
                self.project = None
        finally:
            self.project = None