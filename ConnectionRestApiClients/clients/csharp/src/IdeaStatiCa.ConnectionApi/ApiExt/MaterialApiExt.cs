using System;
using System.Collections.Generic;
using System.Text;

namespace connection_restapi_client_poc.Api
{
	public class MaterialApiExt : MaterialApi
	{
			public MaterialApiExt(connection_restapi_client_poc.Client.ISynchronousClient client, connection_restapi_client_poc.Client.IAsynchronousClient asyncClient, connection_restapi_client_poc.Client.IReadableConfiguration configuration) : base(client, asyncClient, configuration)
			{
			}
	}
}
