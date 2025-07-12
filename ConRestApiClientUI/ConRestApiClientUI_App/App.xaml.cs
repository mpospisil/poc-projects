using ConRestApiClientUI_App.ViewModels;
using IdeaStatiCa.ConRestApiClientUI;
using IdeaStatiCa.Plugin;
using IdeaStatiCa.PluginLogger;
using Microsoft.Extensions.Configuration;
using Microsoft.Extensions.DependencyInjection;
using System.Configuration;
using System.Windows;

namespace ConRestApiClientUI_App
{
	/// <summary>
	/// Interaction logic for App.xaml
	/// </summary>
	public partial class App : Application
	{
		private readonly IConfiguration _configuration;
		private readonly IServiceProvider serviceProvider;
		private MainWindowViewModel? mainWindowViewModel;

		public App()
		{
			IConfiguration config = BuildConfiguration();

			var services = new ServiceCollection();

			services.AddSingleton<IConfiguration>(config);

			services.AddSingleton<IPluginLogger>(serviceProvider =>
			{
				SerilogFacade.Initialize();
				return LoggerProvider.GetLogger("ConRestApiClientUI_App");
			});

			services.AddTransient<IMainWindowViewModel , MainWindowViewModel>();

			services.AddTransient<MainWindow>();

			services.AddTransient<ISceneController, SceneController>();

			services.AddTransient<IClientHost, ClientHost>();

			services.AddTransient<IConRestApiClientViewModel, ConRestApiClientViewModel>();

			serviceProvider = services.BuildServiceProvider();
		}

		public static IConfigurationRoot BuildConfiguration()
		{
			return new ConfigurationBuilder()
				.AddJsonFile("appsettings.json")
				.AddEnvironmentVariables()
				.Build();
		}

		protected override void OnExit(ExitEventArgs e)
		{
			if (this.mainWindowViewModel != null)
			{
				//this.mainWindowViewModel.Dispose();
				this.mainWindowViewModel = null;
			}

			base.OnExit(e);
		}

		protected override void OnStartup(StartupEventArgs e)
		{
			var mainWindow = serviceProvider.GetRequiredService<MainWindow>();
			mainWindow.Show();
			this.mainWindowViewModel = mainWindow.DataContext as MainWindowViewModel;
			base.OnStartup(e);
		}
	}
}
