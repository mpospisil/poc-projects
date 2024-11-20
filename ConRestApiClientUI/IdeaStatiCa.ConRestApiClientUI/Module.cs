using IdeaStatiCa.ConRestApiClientUI.Dialogs;
using IdeaStatiCa.ConRestApiClientUI.Services;
using IdeaStatiCa.ConRestApiClientUI.ViewModels;
using IdeaStatiCa.ConRestApiClientUI.Views;
using Microsoft.Extensions.Configuration;
using Microsoft.Extensions.DependencyInjection;

namespace IdeaStatiCa.ConRestApiClientUI
{
	public static class Module
	{
		public static void RegisterConRestApiClient(this ServiceCollection services)
		{
			services.AddTransient<IConRestApiClientViewModel, ConRestApiClientViewModel>();
			services.AddTransient<IDialogService, DialogService>();
			services.AddTransient<IClientHost, ClientHost>();
			services.AddTransient<ConRestApiClient>();

			services.AddSingleton<IConApiClientVMProvider, ConApiClientVMProvider>(serviceProvider =>
			{
				var config = serviceProvider.GetRequiredService<IConfiguration>();
				return new ConApiClientVMProvider(config, serviceProvider);
			});

			services.AddSingleton<IWebServer, WebServer>(serviceProvider =>
			{
				return new WebServer();
			});


		}
	}
}
