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

			string htmlFilePath = System.IO.Path.Combine(AppDomain.CurrentDomain.BaseDirectory, "static", "test1.html");
			webView.CoreWebView2.Navigate(new Uri(htmlFilePath).AbsoluteUri);

			var host = new ClientHost();

			// Expose .NET object to JavaScript
			webView.CoreWebView2.AddHostObjectToScript("clientHost", host);

		}
	}
}
