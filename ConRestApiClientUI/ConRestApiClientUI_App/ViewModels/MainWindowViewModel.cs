using CommunityToolkit.Mvvm.ComponentModel;
using CommunityToolkit.Mvvm.Input;
using IdeaStatiCa.ConRestApiClientUI;
using IdeaStatiCa.Plugin;
using Microsoft.Extensions.Configuration;
using Microsoft.Win32;
using System.IO;

namespace ConRestApiClientUI_App.ViewModels
{
	public interface IMainWindowViewModel
	{
		Task OnLoadAsync();
	}

	public class MainWindowViewModel : ObservableObject, IMainWindowViewModel
	{

		private readonly IConfiguration _configuration;
		private readonly IPluginLogger _logger;
		private readonly ISceneController _sceneController;

		public MainWindowViewModel(IConfiguration configuration,
			IPluginLogger logger,
			ISceneController sceneController)
		{
			this._configuration = configuration;
			this._logger = logger;
			this._sceneController =sceneController;

			OpenSceneWndCommand = new RelayCommand(OpenSceneWnd, () => true);
			PresentCommand = new RelayCommand(Present, () => true);
		}

		public async Task OnLoadAsync()
		{
			await Task.CompletedTask;
		}

		public RelayCommand OpenSceneWndCommand { get; }

		public RelayCommand PresentCommand { get; }

		private void OpenSceneWnd()
		{
			_logger.LogInformation("ShowIdeaStatiCaLogsAsync");
			_sceneController.ShowWindow();
		}

		private void Present()
		{
			_logger.LogInformation("Present");

			OpenFileDialog dialog = new OpenFileDialog();
			var res = dialog.ShowDialog();

			if(res == true)
			{
				var sceneData = File.ReadAllText(dialog.FileName);
				_sceneController.PresentAsync(sceneData);
			}

			
		}
	}
}
