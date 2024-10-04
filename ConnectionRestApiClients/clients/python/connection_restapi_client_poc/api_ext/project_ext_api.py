import logging
from connection_restapi_client_poc.api.project_api import ProjectApi

logger = logging.getLogger(__name__)

class ProjectExtApi(ProjectApi):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add any additional initialization here

