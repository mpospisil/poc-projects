using System;
using System.Windows;


namespace IdeaStatiCa.ConRestApiClientUI
{
	/// <summary>
	/// Interaction logic for ConRestApiClientWnd.xaml
	/// </summary>
	public partial class ConRestApiClientWnd : Window
	{
		public ConRestApiClientWnd()
		{
			InitializeComponent();
			InitializeWebView();
		}

		private async void InitializeWebView()
		{
			await webView.EnsureCoreWebView2Async(null);

			string htmlFilePath = System.IO.Path.Combine(AppDomain.CurrentDomain.BaseDirectory, "static", "index.html");
			//string htmlFilePath = System.IO.Path.Combine(AppDomain.CurrentDomain.BaseDirectory, "static2", "index.html");

			//// Disable CORS
			//webView.CoreWebView2.WebResourceRequested += (sender, args) =>
			//{
			//	var request = args.Request;
			//	var headers = request.Headers;

			//	// Add headers to disable CORS
			//	headers.SetHeader("Access-Control-Allow-Origin", "*");
			//	headers.SetHeader("Access-Control-Allow-Methods", "GET, POST, PUT, DELETE, OPTIONS");
			//	headers.SetHeader("Access-Control-Allow-Headers", "Content-Type, Authorization");

			//	args.Response = webView.CoreWebView2.Environment.CreateWebResourceResponse(
			//			null, 200, "OK", headers.ToString());
			//};

			webView.CoreWebView2.Navigate(new Uri(htmlFilePath).AbsoluteUri);

			var host = new ClientHost();

			// Expose .NET object to JavaScript
			webView.CoreWebView2.AddHostObjectToScript("clientHost", host);

		}
	}
}
