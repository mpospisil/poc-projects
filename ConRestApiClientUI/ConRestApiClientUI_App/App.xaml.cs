using IdeaStatiCa.ConRestApiClientUI;
using System.Configuration;
using System.Data;
using System.Windows;

namespace ConRestApiClientUI_App
{
	/// <summary>
	/// Interaction logic for App.xaml
	/// </summary>
	public partial class App : Application
	{
		ClientWndController _controller;
		public App()
		{
		}

		private void Application_Startup(object sender, StartupEventArgs e)
		{
			_controller = new ClientWndController();
			_controller.Start();
		}

		private void Application_Exit(object sender, ExitEventArgs e)
		{
			_controller.StopAsync();
		}
	}

}
