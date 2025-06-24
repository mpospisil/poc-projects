using Microsoft.Extensions.Configuration;
using System.Windows;

namespace ConRestApiClientUI_App
{
	/// <summary>
	/// Interaction logic for App.xaml
	/// </summary>
	public partial class App : Application
	{
		private readonly IConfiguration _configuration;
		public App()
		{
			IConfiguration config = BuildConfiguration();
			MainWindow mainWindow = new MainWindow(config);
			mainWindow.Show();
		}

		public static IConfigurationRoot BuildConfiguration()
		{
			return new ConfigurationBuilder()
				.AddJsonFile("appsettings.json")
				.AddEnvironmentVariables()
				.Build();
		}
	}
}
