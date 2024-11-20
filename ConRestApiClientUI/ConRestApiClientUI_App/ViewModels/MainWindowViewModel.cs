using CommunityToolkit.Mvvm.Input;
using IdeaStatiCa.ConRestApiClientUI.Dialogs;
using IdeaStatiCa.ConRestApiClientUI.Services;
using IdeaStatiCa.ConRestApiClientUI.ViewModels;
using System.Threading.Tasks;
using System.Windows;

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
			ShowClientWndCommand = new AsyncRelayCommand(ShowClientWndAsync, CanShowClientWndAsync);
			CallScriptCommand = new AsyncRelayCommand(CallScriptAsync, CanCallScriptAsync);
			_webServer.StartAsync().ContinueWith(_ =>
			{
				RefreshCommands();
			});
		}

		public IAsyncRelayCommand ShowClientWndCommand { get; }


		public IAsyncRelayCommand CallScriptCommand { get; }

		private Window clientWindow;
		private Window ClientWindow
		{
			get => clientWindow;
			set => SetProperty(ref clientWindow, value);
		}

		private IConRestApiClientViewModel clientViewModel;
		private IConRestApiClientViewModel ClientViewModel
		{
			get => clientViewModel;
			set => SetProperty(ref clientViewModel, value);
		}

		private bool CanCallScriptAsync()
		{
			return ClientViewModel != null;
		}

		private async Task CallScriptAsync()
		{
			if(ClientViewModel.ClientHost is IScriptExecutor executor)
			{
				var res = await executor.ExecuteScriptAsync("alert('Hello from C#')");
			}
		}

		private bool CanShowClientWndAsync()
		{
			bool res = (_webServer?.IsListening == true) && (ClientWindow == null);
			return res;
		}
		private async Task ShowClientWndAsync()
		{
			if(ClientWindow != null)
			{
				ClientWindow.Activate();
				return;
			}

			ClientViewModel = _conApiVmProvider.CreateConApiClientViewModel();
			ClientWindow = _dialogService.GetDialog(ClientViewModel);
			//ClientWindow.Owner = Application.Current.MainWindow;

			ClientWindow.Closed += (s, e) =>
			{
				ClientViewModel = null;
				ClientWindow = null;
				RefreshCommands();
			};

			ClientWindow.Show();
			ClientWindow.Activate();

			RefreshCommands();

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
			this.CallScriptCommand.NotifyCanExecuteChanged();
		}
	}
}
