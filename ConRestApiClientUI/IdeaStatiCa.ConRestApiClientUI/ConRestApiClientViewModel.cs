using CommunityToolkit.Mvvm.ComponentModel;
//using IdeaStatiCa.Plugin;
using Microsoft.Extensions.Configuration;
using Microsoft.Web.WebView2.Wpf;
using System;
using System.IO;
using System.Threading.Tasks;
using System.Windows;

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

		Task<Stream> CaptureSceneAsImage();
	}

	public class ConRestApiClientViewModel : ObservableObject, IConRestApiClientViewModel
	{
		//private readonly IPluginLogger _logger;
		private readonly IClientHost _clientHost;
		private readonly IConfiguration _configuration;
		private bool isViewReady;
		private WebView2 _webView;

		public ConRestApiClientViewModel(IConfiguration configuration,/* IPluginLogger logger, */IClientHost clientHost)
		{
			//this._logger = logger;
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
			//_logger.LogDebug("ConRestApiClientViewModel.OnViewInited");
			_webView = webView;
			IsViewReady = true;
		}

		public void NotifyViewClosed()
		{
			//_logger.LogDebug("ConRestApiClientViewModel.OnViewClosed");
			_webView = null;
			IsViewReady = false;
		}

		public async Task PresentAsync(string sceneData)
		{
			if(_webView == null)
			{
				//_logger.LogDebug("WebView is not connected");
				return;
			}

			var javaScript = $"window.scene3dPresenterApi.PresentFunction('{sceneData}')";
			await _webView.CoreWebView2.ExecuteScriptAsync(javaScript);
		}

		public async Task<Stream> CaptureSceneAsImage()
		{
			if (_webView == null)
			{
				//_logger.LogDebug("WebView is not connected");
				throw new System.Exception("WebView is not connected");
			}

			var javaScript = $"window.scene3dPresenterApi.CaptureDivAsImage('scenePlaceholder')";
			string result = await _webView.CoreWebView2.ExecuteScriptAsync(javaScript);

			//if (!string.IsNullOrEmpty(result) && result != "null")
			//{
			//	// The result will be a JSON-encoded string, which needs to be deserialized.
			//	// If the JS returns a raw string, it might just be the Base64.
			//	// For simple string return, remove JSON.stringify in JS or handle here.
			//	string base64Image = result.Trim('"'); // Remove quotes if ExecuteScriptAsync adds them

			//	// Remove the data URL prefix (e.g., "data:image/png;base64,")
			//	if (base64Image.StartsWith("data:image"))
			//	{
			//		int commaIndex = base64Image.IndexOf(',');
			//		if (commaIndex > -1)
			//		{
			//			base64Image = base64Image.Substring(commaIndex + 1);
			//		}
			//	}

			//	byte[] imageBytes = Convert.FromBase64String(base64Image);

			//	MemoryStream ms = new MemoryStream();
			//	await ms.WriteAsync(imageBytes, 0, imageBytes.Length);
			//	ms.Seek(0, SeekOrigin.Begin);
			//	return ms;
			//}
			//else
			//{
			//	throw new Exception("Failed to capture div or div not found.");
			//}

			return new MemoryStream();
		}
	}
}
