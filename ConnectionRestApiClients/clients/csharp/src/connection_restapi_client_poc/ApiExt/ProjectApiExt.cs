﻿using connection_restapi_client_poc.Model;
using Newtonsoft.Json;
using System;
using System.Collections.Generic;
using System.IO;
using System.Net.Http;
using System.Text;
using System.Threading.Tasks;

namespace connection_restapi_client_poc.Api
{
	public interface IProjectApiExtAsync : IProjectApiAsync
	{
		Task DownloadProjectAsync(Guid projectId, string fileName);

		Task<ConProject> CreateProjectFromIomFileAsync(string iomFilePath);
	}


	public class ProjectApiExt : ProjectApi, IProjectApiExtAsync
	{
		/// <inheritdoc cref="ProjectApi.ProjectApi(connection_restapi_client_poc.Client.ISynchronousClient, connection_restapi_client_poc.Client.IAsynchronousClient, connection_restapi_client_poc.Client.IReadableConfiguration)"/>/>
		public ProjectApiExt(connection_restapi_client_poc.Client.ISynchronousClient client, connection_restapi_client_poc.Client.IAsynchronousClient asyncClient, connection_restapi_client_poc.Client.IReadableConfiguration configuration) : base(client, asyncClient, configuration)
		{
		}

		public async Task DownloadProjectAsync(Guid projectId, string fileName)
		{
			var response = await base.DownloadProjectWithHttpInfoAsync(projectId, "application/octet-stream");
			byte[] buffer = (byte[])response.Data;
			using (var fileStream = System.IO.File.Create(fileName))
			{
				await fileStream.WriteAsync(buffer, 0, buffer.Length);
			}
		}

		public async Task<ConProject> CreateProjectFromIomFileAsync(string fileName)
		{
			connection_restapi_client_poc.Client.RequestOptions localVarRequestOptions = new connection_restapi_client_poc.Client.RequestOptions();

			var localVarContentType = "application/xml";
			localVarRequestOptions.HeaderParameters.Add("Content-Type", localVarContentType);

			string localVarAccept = "application/json";
			localVarRequestOptions.HeaderParameters.Add("Accept", localVarAccept);


			//localVarRequestOptions.PathParameters.Add("projectId", connection_restapi_client_poc.Client.ClientUtils.ParameterToString(projectId)); // path parameter

			localVarRequestOptions.Operation = "ProjectApi.UpdateFromIOM";
			localVarRequestOptions.OperationIndex = 0;

			string xmlString = string.Empty;
#if NETSTANDARD2_1_OR_GREATER
			xmlString = await System.IO.File.ReadAllTextAsync(fileName);
#else
			xmlString = System.IO.File.ReadAllText(fileName);

#endif
			localVarRequestOptions.Data = xmlString;


			xmlString = xmlString.Replace("utf-16", "utf-8");
			var contentString = new StringContent(xmlString, encoding: Encoding.UTF8, "application/xml");

			//ConIomImportOptions 

			//if (connectionsToCreate != null)
			//{
			//	localVarRequestOptions.QueryParameters.Add(connection_restapi_client_poc.Client.ClientUtils.ParameterToMultiMap("multi", "ConnectionsToCreate", connectionsToCreate));
			//}

			localVarRequestOptions.QueryParameters.Add(connection_restapi_client_poc.Client.ClientUtils.ParameterToMultiMap("multi", "ConnectionsToCreate", new List<int>()));
			localVarRequestOptions.Data = contentString;

			localVarRequestOptions.Operation = "ProjectApi.ImportIOMContainer";


			// make the HTTP request
			var localVarResponse = this.Client.Post<ConProject>("/api/1/projects/import-iom", localVarRequestOptions, this.Configuration);
			if (this.ExceptionFactory != null)
			{
				Exception _exception = this.ExceptionFactory("ImportIOMContainer", localVarResponse);
				if (_exception != null)
				{
					throw _exception;
				}
			}

			return localVarResponse.Data;

		}

		/// <inheritdoc cref="ProjectApi.GetSetupAsync(Guid, int, System.Threading.CancellationToken)"/>
		public new async System.Threading.Tasks.Task<ConnectionSetup> GetSetupAsync(Guid projectId, int operationIndex = 0, System.Threading.CancellationToken cancellationToken = default(System.Threading.CancellationToken))
		{
				var response = await GetSetupWithHttpInfoAsync(projectId);
				var setup = JsonConvert.DeserializeObject<ConnectionSetup>(response.RawContent, IdeaJsonSerializerSetting.GetJsonSettingIdea());
				return setup;
		}

		/// <inheritdoc cref="ProjectApi.UpdateSetupAsync(Guid, ConnectionSetup, int, System.Threading.CancellationToken)"/>
		public new async System.Threading.Tasks.Task<ConnectionSetup> UpdateSetupAsync(Guid projectId, ConnectionSetup connectionSetup = default(ConnectionSetup), int operationIndex = 0, System.Threading.CancellationToken cancellationToken = default(System.Threading.CancellationToken))
		{

			connection_restapi_client_poc.Client.RequestOptions localVarRequestOptions = new connection_restapi_client_poc.Client.RequestOptions();

			var localVarContentType = "application/json";

			var localVarAccept = "application/json";

			localVarRequestOptions.HeaderParameters.Add("Content-Type", localVarContentType);

			localVarRequestOptions.HeaderParameters.Add("Accept", localVarAccept);

			localVarRequestOptions.PathParameters.Add("projectId", connection_restapi_client_poc.Client.ClientUtils.ParameterToString(projectId)); // path parameter
			localVarRequestOptions.Data = connectionSetup;

			localVarRequestOptions.Operation = "ProjectApi.UpdateSetup";
			localVarRequestOptions.OperationIndex = operationIndex;

			localVarRequestOptions.Data = JsonConvert.SerializeObject(connectionSetup, IdeaJsonSerializerSetting.GetJsonSettingIdea());

			// make the HTTP request
			var localVarResponse = await this.AsynchronousClient.PutAsync<ConnectionSetup>("/api/1/projects/{projectId}/connection-setup", localVarRequestOptions, this.Configuration, cancellationToken).ConfigureAwait(false);

			if (this.ExceptionFactory != null)
			{
				Exception _exception = this.ExceptionFactory("UpdateSetup", localVarResponse);
				if (_exception != null)
				{
					throw _exception;
				}
			}

			var setup = JsonConvert.DeserializeObject<ConnectionSetup>(localVarResponse.RawContent, IdeaJsonSerializerSetting.GetJsonSettingIdea());
			return setup;
		}
	}
}
