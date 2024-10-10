namespace connection_restapi_client_poc.Api
{
	public class TemplateApiExt : TemplateApi
	{
		public TemplateApiExt(connection_restapi_client_poc.Client.ISynchronousClient client, connection_restapi_client_poc.Client.IAsynchronousClient asyncClient, connection_restapi_client_poc.Client.IReadableConfiguration configuration) : base(client, asyncClient, configuration)
		{
		}
	}
}
