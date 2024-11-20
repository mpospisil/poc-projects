using IdeaStatiCa.ConRestApiClientUI.Services;

namespace IdeaStatiCa.ConRestApiClientUI.ViewModels
{
	public interface IConRestApiClientViewModel
	{
		string ClientUiUrl { get; set; }

		IClientHost ClientHost { get; set; }
	}

	public class ConRestApiClientViewModel : ViewModelBase, IConRestApiClientViewModel
	{
		private readonly IWebServer _webserver;

		public ConRestApiClientViewModel(IWebServer webserver, IClientHost clientHost)
		{
			this._webserver = webserver;
			this.ClientUiUrl = webserver.GetUrl();
			this.ClientHost = clientHost;
		}

		private string clientUiUrl;
		public string ClientUiUrl
		{
			get => clientUiUrl;
			set => SetProperty(ref clientUiUrl, value);
		}

		private IClientHost clientHost;
		public IClientHost ClientHost
		{
			get => clientHost;
			set => SetProperty(ref clientHost, value);
		}
	}
}
