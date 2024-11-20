using IdeaStatiCa.ConRestApiClientUI.ViewModels;
using IdeaStatiCa.ConRestApiClientUI.Views;
using Microsoft.Extensions.DependencyInjection;
using System;
using System.Windows;

namespace IdeaStatiCa.ConRestApiClientUI.Dialogs
{
	internal class DialogService : IDialogService
	{
		private readonly IServiceProvider _serviceProvider;

		public DialogService(IServiceProvider serviceProvider)
		{
			this._serviceProvider = serviceProvider;
		}

		public Window GetDialog(object viewModel)
		{
			if(viewModel is IConRestApiClientViewModel vm)
			{
				var wnd = _serviceProvider.GetRequiredService<ConRestApiClient>();
				wnd.DataContext = vm;
				return wnd;
			}

			throw new NotImplementedException();
		}
	}
}
