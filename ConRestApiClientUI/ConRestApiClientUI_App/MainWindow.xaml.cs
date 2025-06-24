using System.Windows;
using IdeaStatiCa.ConRestApiClientUI;
using Microsoft.Extensions.Configuration;

namespace ConRestApiClientUI_App
{
	/// <summary>
	/// Interaction logic for MainWindow.xaml
	/// </summary>
	public partial class MainWindow : Window
	{
		private readonly SceneController _sceneController;

		public MainWindow(IConfiguration configuration)
		{
			this._sceneController = new SceneController(configuration);
			InitializeComponent();
		}

		private void button_Click(object sender, RoutedEventArgs e)
		{
			_sceneController.ShowWindowAsync();
		}
	}
}