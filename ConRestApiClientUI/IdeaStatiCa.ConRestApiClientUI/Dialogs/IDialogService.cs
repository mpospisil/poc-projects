using IdeaStatiCa.ConRestApiClientUI.ViewModels;
using System.Windows;

namespace IdeaStatiCa.ConRestApiClientUI.Dialogs
{
	public interface IDialogService
	{
		Window GetDialog(object viewModel);
	}
}
