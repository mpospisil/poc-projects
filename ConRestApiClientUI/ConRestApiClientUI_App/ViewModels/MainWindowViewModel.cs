using CommunityToolkit.Mvvm.Input;
using IdeaStatiCa.ConRestApiClientUI.Dialogs;
using IdeaStatiCa.ConRestApiClientUI.Services;
using IdeaStatiCa.ConRestApiClientUI.ViewModels;
using System.Threading.Tasks;

namespace ConRestApiClientUI_App.ViewModels
{
	public class MainWindowViewModel : ViewModelBase
	{
		private readonly IWebServer _webServer;
		private readonly IConApiClientVMProvider _conApiVmProvider;
		private readonly IDialogService _dialogService;

		public MainWindowViewModel(IWebServer webServer,
			IConApiClientVMProvider conApiVmProvider,
			IDialogService dialogService)
		{
			this._dialogService = dialogService;
			this._conApiVmProvider = conApiVmProvider;
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
			var vm = _conApiVmProvider.CreateConApiClientViewModel();

			var dlg = _dialogService.GetDialog(vm);

			dlg.ShowDialog();

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
