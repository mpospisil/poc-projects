# coding: utf-8

"""
    Connection Rest API 1.0

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

import warnings
from pydantic import validate_call, Field, StrictFloat, StrictStr, StrictInt
from typing import Any, Dict, List, Optional, Tuple, Union
from typing_extensions import Annotated

from pydantic import Field, StrictInt, StrictStr
from typing import Any, Dict, Optional
from typing_extensions import Annotated
from connection_restapi_client_poc.models.idea_stati_ca_api_connection_model_con_template_apply_param_idea_stati_ca_api import IdeaStatiCaApiConnectionModelConTemplateApplyParamIdeaStatiCaApi
from connection_restapi_client_poc.models.idea_stati_ca_api_connection_model_con_template_mapping_get_param_idea_stati_ca_api import IdeaStatiCaApiConnectionModelConTemplateMappingGetParamIdeaStatiCaApi
from connection_restapi_client_poc.models.idea_stati_ca_api_connection_model_template_conversions_idea_stati_ca_api import IdeaStatiCaApiConnectionModelTemplateConversionsIdeaStatiCaApi

from connection_restapi_client_poc.api_client import ApiClient, RequestSerialized
from connection_restapi_client_poc.api_response import ApiResponse
from connection_restapi_client_poc.rest import RESTResponseType


class TemplateApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client


    @validate_call
    def api1_projects_project_id_connections_connection_id_apply_mapping_post(
        self,
        project_id: Annotated[StrictStr, Field(description="The unique identifier of the opened connection in the ConnectionReastApi service")],
        connection_id: Annotated[StrictInt, Field(description="Id of the connection to apply the template")],
        idea_stati_ca_api_connection_model_con_template_mapping_get_param_idea_stati_ca_api: Annotated[Optional[IdeaStatiCaApiConnectionModelConTemplateMappingGetParamIdeaStatiCaApi], Field(description="Data of the template to apply")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> IdeaStatiCaApiConnectionModelTemplateConversionsIdeaStatiCaApi:
        """Get the default mappings for the application of the connection template passed in conTemplateGetParam  on connectionId in the project projectId

        The result IdeaStatiCa.Api.Connection.Model.TemplateConversions can be modified by a user and used for the application of a template M:IdeaStatiCa.ConnectionRestApi.Controllers.TemplateController.ApplyConnectionTemplateAsync(System.Guid,System.Int32,IdeaStatiCa.Api.Connection.Model.ConTemplateApplyParam) method.

        :param project_id: The unique identifier of the opened connection in the ConnectionReastApi service (required)
        :type project_id: str
        :param connection_id: Id of the connection to apply the template (required)
        :type connection_id: int
        :param idea_stati_ca_api_connection_model_con_template_mapping_get_param_idea_stati_ca_api: Data of the template to apply
        :type idea_stati_ca_api_connection_model_con_template_mapping_get_param_idea_stati_ca_api: IdeaStatiCaApiConnectionModelConTemplateMappingGetParamIdeaStatiCaApi
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api1_projects_project_id_connections_connection_id_apply_mapping_post_serialize(
            project_id=project_id,
            connection_id=connection_id,
            idea_stati_ca_api_connection_model_con_template_mapping_get_param_idea_stati_ca_api=idea_stati_ca_api_connection_model_con_template_mapping_get_param_idea_stati_ca_api,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "IdeaStatiCaApiConnectionModelTemplateConversionsIdeaStatiCaApi",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def api1_projects_project_id_connections_connection_id_apply_mapping_post_with_http_info(
        self,
        project_id: Annotated[StrictStr, Field(description="The unique identifier of the opened connection in the ConnectionReastApi service")],
        connection_id: Annotated[StrictInt, Field(description="Id of the connection to apply the template")],
        idea_stati_ca_api_connection_model_con_template_mapping_get_param_idea_stati_ca_api: Annotated[Optional[IdeaStatiCaApiConnectionModelConTemplateMappingGetParamIdeaStatiCaApi], Field(description="Data of the template to apply")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[IdeaStatiCaApiConnectionModelTemplateConversionsIdeaStatiCaApi]:
        """Get the default mappings for the application of the connection template passed in conTemplateGetParam  on connectionId in the project projectId

        The result IdeaStatiCa.Api.Connection.Model.TemplateConversions can be modified by a user and used for the application of a template M:IdeaStatiCa.ConnectionRestApi.Controllers.TemplateController.ApplyConnectionTemplateAsync(System.Guid,System.Int32,IdeaStatiCa.Api.Connection.Model.ConTemplateApplyParam) method.

        :param project_id: The unique identifier of the opened connection in the ConnectionReastApi service (required)
        :type project_id: str
        :param connection_id: Id of the connection to apply the template (required)
        :type connection_id: int
        :param idea_stati_ca_api_connection_model_con_template_mapping_get_param_idea_stati_ca_api: Data of the template to apply
        :type idea_stati_ca_api_connection_model_con_template_mapping_get_param_idea_stati_ca_api: IdeaStatiCaApiConnectionModelConTemplateMappingGetParamIdeaStatiCaApi
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api1_projects_project_id_connections_connection_id_apply_mapping_post_serialize(
            project_id=project_id,
            connection_id=connection_id,
            idea_stati_ca_api_connection_model_con_template_mapping_get_param_idea_stati_ca_api=idea_stati_ca_api_connection_model_con_template_mapping_get_param_idea_stati_ca_api,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "IdeaStatiCaApiConnectionModelTemplateConversionsIdeaStatiCaApi",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def api1_projects_project_id_connections_connection_id_apply_mapping_post_without_preload_content(
        self,
        project_id: Annotated[StrictStr, Field(description="The unique identifier of the opened connection in the ConnectionReastApi service")],
        connection_id: Annotated[StrictInt, Field(description="Id of the connection to apply the template")],
        idea_stati_ca_api_connection_model_con_template_mapping_get_param_idea_stati_ca_api: Annotated[Optional[IdeaStatiCaApiConnectionModelConTemplateMappingGetParamIdeaStatiCaApi], Field(description="Data of the template to apply")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Get the default mappings for the application of the connection template passed in conTemplateGetParam  on connectionId in the project projectId

        The result IdeaStatiCa.Api.Connection.Model.TemplateConversions can be modified by a user and used for the application of a template M:IdeaStatiCa.ConnectionRestApi.Controllers.TemplateController.ApplyConnectionTemplateAsync(System.Guid,System.Int32,IdeaStatiCa.Api.Connection.Model.ConTemplateApplyParam) method.

        :param project_id: The unique identifier of the opened connection in the ConnectionReastApi service (required)
        :type project_id: str
        :param connection_id: Id of the connection to apply the template (required)
        :type connection_id: int
        :param idea_stati_ca_api_connection_model_con_template_mapping_get_param_idea_stati_ca_api: Data of the template to apply
        :type idea_stati_ca_api_connection_model_con_template_mapping_get_param_idea_stati_ca_api: IdeaStatiCaApiConnectionModelConTemplateMappingGetParamIdeaStatiCaApi
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api1_projects_project_id_connections_connection_id_apply_mapping_post_serialize(
            project_id=project_id,
            connection_id=connection_id,
            idea_stati_ca_api_connection_model_con_template_mapping_get_param_idea_stati_ca_api=idea_stati_ca_api_connection_model_con_template_mapping_get_param_idea_stati_ca_api,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "IdeaStatiCaApiConnectionModelTemplateConversionsIdeaStatiCaApi",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _api1_projects_project_id_connections_connection_id_apply_mapping_post_serialize(
        self,
        project_id,
        connection_id,
        idea_stati_ca_api_connection_model_con_template_mapping_get_param_idea_stati_ca_api,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[str, Union[str, bytes]] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if project_id is not None:
            _path_params['projectId'] = project_id
        if connection_id is not None:
            _path_params['connectionId'] = connection_id
        # process the query parameters
        # process the header parameters
        # process the form parameters
        # process the body parameter
        if idea_stati_ca_api_connection_model_con_template_mapping_get_param_idea_stati_ca_api is not None:
            _body_params = idea_stati_ca_api_connection_model_con_template_mapping_get_param_idea_stati_ca_api


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json'
                ]
            )

        # set the HTTP header `Content-Type`
        if _content_type:
            _header_params['Content-Type'] = _content_type
        else:
            _default_content_type = (
                self.api_client.select_header_content_type(
                    [
                        'application/xml', 
                        'text/xml', 
                        'application/*+xml', 
                        'application/json-patch+json', 
                        'application/json', 
                        'text/json', 
                        'application/*+json'
                    ]
                )
            )
            if _default_content_type is not None:
                _header_params['Content-Type'] = _default_content_type

        # authentication setting
        _auth_settings: List[str] = [
        ]

        return self.api_client.param_serialize(
            method='POST',
            resource_path='/api/1/projects/{projectId}/connections/{connectionId}/apply-mapping',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def api1_projects_project_id_connections_connection_id_apply_template_post(
        self,
        project_id: StrictStr,
        connection_id: StrictInt,
        idea_stati_ca_api_connection_model_con_template_apply_param_idea_stati_ca_api: Optional[IdeaStatiCaApiConnectionModelConTemplateApplyParamIdeaStatiCaApi] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> object:
        """api1_projects_project_id_connections_connection_id_apply_template_post


        :param project_id: (required)
        :type project_id: str
        :param connection_id: (required)
        :type connection_id: int
        :param idea_stati_ca_api_connection_model_con_template_apply_param_idea_stati_ca_api:
        :type idea_stati_ca_api_connection_model_con_template_apply_param_idea_stati_ca_api: IdeaStatiCaApiConnectionModelConTemplateApplyParamIdeaStatiCaApi
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api1_projects_project_id_connections_connection_id_apply_template_post_serialize(
            project_id=project_id,
            connection_id=connection_id,
            idea_stati_ca_api_connection_model_con_template_apply_param_idea_stati_ca_api=idea_stati_ca_api_connection_model_con_template_apply_param_idea_stati_ca_api,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "object",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def api1_projects_project_id_connections_connection_id_apply_template_post_with_http_info(
        self,
        project_id: StrictStr,
        connection_id: StrictInt,
        idea_stati_ca_api_connection_model_con_template_apply_param_idea_stati_ca_api: Optional[IdeaStatiCaApiConnectionModelConTemplateApplyParamIdeaStatiCaApi] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[object]:
        """api1_projects_project_id_connections_connection_id_apply_template_post


        :param project_id: (required)
        :type project_id: str
        :param connection_id: (required)
        :type connection_id: int
        :param idea_stati_ca_api_connection_model_con_template_apply_param_idea_stati_ca_api:
        :type idea_stati_ca_api_connection_model_con_template_apply_param_idea_stati_ca_api: IdeaStatiCaApiConnectionModelConTemplateApplyParamIdeaStatiCaApi
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api1_projects_project_id_connections_connection_id_apply_template_post_serialize(
            project_id=project_id,
            connection_id=connection_id,
            idea_stati_ca_api_connection_model_con_template_apply_param_idea_stati_ca_api=idea_stati_ca_api_connection_model_con_template_apply_param_idea_stati_ca_api,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "object",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def api1_projects_project_id_connections_connection_id_apply_template_post_without_preload_content(
        self,
        project_id: StrictStr,
        connection_id: StrictInt,
        idea_stati_ca_api_connection_model_con_template_apply_param_idea_stati_ca_api: Optional[IdeaStatiCaApiConnectionModelConTemplateApplyParamIdeaStatiCaApi] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """api1_projects_project_id_connections_connection_id_apply_template_post


        :param project_id: (required)
        :type project_id: str
        :param connection_id: (required)
        :type connection_id: int
        :param idea_stati_ca_api_connection_model_con_template_apply_param_idea_stati_ca_api:
        :type idea_stati_ca_api_connection_model_con_template_apply_param_idea_stati_ca_api: IdeaStatiCaApiConnectionModelConTemplateApplyParamIdeaStatiCaApi
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api1_projects_project_id_connections_connection_id_apply_template_post_serialize(
            project_id=project_id,
            connection_id=connection_id,
            idea_stati_ca_api_connection_model_con_template_apply_param_idea_stati_ca_api=idea_stati_ca_api_connection_model_con_template_apply_param_idea_stati_ca_api,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "object",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _api1_projects_project_id_connections_connection_id_apply_template_post_serialize(
        self,
        project_id,
        connection_id,
        idea_stati_ca_api_connection_model_con_template_apply_param_idea_stati_ca_api,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[str, Union[str, bytes]] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if project_id is not None:
            _path_params['projectId'] = project_id
        if connection_id is not None:
            _path_params['connectionId'] = connection_id
        # process the query parameters
        # process the header parameters
        # process the form parameters
        # process the body parameter
        if idea_stati_ca_api_connection_model_con_template_apply_param_idea_stati_ca_api is not None:
            _body_params = idea_stati_ca_api_connection_model_con_template_apply_param_idea_stati_ca_api


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json'
                ]
            )

        # set the HTTP header `Content-Type`
        if _content_type:
            _header_params['Content-Type'] = _content_type
        else:
            _default_content_type = (
                self.api_client.select_header_content_type(
                    [
                        'application/json-patch+json', 
                        'application/json', 
                        'text/json', 
                        'application/*+json'
                    ]
                )
            )
            if _default_content_type is not None:
                _header_params['Content-Type'] = _default_content_type

        # authentication setting
        _auth_settings: List[str] = [
        ]

        return self.api_client.param_serialize(
            method='POST',
            resource_path='/api/1/projects/{projectId}/connections/{connectionId}/apply-template',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )


