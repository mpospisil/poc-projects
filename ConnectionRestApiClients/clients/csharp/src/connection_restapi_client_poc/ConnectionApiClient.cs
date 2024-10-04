﻿using connection_restapi_client_poc.Api;
using connection_restapi_client_poc.Client;
using connection_restapi_client_poc.Model;
using System;
using System.Threading.Tasks;

namespace connection_restapi_client_poc
{
	public class ConnectionApiClient : IConnectionApiClient
	{
		private bool disposedValue;
		

		/// <summary>
		/// 
		/// </summary>
		public Uri BasePath { get; private set; }

		/// <summary>
		/// 
		/// </summary>
		public string ClientId { get; private set; }
		public Guid ProjectId { get; private set; } = Guid.Empty;

		public ConProject ActiveProject { get; private set; } = null;

		/// <summary>
		/// 
		/// </summary>
		public IClientApi ClientApi { get; private set; }

		public ICalculationApiAsync Calculation { get; private set; }
		public IConnectionApiAsync Connection { get; private set; }
		public IExportApiAsync Export { get; private set; }
		public ILoadEffectApiAsync LoadEffect { get; private set; }
		public IMaterialApiAsync Material { get; private set; }
		public IMemberApiAsync Member { get; private set; }
		public IOperationApiAsync Operation { get; private set; }
		public IParameterApiAsync Parameter { get; private set; }
		public IPresentationApiAsync Presentation { get; private set; }
		public IProjectApiAsync Project { get; private set; }
		public IReportApiAsync Report { get; private set; }
		public ITemplateApiAsync Template { get; private set; }

		/// <summary>
		/// 
		/// </summary>
		/// <param name="basePath"></param>
		public ConnectionApiClient(string basePath)
		{
			BasePath = new Uri(basePath);
		}

		public async Task<ConProject> OpenProjectAsync(string path)
		{
			if(ClientApi != null)
			{
				throw new Exception("Client is already connected");
			}

			await CreateClientAsync();

			using(var fs = new System.IO.FileStream(path, System.IO.FileMode.Open))
			{
				using(var ms = new System.IO.MemoryStream())
				{
					await fs.CopyToAsync(ms);
					ms.Seek(0, System.IO.SeekOrigin.Begin);
					var conProject = await this.Project.OpenProjectAsync(ms);
					this.ActiveProject = conProject;
					this.ProjectId = conProject.ProjectId;
				}
			}

			return this.ActiveProject;
		}

		private async Task CloseAsync()
		{
			if(Project != null && ProjectId == Guid.Empty)
			{
				await Project.CloseProjectAsync(ProjectId.ToString());
			}

			this.Calculation = null;
			this.Connection = null;
			this.Export = null;
			this.LoadEffect = null;
			this.Material = null;
			this.Member = null;
			this.Operation = null;
			this.Parameter = null;
			this.Presentation = null;
			this.Project = null;
			this.Report = null;
			this.Template = null;
			this.ClientApi = null;
			this.ClientId = string.Empty;

		}

		private async Task<string> CreateClientAsync()
		{
			Configuration configuration = new Configuration();
			configuration.BasePath = BasePath.AbsoluteUri;

			var clientApi = new ClientApi(configuration);
			string clientId = await clientApi.ConnectClientAsync();
			configuration.DefaultHeaders.Add("ClientId", clientId);

			this.Calculation = new CalculationApi(clientApi.Client, clientApi.AsynchronousClient, configuration);
			this.Connection = new ConnectionApi(clientApi.Client, clientApi.AsynchronousClient, configuration);
			this.Export = new ExportApi(clientApi.Client, clientApi.AsynchronousClient, configuration);
			this.LoadEffect = new LoadEffectApi(clientApi.Client, clientApi.AsynchronousClient, configuration);
			this.Material = new MaterialApi(clientApi.Client, clientApi.AsynchronousClient, configuration);
			this.Member = new MemberApi(clientApi.Client, clientApi.AsynchronousClient, configuration);
			this.Operation = new OperationApi(clientApi.Client, clientApi.AsynchronousClient, configuration);
			this.Parameter = new ParameterApi(clientApi.Client, clientApi.AsynchronousClient, configuration);
			this.Presentation = new PresentationApi(clientApi.Client, clientApi.AsynchronousClient, configuration);
			this.Project = new ProjectApi(clientApi.Client, clientApi.AsynchronousClient, configuration);
			this.Report = new ReportApi(clientApi.Client, clientApi.AsynchronousClient, configuration);
			this.Template = new TemplateApi(clientApi.Client, clientApi.AsynchronousClient, configuration);

			this.ClientApi = clientApi;
			this.ClientId = clientId;
			return clientId;
		}

		protected virtual void Dispose(bool disposing)
		{
			if (!disposedValue)
			{
				if (disposing)
				{
					CloseAsync().Wait();
				}

				// TODO: free unmanaged resources (unmanaged objects) and override finalizer
				// TODO: set large fields to null
				disposedValue = true;
			}
		}

		protected virtual async Task DisposeAsync(bool disposing)
		{
			if (!disposedValue)
			{
				if (disposing)
				{
					await CloseAsync();
				}

				// TODO: free unmanaged resources (unmanaged objects) and override finalizer
				// TODO: set large fields to null
				disposedValue = true;
			}
		}

		public void Dispose()
		{
			// Do not change this code. Put cleanup code in 'Dispose(bool disposing)' method
			Dispose(disposing: true);
			GC.SuppressFinalize(this);
		}

		public async ValueTask DisposeAsync()
		{
			await DisposeAsync(disposing: true);
			GC.SuppressFinalize(this);
		}
	}
}