using CommunityToolkit.Mvvm.Input;
using ConLibClientApp.Core.Services;
using System.Threading.Tasks;

namespace ConLibClientApp.ViewModels.Core
{
	public class MainWindowViewModel : ViewModelBase
	{
		private readonly IProjectService projectService;
		public MainWindowViewModel(IProjectService projectService)
		{
			this.projectService = projectService;
			DoSomethingCommand = new AsyncRelayCommand<string>(DoSomethingAsync, CanDoSomethingAsync);
		}

		public IAsyncRelayCommand<string> DoSomethingCommand { get; }

		private bool CanDoSomethingAsync(string? name)
		{
			return true;
		}

		private async Task DoSomethingAsync(string? name)
		{
			var projInfo = await projectService.CreateProjectAsync();
			Status = projInfo.Id;
		}

		private string? status;
		public string? Status
		{
			get => status;
			set => SetProperty(ref status, value);
		}
	}
}
