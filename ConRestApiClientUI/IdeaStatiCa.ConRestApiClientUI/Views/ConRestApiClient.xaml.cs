using IdeaStatiCa.ConRestApiClientUI.Services;
using IdeaStatiCa.ConRestApiClientUI.ViewModels;
using System;
using System.Threading.Tasks;
using System.Windows;


namespace IdeaStatiCa.ConRestApiClientUI.Views
{
	/// <summary>
	/// Interaction logic for ConRestApiClientWnd.xaml
	/// </summary>
	public partial class ConRestApiClient : Window, IScriptExecutor
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

			vm.ClientHost.AttachScriptExecutor(this);
		}

		public async Task<string> ExecuteScriptAsync(string script)
		{
			var result = await webView.CoreWebView2.ExecuteScriptWithResultAsync(script);
			if (!result.Succeeded)
			{
				throw new Exception(result.Exception.Message);
			}
			else
			{ 
				int is_success = 0;
				string str = "";
				result.TryGetResultAsString(out str, out is_success);
				if (is_success == 1)
				{
					return str;
				}
				else
				{
				return string.Empty;
				}
			}
		}
	}
}
