using ConRestApiClientUI_App.ViewModels;
using Microsoft.Extensions.Configuration;
using System.Diagnostics;
using System.Windows;

namespace ConRestApiClientUI_App
{
	/// <summary>
	/// Interaction logic for MainWindow.xaml
	/// </summary>
	public partial class MainWindow : Window
	{
		private readonly IMainWindowViewModel _viewModel;
		public MainWindow(IConfiguration configuration, IMainWindowViewModel vm)
		{
			Debug.Assert(vm != null);
			Debug.Assert(configuration != null);

			this.DataContext = vm;
			this._viewModel = vm;
			InitializeComponent();
		}

		private async void Window_Loaded(object sender, RoutedEventArgs e)
		{
			await this._viewModel.OnLoadAsync();
		}
	}
}