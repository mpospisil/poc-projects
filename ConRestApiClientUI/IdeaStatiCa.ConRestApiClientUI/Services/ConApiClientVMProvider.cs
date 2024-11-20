using IdeaStatiCa.ConRestApiClientUI.ViewModels;
using Microsoft.Extensions.Configuration;
using Microsoft.Extensions.DependencyInjection;
using System;

namespace IdeaStatiCa.ConRestApiClientUI.Services
{
	internal class ConApiClientVMProvider : IConApiClientVMProvider
	{
		private readonly IServiceProvider _serviceProvider;
		private readonly IConfiguration _configuration;

		public ConApiClientVMProvider(IConfiguration configuration, IServiceProvider serviceProvider)
		{
			this._configuration = configuration;
			this._serviceProvider = serviceProvider;
		}

		public IConRestApiClientViewModel CreateConApiClientViewModel()
		{
			var vm = _serviceProvider.GetRequiredService<IConRestApiClientViewModel>();
			return vm;
		}
	}
}
