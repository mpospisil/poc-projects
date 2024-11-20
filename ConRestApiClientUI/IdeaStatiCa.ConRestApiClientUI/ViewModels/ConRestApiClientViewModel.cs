namespace IdeaStatiCa.ConRestApiClientUI.ViewModels
{
	public interface IConRestApiClientViewModel
	{
		string ClientUiUrl { get; set; }
	}

	public class ConRestApiClientViewModel : ViewModelBase, IConRestApiClientViewModel
	{
		public ConRestApiClientViewModel()
		{
			ClientUiUrl = "https://www.ideastatica.com";
		}


		private string clientUiUrl;
		public string ClientUiUrl
		{
			get => clientUiUrl;
			set => SetProperty(ref clientUiUrl, value);
		}
	}
}
