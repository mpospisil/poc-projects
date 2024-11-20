using System;
using System.Threading.Tasks;

namespace IdeaStatiCa.ConRestApiClientUI.Services
{
	public class ClientWndController
	{
		private IWebServer _server;

		public ClientWndController(IWebServer server)
		{
			_server = server;
		}

		//public async Task Start(string wwwroot = null)
		//{
		//	if(_server != null)
		//	{
		//		throw new InvalidOperationException("The server is already running.");
		//	}

		//	_server = new WebServer(wwwroot);
		//	_server.Run();

		//	await Task.CompletedTask;
		//}

		//public async Task StopAsync()
		//{
		//	if (_server == null)
		//	{
		//		return;
		//	}

		//	await _server.StopAsync();
		//	_server = null;
		//}
	}
}
