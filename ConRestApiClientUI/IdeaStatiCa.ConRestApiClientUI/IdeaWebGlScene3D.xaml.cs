using System.Windows.Controls;

namespace IdeaStatiCa.ConRestApiClientUI
{
	/// <summary>
	/// Interaction logic for IdeaWebGlScene3D.xaml
	/// </summary>
	public partial class IdeaWebGlScene3D : UserControl
	{
		private readonly IConRestApiClientViewModel _viewModel;
		public IdeaWebGlScene3D(IConRestApiClientViewModel viewModel)
		{
			this._viewModel = viewModel;
			this.DataContext = viewModel;
			InitializeComponent();
		}

		private async void UserControl_Loaded(object sender, System.Windows.RoutedEventArgs e)
		{
			await webView.EnsureCoreWebView2Async(null);

			//// Expose .NET object to JavaScript
			webView.CoreWebView2.AddHostObjectToScript("clientHost", _viewModel.ClientHost);

			webView.CoreWebView2.Navigate(_viewModel.MainPageUrl);
		}

		private void webView_NavigationCompleted(object sender, Microsoft.Web.WebView2.Core.CoreWebView2NavigationCompletedEventArgs e)
		{
			_viewModel.NotifyViewInited();
		}

		private void UserControl_Unloaded(object sender, System.Windows.RoutedEventArgs e)
		{
			_viewModel.NotifyViewClosed();
		}
	}
}
