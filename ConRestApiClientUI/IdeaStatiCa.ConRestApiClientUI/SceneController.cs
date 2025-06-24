using Microsoft.Extensions.Configuration;

namespace IdeaStatiCa.ConRestApiClientUI
{
	public class SceneController : ISceneController
	{
		private readonly IWebServer _webServer;
		private readonly IConfiguration _configuration;

		public SceneController(IConfiguration configuration)
		{
			this._configuration = configuration;
			this._webServer = new WebServer("static");
			var baseUrl = _configuration["WEBSERVER_ENDPOINT"];

			this._webServer.Start(baseUrl);
		}

		public void ShowWindowAsync()
		{
			var dlg = new ConRestApiClientWnd();
			dlg.Show();



			string htmlFilePath = _configuration["MAIN_PAGE_URL"];
			dlg.ShowAsync(htmlFilePath);
		}
	}
}
