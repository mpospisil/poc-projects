using IdeaStatiCa.ConRestApiClientUI.Services;
using Microsoft.Extensions.DependencyInjection;

namespace IdeaStatiCa.ConRestApiClientUI
{
	public static class Module
	{
		public static void RegisterConRestApiClient(this ServiceCollection services)
		{
			services.AddSingleton<IWebServer, WebServer>(serviceProvider =>
			{
				return new WebServer();
			});


		}
	}
}
