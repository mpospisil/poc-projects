/*
 * Connection Rest API 1.0
 *
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 1.0
 * Generated by: https://github.com/openapitools/openapi-generator.git
 */


using System;
using System.Collections.Generic;
using System.Collections.ObjectModel;
using System.Linq;
using System.Net;
using System.Net.Mime;
using connection_restapi_client_poc.Client;
using connection_restapi_client_poc.Model;

namespace connection_restapi_client_poc.Api
{

    /// <summary>
    /// Represents a collection of functions to interact with the API endpoints
    /// </summary>
    public interface IPresentationApiSync : IApiAccessor
    {
        #region Synchronous Operations
        /// <summary>
        /// Returns data for scene3D
        /// </summary>
        /// <exception cref="connection_restapi_client_poc.Client.ApiException">Thrown when fails to make API call</exception>
        /// <param name="projectId">The unique identifier of the open project in the ConnectionRestApi service</param>
        /// <param name="connectionId">Id of the connection to be presented to scene3D</param>
        /// <param name="operationIndex">Index associated with the operation.</param>
        /// <returns>DrawData</returns>
        DrawData GetDataScene3D(Guid projectId, int connectionId, int operationIndex = 0);

        /// <summary>
        /// Returns data for scene3D
        /// </summary>
        /// <remarks>
        /// 
        /// </remarks>
        /// <exception cref="connection_restapi_client_poc.Client.ApiException">Thrown when fails to make API call</exception>
        /// <param name="projectId">The unique identifier of the open project in the ConnectionRestApi service</param>
        /// <param name="connectionId">Id of the connection to be presented to scene3D</param>
        /// <param name="operationIndex">Index associated with the operation.</param>
        /// <returns>ApiResponse of DrawData</returns>
        ApiResponse<DrawData> GetDataScene3DWithHttpInfo(Guid projectId, int connectionId, int operationIndex = 0);
        #endregion Synchronous Operations
    }

    /// <summary>
    /// Represents a collection of functions to interact with the API endpoints
    /// </summary>
    public interface IPresentationApiAsync : IApiAccessor
    {
        #region Asynchronous Operations
        /// <summary>
        /// Returns data for scene3D
        /// </summary>
        /// <remarks>
        /// 
        /// </remarks>
        /// <exception cref="connection_restapi_client_poc.Client.ApiException">Thrown when fails to make API call</exception>
        /// <param name="projectId">The unique identifier of the open project in the ConnectionRestApi service</param>
        /// <param name="connectionId">Id of the connection to be presented to scene3D</param>
        /// <param name="operationIndex">Index associated with the operation.</param>
        /// <param name="cancellationToken">Cancellation Token to cancel the request.</param>
        /// <returns>Task of DrawData</returns>
        System.Threading.Tasks.Task<DrawData> GetDataScene3DAsync(Guid projectId, int connectionId, int operationIndex = 0, System.Threading.CancellationToken cancellationToken = default(global::System.Threading.CancellationToken));

        /// <summary>
        /// Returns data for scene3D
        /// </summary>
        /// <remarks>
        /// 
        /// </remarks>
        /// <exception cref="connection_restapi_client_poc.Client.ApiException">Thrown when fails to make API call</exception>
        /// <param name="projectId">The unique identifier of the open project in the ConnectionRestApi service</param>
        /// <param name="connectionId">Id of the connection to be presented to scene3D</param>
        /// <param name="operationIndex">Index associated with the operation.</param>
        /// <param name="cancellationToken">Cancellation Token to cancel the request.</param>
        /// <returns>Task of ApiResponse (DrawData)</returns>
        System.Threading.Tasks.Task<ApiResponse<DrawData>> GetDataScene3DWithHttpInfoAsync(Guid projectId, int connectionId, int operationIndex = 0, System.Threading.CancellationToken cancellationToken = default(global::System.Threading.CancellationToken));
        #endregion Asynchronous Operations
    }

    /// <summary>
    /// Represents a collection of functions to interact with the API endpoints
    /// </summary>
    public interface IPresentationApi : IPresentationApiSync, IPresentationApiAsync
    {

    }

    /// <summary>
    /// Represents a collection of functions to interact with the API endpoints
    /// </summary>
    public partial class PresentationApi : IPresentationApi
    {
        private connection_restapi_client_poc.Client.ExceptionFactory _exceptionFactory = (name, response) => null;

        /// <summary>
        /// Initializes a new instance of the <see cref="PresentationApi"/> class.
        /// </summary>
        /// <returns></returns>
        public PresentationApi() : this((string)null)
        {
        }

        /// <summary>
        /// Initializes a new instance of the <see cref="PresentationApi"/> class.
        /// </summary>
        /// <returns></returns>
        public PresentationApi(string basePath)
        {
            this.Configuration = connection_restapi_client_poc.Client.Configuration.MergeConfigurations(
                connection_restapi_client_poc.Client.GlobalConfiguration.Instance,
                new connection_restapi_client_poc.Client.Configuration { BasePath = basePath }
            );
            this.Client = new connection_restapi_client_poc.Client.ApiClient(this.Configuration.BasePath);
            this.AsynchronousClient = new connection_restapi_client_poc.Client.ApiClient(this.Configuration.BasePath);
            this.ExceptionFactory = connection_restapi_client_poc.Client.Configuration.DefaultExceptionFactory;
        }

        /// <summary>
        /// Initializes a new instance of the <see cref="PresentationApi"/> class
        /// using Configuration object
        /// </summary>
        /// <param name="configuration">An instance of Configuration</param>
        /// <returns></returns>
        public PresentationApi(connection_restapi_client_poc.Client.Configuration configuration)
        {
            if (configuration == null) throw new ArgumentNullException("configuration");

            this.Configuration = connection_restapi_client_poc.Client.Configuration.MergeConfigurations(
                connection_restapi_client_poc.Client.GlobalConfiguration.Instance,
                configuration
            );
            this.Client = new connection_restapi_client_poc.Client.ApiClient(this.Configuration.BasePath);
            this.AsynchronousClient = new connection_restapi_client_poc.Client.ApiClient(this.Configuration.BasePath);
            ExceptionFactory = connection_restapi_client_poc.Client.Configuration.DefaultExceptionFactory;
        }

        /// <summary>
        /// Initializes a new instance of the <see cref="PresentationApi"/> class
        /// using a Configuration object and client instance.
        /// </summary>
        /// <param name="client">The client interface for synchronous API access.</param>
        /// <param name="asyncClient">The client interface for asynchronous API access.</param>
        /// <param name="configuration">The configuration object.</param>
        public PresentationApi(connection_restapi_client_poc.Client.ISynchronousClient client, connection_restapi_client_poc.Client.IAsynchronousClient asyncClient, connection_restapi_client_poc.Client.IReadableConfiguration configuration)
        {
            if (client == null) throw new ArgumentNullException("client");
            if (asyncClient == null) throw new ArgumentNullException("asyncClient");
            if (configuration == null) throw new ArgumentNullException("configuration");

            this.Client = client;
            this.AsynchronousClient = asyncClient;
            this.Configuration = configuration;
            this.ExceptionFactory = connection_restapi_client_poc.Client.Configuration.DefaultExceptionFactory;
        }

        /// <summary>
        /// The client for accessing this underlying API asynchronously.
        /// </summary>
        public connection_restapi_client_poc.Client.IAsynchronousClient AsynchronousClient { get; set; }

        /// <summary>
        /// The client for accessing this underlying API synchronously.
        /// </summary>
        public connection_restapi_client_poc.Client.ISynchronousClient Client { get; set; }

        /// <summary>
        /// Gets the base path of the API client.
        /// </summary>
        /// <value>The base path</value>
        public string GetBasePath()
        {
            return this.Configuration.BasePath;
        }

        /// <summary>
        /// Gets or sets the configuration object
        /// </summary>
        /// <value>An instance of the Configuration</value>
        public connection_restapi_client_poc.Client.IReadableConfiguration Configuration { get; set; }

        /// <summary>
        /// Provides a factory method hook for the creation of exceptions.
        /// </summary>
        public connection_restapi_client_poc.Client.ExceptionFactory ExceptionFactory
        {
            get
            {
                if (_exceptionFactory != null && _exceptionFactory.GetInvocationList().Length > 1)
                {
                    throw new InvalidOperationException("Multicast delegate for ExceptionFactory is unsupported.");
                }
                return _exceptionFactory;
            }
            set { _exceptionFactory = value; }
        }

        /// <summary>
        /// Returns data for scene3D 
        /// </summary>
        /// <exception cref="connection_restapi_client_poc.Client.ApiException">Thrown when fails to make API call</exception>
        /// <param name="projectId">The unique identifier of the open project in the ConnectionRestApi service</param>
        /// <param name="connectionId">Id of the connection to be presented to scene3D</param>
        /// <param name="operationIndex">Index associated with the operation.</param>
        /// <returns>DrawData</returns>
        public DrawData GetDataScene3D(Guid projectId, int connectionId, int operationIndex = 0)
        {
            connection_restapi_client_poc.Client.ApiResponse<DrawData> localVarResponse = GetDataScene3DWithHttpInfo(projectId, connectionId);
            return localVarResponse.Data;
        }

        /// <summary>
        /// Returns data for scene3D 
        /// </summary>
        /// <exception cref="connection_restapi_client_poc.Client.ApiException">Thrown when fails to make API call</exception>
        /// <param name="projectId">The unique identifier of the open project in the ConnectionRestApi service</param>
        /// <param name="connectionId">Id of the connection to be presented to scene3D</param>
        /// <param name="operationIndex">Index associated with the operation.</param>
        /// <returns>ApiResponse of DrawData</returns>
        public connection_restapi_client_poc.Client.ApiResponse<DrawData> GetDataScene3DWithHttpInfo(Guid projectId, int connectionId, int operationIndex = 0)
        {
            connection_restapi_client_poc.Client.RequestOptions localVarRequestOptions = new connection_restapi_client_poc.Client.RequestOptions();

            string[] _contentTypes = new string[] {
            };

            // to determine the Accept header
            string[] _accepts = new string[] {
                "application/json"
            };

            var localVarContentType = connection_restapi_client_poc.Client.ClientUtils.SelectHeaderContentType(_contentTypes);
            if (localVarContentType != null)
            {
                localVarRequestOptions.HeaderParameters.Add("Content-Type", localVarContentType);
            }

            var localVarAccept = connection_restapi_client_poc.Client.ClientUtils.SelectHeaderAccept(_accepts);
            if (localVarAccept != null)
            {
                localVarRequestOptions.HeaderParameters.Add("Accept", localVarAccept);
            }

            localVarRequestOptions.PathParameters.Add("projectId", connection_restapi_client_poc.Client.ClientUtils.ParameterToString(projectId)); // path parameter
            localVarRequestOptions.PathParameters.Add("connectionId", connection_restapi_client_poc.Client.ClientUtils.ParameterToString(connectionId)); // path parameter

            localVarRequestOptions.Operation = "PresentationApi.GetDataScene3D";
            localVarRequestOptions.OperationIndex = operationIndex;


            // make the HTTP request
            var localVarResponse = this.Client.Get<DrawData>("/api/1/projects/{projectId}/connections/{connectionId}/presentation", localVarRequestOptions, this.Configuration);
            if (this.ExceptionFactory != null)
            {
                Exception _exception = this.ExceptionFactory("GetDataScene3D", localVarResponse);
                if (_exception != null)
                {
                    throw _exception;
                }
            }

            return localVarResponse;
        }

        /// <summary>
        /// Returns data for scene3D 
        /// </summary>
        /// <exception cref="connection_restapi_client_poc.Client.ApiException">Thrown when fails to make API call</exception>
        /// <param name="projectId">The unique identifier of the open project in the ConnectionRestApi service</param>
        /// <param name="connectionId">Id of the connection to be presented to scene3D</param>
        /// <param name="operationIndex">Index associated with the operation.</param>
        /// <param name="cancellationToken">Cancellation Token to cancel the request.</param>
        /// <returns>Task of DrawData</returns>
        public async System.Threading.Tasks.Task<DrawData> GetDataScene3DAsync(Guid projectId, int connectionId, int operationIndex = 0, System.Threading.CancellationToken cancellationToken = default(global::System.Threading.CancellationToken))
        {
            connection_restapi_client_poc.Client.ApiResponse<DrawData> localVarResponse = await GetDataScene3DWithHttpInfoAsync(projectId, connectionId, operationIndex, cancellationToken).ConfigureAwait(false);
            return localVarResponse.Data;
        }

        /// <summary>
        /// Returns data for scene3D 
        /// </summary>
        /// <exception cref="connection_restapi_client_poc.Client.ApiException">Thrown when fails to make API call</exception>
        /// <param name="projectId">The unique identifier of the open project in the ConnectionRestApi service</param>
        /// <param name="connectionId">Id of the connection to be presented to scene3D</param>
        /// <param name="operationIndex">Index associated with the operation.</param>
        /// <param name="cancellationToken">Cancellation Token to cancel the request.</param>
        /// <returns>Task of ApiResponse (DrawData)</returns>
        public async System.Threading.Tasks.Task<connection_restapi_client_poc.Client.ApiResponse<DrawData>> GetDataScene3DWithHttpInfoAsync(Guid projectId, int connectionId, int operationIndex = 0, System.Threading.CancellationToken cancellationToken = default(global::System.Threading.CancellationToken))
        {

            connection_restapi_client_poc.Client.RequestOptions localVarRequestOptions = new connection_restapi_client_poc.Client.RequestOptions();

            string[] _contentTypes = new string[] {
            };

            // to determine the Accept header
            string[] _accepts = new string[] {
                "application/json"
            };

            var localVarContentType = connection_restapi_client_poc.Client.ClientUtils.SelectHeaderContentType(_contentTypes);
            if (localVarContentType != null)
            {
                localVarRequestOptions.HeaderParameters.Add("Content-Type", localVarContentType);
            }

            var localVarAccept = connection_restapi_client_poc.Client.ClientUtils.SelectHeaderAccept(_accepts);
            if (localVarAccept != null)
            {
                localVarRequestOptions.HeaderParameters.Add("Accept", localVarAccept);
            }

            localVarRequestOptions.PathParameters.Add("projectId", connection_restapi_client_poc.Client.ClientUtils.ParameterToString(projectId)); // path parameter
            localVarRequestOptions.PathParameters.Add("connectionId", connection_restapi_client_poc.Client.ClientUtils.ParameterToString(connectionId)); // path parameter

            localVarRequestOptions.Operation = "PresentationApi.GetDataScene3D";
            localVarRequestOptions.OperationIndex = operationIndex;


            // make the HTTP request
            var localVarResponse = await this.AsynchronousClient.GetAsync<DrawData>("/api/1/projects/{projectId}/connections/{connectionId}/presentation", localVarRequestOptions, this.Configuration, cancellationToken).ConfigureAwait(false);

            if (this.ExceptionFactory != null)
            {
                Exception _exception = this.ExceptionFactory("GetDataScene3D", localVarResponse);
                if (_exception != null)
                {
                    throw _exception;
                }
            }

            return localVarResponse;
        }

    }
}
