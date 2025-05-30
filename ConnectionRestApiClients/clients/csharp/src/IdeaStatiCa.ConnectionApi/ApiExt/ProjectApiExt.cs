﻿using IdeaStatiCa.ConnectionApi.Model;
using Newtonsoft.Json;
using System;
using System.Collections.Generic;
using System.Net.Http;
using System.Text;
using System.Threading.Tasks;

namespace IdeaStatiCa.ConnectionApi.Api
{
	public interface IProjectApiExtAsync : IProjectApiAsync
	{
		/// <summary>
		/// 
		/// </summary>
		Guid ProjectId { get; }

		/// <summary>
		/// 
		/// </summary>
		ConProject ActiveProject { get; }

		/// <summary>
		/// 
		/// </summary>
		/// <param name="filePath"></param>
		/// <returns></returns>
		Task<ConProject> OpenProjectAsync(string filePath);

		Task SaveProjectAsync(Guid projectId, string fileName);

		/// <summary>
		/// 
		/// </summary>
		/// <param name="iomFilePath"></param>
		/// <param name="connectionsToCreate"></param>
		/// <returns></returns>
		Task<ConProject> CreateProjectFromIomFileAsync(string iomFilePath, List<int> connectionsToCreate = null);
	}

	/// <summary>
	/// 
	/// </summary>
	public class ProjectApiExt : ProjectApi, IProjectApiExtAsync
	{
		private readonly IConnectionApiClient _connectionApiClient;

		public ProjectApiExt(IConnectionApiClient connectionApiClient, IdeaStatiCa.ConnectionApi.Client.ISynchronousClient client, IdeaStatiCa.ConnectionApi.Client.IAsynchronousClient asyncClient, IdeaStatiCa.ConnectionApi.Client.IReadableConfiguration configuration) : base(client, asyncClient, configuration)
		{
			this._connectionApiClient = connectionApiClient;
		}


		/// <inheritdoc cref="IConnectionApiClient.ProjectId"/>/>
		public Guid ProjectId
		{
			get => ActiveProject == null ? Guid.Empty : ActiveProject.ProjectId;
		}

		/// <summary>
		/// Data about the active project
		/// </summary>
		public ConProject ActiveProject { get; private set; } = null;

		public async Task<ConProject> OpenProjectAsync(string path)
		{

			using (var fs = new System.IO.FileStream(path, System.IO.FileMode.Open))
			{
				using (var ms = new System.IO.MemoryStream())
				{
					await fs.CopyToAsync(ms);
					ms.Seek(0, System.IO.SeekOrigin.Begin);
					var conProject = await OpenProjectAsync(ms);
					this.ActiveProject = conProject;
				}
			}

			return this.ActiveProject;
		}


		public async Task SaveProjectAsync(Guid projectId, string fileName)
		{
			var response = await base.DownloadProjectWithHttpInfoAsync(projectId, "application/octet-stream");
			byte[] buffer = (byte[])response.Data;
			using (var fileStream = System.IO.File.Create(fileName))
			{
				await fileStream.WriteAsync(buffer, 0, buffer.Length);
			}
		}

		public async Task<ConProject> CreateProjectFromIomFileAsync(string fileName, List<int> connectionsToCreate = null)
		{
			IdeaStatiCa.ConnectionApi.Client.RequestOptions localVarRequestOptions = new IdeaStatiCa.ConnectionApi.Client.RequestOptions();

			var localVarContentType = "application/xml";
			localVarRequestOptions.HeaderParameters.Add("Content-Type", localVarContentType);

			string localVarAccept = "application/json";
			localVarRequestOptions.HeaderParameters.Add("Accept", localVarAccept);


			//localVarRequestOptions.PathParameters.Add("projectId", IdeaStatiCa.ConnectionApi.Client.ClientUtils.ParameterToString(projectId)); // path parameter

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



			//if (connectionsToCreate != null)
			//{
			//	localVarRequestOptions.QueryParameters.Add(IdeaStatiCa.ConnectionApi.Client.ClientUtils.ParameterToMultiMap("multi", "ConnectionsToCreate", connectionsToCreate));
			//}
			if (connectionsToCreate == null)
				connectionsToCreate = new List<int>();

			localVarRequestOptions.QueryParameters.Add(IdeaStatiCa.ConnectionApi.Client.ClientUtils.ParameterToMultiMap("multi", "ConnectionsToCreate", connectionsToCreate));
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

			ActiveProject = localVarResponse.Data;
            return ActiveProject;
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

			IdeaStatiCa.ConnectionApi.Client.RequestOptions localVarRequestOptions = new IdeaStatiCa.ConnectionApi.Client.RequestOptions();

			var localVarContentType = "application/json";

			var localVarAccept = "application/json";

			localVarRequestOptions.HeaderParameters.Add("Content-Type", localVarContentType);

			localVarRequestOptions.HeaderParameters.Add("Accept", localVarAccept);

			localVarRequestOptions.PathParameters.Add("projectId", IdeaStatiCa.ConnectionApi.Client.ClientUtils.ParameterToString(projectId)); // path parameter
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
