using System;
using System.Threading.Tasks;

namespace connection_restapi_client_poc.Api
{
	public interface IProjectApiExtAsync : IProjectApiAsync
	{
		Task DownloadProjectAsync(Guid projectId, string fileName);
	}

	public class ProjectApiExt : ProjectApi, IProjectApiExtAsync
	{
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
	}
}
