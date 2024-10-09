using connection_restapi_client_poc.Model;
using System;
using System.IO;
using System.Threading.Tasks;

namespace connection_restapi_client_poc.Api
{
	public interface IProjectApiAsyncExt : IProjectApiAsync
	{
		Task<ConProject> OpenProjectFromFileAsync(string fileName);

        Task SaveProjectAsync(Guid projectId, string fileName);
	}

	public class ProjectApiExt : ProjectApi, IProjectApiAsyncExt
	{
		public ProjectApiExt(connection_restapi_client_poc.Client.ISynchronousClient client, connection_restapi_client_poc.Client.IAsynchronousClient asyncClient, connection_restapi_client_poc.Client.IReadableConfiguration configuration) : base(client, asyncClient, configuration)
		{
		}

        public async Task<ConProject> OpenProjectFromFileAsync(string filePath)
        {
            ConProject conProject = null;

            using (var fs = new System.IO.FileStream(filePath, System.IO.FileMode.Open))
            {
                using (var ms = new System.IO.MemoryStream())
                {
                    await fs.CopyToAsync(ms);
                    ms.Seek(0, System.IO.SeekOrigin.Begin);
                    conProject = await this.OpenProjectAsync(ms);
                }
            }

            return conProject;
        }

        public async Task<ConProject> CreateProjectFromIomFileAsync(string filePath)
        {
            

            ConProject conProject = null;

            using (var fs = new System.IO.FileStream(filePath, System.IO.FileMode.Open))
            {
                using (var ms = new System.IO.MemoryStream())
                {
                    await fs.CopyToAsync(ms);
                    ms.Seek(0, System.IO.SeekOrigin.Begin);

                    //this.ImportIOMContainerAsync()


                    conProject = await this.OpenProjectAsync(ms);
                }
            }

            return conProject;
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
    }
}
