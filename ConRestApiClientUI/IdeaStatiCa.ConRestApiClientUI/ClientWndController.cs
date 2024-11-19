using System;
using System.Threading.Tasks;

namespace IdeaStatiCa.ConRestApiClientUI
{
	public class ClientWndController
	{
		private static WebServer _server;

		public ClientWndController()
		{
		}

		public void Start(string wwwroot = null)
		{
			if(_server != null)
			{
				throw new InvalidOperationException("The server is already running.");
			}

			_server = new WebServer(wwwroot);
			_server.Run();
		}

		public async Task StopAsync()
		{
			if (_server == null)
			{
				return;
			}

			await _server.StopAsync();
			_server = null;
		}
	}
}
