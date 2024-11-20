using System;
using System.Windows;


namespace IdeaStatiCa.ConRestApiClientUI.Views
{
	/// <summary>
	/// Interaction logic for ConRestApiClientWnd.xaml
	/// </summary>
	public partial class ConRestApiClient : Window
	{
		public ConRestApiClient()
		{
			InitializeComponent();
			//InitializeWebView();
		}

		//private async void InitializeWebView()
		//{
		//	await webView.EnsureCoreWebView2Async(null);

		//	string htmlFilePath = "http://localhost:8080/index.html";
		//	webView.CoreWebView2.Navigate(new Uri(htmlFilePath).AbsoluteUri);

		//	var host = new ClientHost();

		//	// Expose .NET object to JavaScript
		//	webView.CoreWebView2.AddHostObjectToScript("clientHost", host);
		//}
	}
}
