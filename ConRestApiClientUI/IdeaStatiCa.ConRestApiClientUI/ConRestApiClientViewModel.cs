using CommunityToolkit.Mvvm.ComponentModel;
using IdeaStatiCa.Plugin;
using Microsoft.Extensions.Configuration;
using Microsoft.Web.WebView2.Wpf;
using System.Threading.Tasks;

namespace IdeaStatiCa.ConRestApiClientUI
{
	public interface IConRestApiClientViewModel
	{
		IClientHost ClientHost { get; }
		string MainPageUrl { get; }

		bool IsViewReady { get; }

		void NotifyViewInited(WebView2 webView);

		void NotifyViewClosed();

		Task PresentAsync(string sceneData);
	}

	public class ConRestApiClientViewModel : ObservableObject, IConRestApiClientViewModel
	{
		private readonly IPluginLogger _logger;
		private readonly IClientHost _clientHost;
		private readonly IConfiguration _configuration;
		private bool isViewReady;
		private WebView2 _webView;

		public ConRestApiClientViewModel(IConfiguration configuration, IPluginLogger logger, IClientHost clientHost)
		{
			this._logger = logger;
			this._clientHost = clientHost;
			this._configuration = configuration;
		}

		public IClientHost ClientHost => _clientHost;

		public string MainPageUrl => _configuration["MAIN_PAGE_URL"];

		public bool IsViewReady
		{
			get => isViewReady;
			set
			{
				isViewReady = value;
				OnPropertyChanged("IsViewReady");
			}
		}

		public void NotifyViewInited(WebView2 webView)
		{
			_logger.LogDebug("ConRestApiClientViewModel.OnViewInited");
			_webView = webView;
			IsViewReady = true;
		}

		public void NotifyViewClosed()
		{
			_logger.LogDebug("ConRestApiClientViewModel.OnViewClosed");
			_webView = null;
			IsViewReady = false;
		}

		public async Task PresentAsync(string sceneData)
		{
			if(_webView == null)
			{
				_logger.LogDebug("WebView is not connected");
				return;
			}

			var javaScript = $"window.scene3dPresenterApi.PresentFunction('{sceneData}')";
			await _webView.CoreWebView2.ExecuteScriptAsync(javaScript);
		}
	}
}
