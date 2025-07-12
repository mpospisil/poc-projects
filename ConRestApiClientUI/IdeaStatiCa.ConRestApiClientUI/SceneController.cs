using IdeaStatiCa.Plugin;
using Microsoft.Extensions.Configuration;
using System.Threading.Tasks;

namespace IdeaStatiCa.ConRestApiClientUI
{
	public class SceneController : ISceneController
	{
		private readonly IWebServer _webServer;
		private readonly IConfiguration _configuration;
		private readonly IPluginLogger _logger;
		private readonly bool _isDevelop;
		private readonly IConRestApiClientViewModel _conRestApiClientVM;

		public SceneController(IConfiguration configuration, IPluginLogger logger, IConRestApiClientViewModel conRestApiClientVM)
		{
			this._configuration = configuration;
			this._conRestApiClientVM = conRestApiClientVM;
			this._webServer = new WebServer("static");
			this._logger = logger;
			var baseUrl = _configuration["WEBSERVER_ENDPOINT"];
			var useNodeJsServer = _configuration["USE_NODEJS_SERVER"];
			this._isDevelop = "true".Equals(useNodeJsServer, System.StringComparison.InvariantCultureIgnoreCase);

			if (!_isDevelop)
			{
				this._webServer.Start(baseUrl);
			}
		}

		public void ShowWindow()
		{
			var dlg = new ConRestApiClientWnd(_conRestApiClientVM);
			dlg.Show();
		}
	}
}
