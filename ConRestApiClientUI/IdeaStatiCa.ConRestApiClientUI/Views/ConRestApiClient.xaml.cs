using IdeaStatiCa.ConRestApiClientUI.ViewModels;
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
		}

		private void Window_DataContextChanged(object sender, DependencyPropertyChangedEventArgs e)
		{
			if(e.NewValue is IConRestApiClientViewModel vm)
			{
				if(e.NewValue != e.OldValue)
				{
					InitializeWebView(vm);
				}
			}
		}

		private async void InitializeWebView(IConRestApiClientViewModel vm)
		{
			await webView.EnsureCoreWebView2Async(null);

			string htmlFilePath = $"{vm.ClientUiUrl}/index.html";
			webView.CoreWebView2.Navigate(new Uri(htmlFilePath).AbsoluteUri);

			// Expose .NET object to JavaScript
			webView.CoreWebView2.AddHostObjectToScript("clientHost", vm.ClientHost);
		}
	}
}
