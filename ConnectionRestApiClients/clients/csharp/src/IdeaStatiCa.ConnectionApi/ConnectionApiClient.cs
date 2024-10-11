using IdeaStatiCa.ConnectionApi.Api;
using IdeaStatiCa.ConnectionApi.Client;
using IdeaStatiCa.ConnectionApi.Model;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace IdeaStatiCa.ConnectionApi
{
	public class ConnectionApiClient : IConnectionApiClient
	{
		private bool disposedValue;
		
		/// <summary>
		/// 
		/// </summary>
		public Uri BasePath { get; private set; }

		/// <inheritdoc cref="IConnectionApiClient.ClientId"/>/>
		public string ClientId { get; private set; }

		/// <summary>
		/// Client API
		/// </summary>
		public IClientApi ClientApi { get; private set; }

		/// <inheritdoc cref="IConnectionApiClient.Calculation"/>
		public ICalculationApiAsync Calculation { get; private set; }
		
		/// <inheritdoc cref="IConnectionApiClient.Connection"/>
		public IConnectionApiAsync Connection { get; private set; }
		
		/// <inheritdoc cref="IConnectionApiClient.Export"/>

		public IExportApiExtAsync Export { get; private set; }

		/// <inheritdoc cref="IConnectionApiClient.LoadEffect"/>
		public ILoadEffectApiAsync LoadEffect { get; private set; }
		
		/// <inheritdoc cref="IConnectionApiClient.Material"/>
		public IMaterialApiAsync Material { get; private set; }
		
		/// <inheritdoc cref="IConnectionApiClient.Member"/>
		public IMemberApiAsync Member { get; private set; }
		
		/// <inheritdoc cref="IConnectionApiClient.Operation"/>
		public IOperationApiAsync Operation { get; private set; }
		
		/// <inheritdoc cref="IConnectionApiClient.Parameter"/>
		public IParameterApiAsync Parameter { get; private set; }
		
		/// <inheritdoc cref="IConnectionApiClient.Presentation"/>
		public IPresentationApiAsync Presentation { get; private set; }
		
		/// <inheritdoc cref="IConnectionApiClient.Project"/>
		public IProjectApiExtAsync Project { get; private set; }

		/// <inheritdoc cref="IConnectionApiClient.Report"/>
		public IReportApiAsync Report { get; private set; }

		/// <inheritdoc cref="IConnectionApiClient.Template"/>
		public ITemplateApiExtAsync Template { get; private set; }


		/// <summary>
		/// 
		/// </summary>
		/// <param name="basePath"></param>
		public ConnectionApiClient(string basePath)
		{
			BasePath = new Uri(basePath);
            CreateClientAsync().Wait();
        }

		/// <summary
		/// 
		/// </summary>
		/// <returns></returns>
		/// <exception cref="Exception"></exception>
		public async Task CreateAsync()
		{
			if (ClientApi != null)
			{
				throw new Exception("Client is already connected");
			}

			await CreateClientAsync();
		}

		//public async Task<ConProject> OpenFromIomFileAsync(string iomFilePath)
		//{
		//	await CreateAsync();

		//	var conProject = await this.Project.CreateProjectFromIomFileAsync(iomFilePath);
		//	this.ActiveProject = conProject;
		//	this.ProjectId = conProject.ProjectId;

		//	return conProject;
		//}

		//public async Task<ConProject> OpenProjectAsync(string path)
		//{
		//	await CreateAsync();

		//	using (var fs = new System.IO.FileStream(path, System.IO.FileMode.Open))
		//	{
		//		using (var ms = new System.IO.MemoryStream())
		//		{
		//			await fs.CopyToAsync(ms);
		//			ms.Seek(0, System.IO.SeekOrigin.Begin);
		//			var conProject = await this.Project.OpenProjectAsync(ms);
		//			this.ActiveProject = conProject;
		//			this.ProjectId = conProject.ProjectId;
		//		}
		//	}
		//}


		private async Task CloseAsync()
		{
			if(Project != null)
			{
				//Close all projects open on the server.
				var guids = await Project.GetActiveProjectsAsync();
				var closed = await Task.WhenAll(guids.Select(x => Project.CloseProjectAsync(x.ProjectId.ToString())));
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
			this.Connection = new IdeaStatiCa.ConnectionApi.Api.ConnectionApi(clientApi.Client, clientApi.AsynchronousClient, configuration);
			this.Export = new ExportApiExt(clientApi.Client, clientApi.AsynchronousClient, configuration);
			this.LoadEffect = new LoadEffectApi(clientApi.Client, clientApi.AsynchronousClient, configuration);

			var iomClient = new IdeaStatiCa.ConnectionApi.Client.ApiClient(configuration.BasePath);
			iomClient.SerializerSettings = IdeaJsonSerializerSetting.GetJsonSettingIdea();

			this.Material = new MaterialApi(iomClient, iomClient, configuration);
			this.Member = new MemberApi(clientApi.Client, clientApi.AsynchronousClient, configuration);
			this.Operation = new OperationApi(clientApi.Client, clientApi.AsynchronousClient, configuration);
			this.Parameter = new ParameterApi(clientApi.Client, clientApi.AsynchronousClient, configuration);
			this.Presentation = new PresentationApi(clientApi.Client, clientApi.AsynchronousClient, configuration);
			this.Project = new ProjectApiExt(clientApi.Client, clientApi.AsynchronousClient, configuration);
			this.Report = new ReportApi(clientApi.Client, clientApi.AsynchronousClient, configuration);
			this.Template = new TemplateApiExt(iomClient, iomClient, configuration);


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
