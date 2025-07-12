using CommunityToolkit.Mvvm.ComponentModel;
using IdeaStatiCa.Plugin;
using Microsoft.Extensions.Configuration;

namespace IdeaStatiCa.ConRestApiClientUI
{
	public interface IConRestApiClientViewModel
	{
		IClientHost ClientHost { get; }
		string MainPageUrl { get; }

		void OnViewInited();
	}

	public class ConRestApiClientViewModel : ObservableObject, IConRestApiClientViewModel
	{
		private readonly IPluginLogger _logger;
		private readonly IClientHost _clientHost;
		private readonly IConfiguration _configuration;
		private bool isViewReady;

		public ConRestApiClientViewModel(IConfiguration configuration, IPluginLogger logger, IClientHost clientHost)
		{
			this._logger = logger;
			this._clientHost = clientHost;
			this._configuration = configuration;
		}

		public IClientHost ClientHost => _clientHost;

		public string MainPageUrl => _configuration["MAIN_PAGE_URL"];

		public bool IsViewReady
		{
			get => isViewReady;
			set
			{
				isViewReady = value;
				OnPropertyChanged("IsViewReady");
			}
		}

		public void OnViewInited()
		{
			_logger.LogDebug("ConRestApiClientViewModel.OnViewInited");
			IsViewReady = true;
		}
	}
}
