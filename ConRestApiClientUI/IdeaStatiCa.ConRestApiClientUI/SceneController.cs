using Microsoft.Extensions.Configuration;
using System.Threading.Tasks;

namespace IdeaStatiCa.ConRestApiClientUI
{
	public class SceneController : ISceneController
	{
		private readonly IWebServer _webServer;
		private readonly IConfiguration _configuration;
		private readonly bool _isDevelop;

		public SceneController(IConfiguration configuration)
		{
			this._configuration = configuration;
			this._webServer = new WebServer("static");
			var baseUrl = _configuration["WEBSERVER_ENDPOINT"];
			var useNodeJsServer = _configuration["USE_NODEJS_SERVER"];
			this._isDevelop = "true".Equals(useNodeJsServer);

			if (!_isDevelop)
			{
				this._webServer.Start(baseUrl);
			}
		}

		public async Task ShowWindowAsync()
		{
			var dlg = new ConRestApiClientWnd();
			dlg.Show();

			string htmlFilePath = _configuration["MAIN_PAGE_URL"];
			await dlg.ShowAsync(htmlFilePath);
		}
	}
}
