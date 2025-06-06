using Microsoft.Win32;
using System.IO;
using System.Windows;
using WebGlSceneController;

namespace WebGlPresenterApp
{
	/// <summary>
	/// Interaction logic for MainWindow.xaml
	/// </summary>
	public partial class MainWindow : Window
	{
		SceneController sceneController = new SceneController();

		public MainWindow()
		{
			InitializeComponent();
		}

		private void button_Click(object sender, RoutedEventArgs e)
		{
			OpenWindowAsync();
		}

		private Task OpenWindowAsync()
		{
			return sceneController.OpenWindowAsync();
		}

		private void button1_Click(object sender, RoutedEventArgs e)
		{
			ShowAsync();
		}


		private Task ShowAsync()
		{
			var dlg = new OpenFileDialog();
			if (dlg.ShowDialog() != true)
			{
				return Task.CompletedTask;
			}

			var scenData = File.ReadAllText(dlg.FileName);
			return sceneController.ShowSceneAsync(scenData);
		}
	}
}