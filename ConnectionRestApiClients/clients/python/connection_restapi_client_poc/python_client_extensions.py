# python_client_extensions.py

from connection_restapi_client_poc import ProjectApi
import os

class ExtendedProjectApi(ProjectApi):
    def open_project_from_file(self, file_path: str):
        """Open a project using just the file path."""
        if not os.path.isfile(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")

        with open(file_path, 'rb') as file:
            byte_array = file.read()

        upload_res = self.open_project(idea_con_file=byte_array, _content_type='multipart/form-data')
        return upload_res