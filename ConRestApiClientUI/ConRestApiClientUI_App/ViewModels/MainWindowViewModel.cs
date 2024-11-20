using CommunityToolkit.Mvvm.Input;
using IdeaStatiCa.ConRestApiClientUI.Services;
using IdeaStatiCa.ConRestApiClientUI.ViewModels;
using System.Threading.Tasks;

namespace ConRestApiClientUI_App.ViewModels
{
	public class MainWindowViewModel : ViewModelBase
	{
		private readonly IWebServer _webServer;
		public MainWindowViewModel(IWebServer webServer)
		{
			this._webServer = webServer;
			ShowClientWndCommand = new AsyncRelayCommand<string>(ShowClientWndAsync, CanShowClientWndAsync);
			_webServer.StartAsync().ContinueWith(_ =>
			{

			});
		}

		public IAsyncRelayCommand<string> ShowClientWndCommand { get; }

		private bool CanShowClientWndAsync(string name)
		{
			return true;
		}

		private async Task ShowClientWndAsync(string name)
		{
			//var projInfo = await projectService.CreateProjectAsync();
			//Status = projInfo.Id;
			await Task.CompletedTask;
		}

		private string status;
		public string Status
		{
			get => status;
			set => SetProperty(ref status, value);
		}

		private void RefreshCommands()
		{
			this.ShowClientWndCommand.NotifyCanExecuteChanged();
			//this.ShowClientUICommand.NotifyCanExecuteChanged();
		}
	}
}
