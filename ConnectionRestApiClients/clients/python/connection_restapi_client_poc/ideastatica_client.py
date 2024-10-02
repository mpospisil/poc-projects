from ast import Param
from connection_restapi_client_poc import Configuration, ProjectApi, ClientApi, CalculationApi, ConnectionApi, ExportApi, LoadEffectApi, MaterialApi, MemberApi, OperationApi, PresentationApi, ReportApi, TemplateApi, ParameterApi
import connection_restapi_client_poc.api_client as api_client
from connection_restapi_client_poc.python_client_extensions import ExtendedProjectApi  # Import the extended class
from typing import Optional

class IdeaStatiCaClient:
    def __init__(self, configuration: Configuration):
        #self.fileName = fileName
        self.configuration = configuration
        self.client: Optional[api_client.ApiClient] = None
        
        #self.project_id: Optional[str] = None
        
        self.client_id: Optional[str] = None

        # Add all API controllers as None initially
        # Initialize API controllers as None initially
        self._projects: Optional[ExtendedProjectApi] = None
        self._connections: Optional[ConnectionApi] = None
        self._calculations: Optional[CalculationApi] = None
        self._exports: Optional[ExportApi] = None
        self._load_effects: Optional[LoadEffectApi] = None
        self._materials: Optional[MaterialApi] = None
        self._members: Optional[MemberApi] = None
        self._operations: Optional[OperationApi] = None
        self._presentations: Optional[PresentationApi] = None
        self._reports: Optional[ReportApi] = None
        self._templates: Optional[TemplateApi] = None
        self._parameters: Optional[ParameterApi] = None

    def __enter__(self):
        # Initialize the client with the provided config
        self.client = api_client.ApiClient(self.configuration)

        client_api = ClientApi(self.client)
        self.client_id = client_api.connect_client()

        # Add your ClientId to HTTP header
        self.client.default_headers['ClientId'] = self.client_id        

        # Initialize all the API controllers
        self._projects = ExtendedProjectApi(self.client)
        self._connections = ConnectionApi(self.client)
        self._calculations = CalculationApi(self.client)
        self._exports = ExportApi(self.client)
        self._load_effects = LoadEffectApi(self.client)
        self._materials = MaterialApi(self.client)
        self._members = MemberApi(self.client)
        self._operations = OperationApi(self.client)
        self._presentations = PresentationApi(self.client)
        self._reports = ReportApi(self.client)
        self._templates = TemplateApi(self.client)
        self._parameters = ParameterApi(self.client)

        # Override the default Content-Type for this specific call
        #uploadRes = self.api_project.open_project(idea_con_file=byte_array, _content_type='multipart/form-data')
        #self.project_id = uploadRes.project_id

        return self

    def __exit__(self, exc_type, exc_value, traceback):
        # Perform any necessary cleanup
            # Perform any necessary cleanup
        try:
            # Clean up all the API controllers
            self._projects = None
            self._connections = None
            self._calculations = None
            self._exports = None
            self._load_effects = None
            self._materials = None
            self._members = None
            self._operations = None
            self._presentations = None
            self._reports = None
            self._templates = None
            self._parameters = None
        finally:
            # Ensure that the client is properly cleaned up
            if self.client:
                self.client = None

    # Properties to expose the APIs with friendly names
    @property
    def projects(self):
        if self._projects is None:
            raise RuntimeError("Projects API is not initialized.")
        return self._projects

    @property
    def connections(self):
        if self._connections is None:
            raise RuntimeError("Connections API is not initialized.")
        return self._connections

    @property
    def calculations(self):
        if self._calculations is None:
            raise RuntimeError("Calculations API is not initialized.")
        return self._calculations

    @property
    def exports(self):
        if self._exports is None:
            raise RuntimeError("Exports API is not initialized.")
        return self._exports

    @property
    def load_effects(self):
        if self._load_effects is None:
            raise RuntimeError("Load Effects API is not initialized.")
        return self._load_effects

    @property
    def materials(self):
        if self._materials is None:
            raise RuntimeError("Materials API is not initialized.")
        return self._materials

    @property
    def members(self):
        if self._members is None:
            raise RuntimeError("Members API is not initialized.")
        return self._members

    @property
    def operations(self):
        if self._operations is None:
            raise RuntimeError("Operations API is not initialized.")
        return self._operations

    @property
    def presentations(self):
        if self._presentations is None:
            raise RuntimeError("Presentations API is not initialized.")
        return self._presentations

    @property
    def reports(self):
        if self._reports is None:
            raise RuntimeError("Reports API is not initialized.")
        return self._reports

    @property
    def templates(self):
        if self._templates is None:
            raise RuntimeError("Templates API is not initialized.")
        return self._templates
    
    @property
    def parameters(self):
        if self._parameters is None:
            raise RuntimeError("Parameters API is not initialized.")
        return self._parameters