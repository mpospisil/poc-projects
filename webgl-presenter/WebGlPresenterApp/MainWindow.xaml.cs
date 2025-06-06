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
			return Task.Run(() =>
			{
				WebGlPresenterApi.OpenWindow();
			});
		}

		private void button1_Click(object sender, RoutedEventArgs e)
		{
			ShowAsync();
		}


		private Task ShowAsync()
		{
			//return Task.Run(() =>
			//{
			//	WebGlPresenterApi.ShowScene("window.myExportedTypeScriptApi.myTypeScriptFunction('xxxxxxxxx')");
			//});

			var dlg = new OpenFileDialog();
			if (dlg.ShowDialog() != true)
			{
				return Task.CompletedTask;
			}

			var sceenData = File.ReadAllText(dlg.FileName);
			return Task.Run(() =>
			{
				var javaScript = $"window.myExportedTypeScriptApi.myTypeScriptFunction('{sceenData}')";
				WebGlPresenterApi.ShowScene(javaScript);
			});
		}
	}
}