using IdeaStatiCa.ConRestApiClientUI.ViewModels;

namespace IdeaStatiCa.ConRestApiClientUI.Services
{
	public interface IConApiClientVMProvider
	{
		IConRestApiClientViewModel CreateConApiClientViewModel();
	}
}
