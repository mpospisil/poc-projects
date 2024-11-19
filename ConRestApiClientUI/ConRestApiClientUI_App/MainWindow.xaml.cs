using System.Windows;
using IdeaStatiCa.ConRestApiClientUI;

namespace ConRestApiClientUI_App
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
			var dlg = new ConRestApiClientWnd();
			dlg.ShowDialog();
		}
	}
}