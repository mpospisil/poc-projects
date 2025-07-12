using System;
using System.Threading.Tasks;
using System.Windows;


namespace IdeaStatiCa.ConRestApiClientUI
{
	/// <summary>
	/// Interaction logic for ConRestApiClientWnd.xaml
	/// </summary>
	public partial class ConRestApiClientWnd : Window
	{
		private readonly SceneController _sceneController;
		//private readonly C _sceneController2;
		public ConRestApiClientWnd()
		{
			InitializeComponent();
		}

		public async Task ShowAsync(string url)
		{
			await webView.EnsureCoreWebView2Async(null);
			var host = new ClientHost();

			// Expose .NET object to JavaScript
			webView.CoreWebView2.AddHostObjectToScript("clientHost", host);

			webView.CoreWebView2.Navigate(url);
		}
	}
}
