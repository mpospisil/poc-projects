using System.Windows;


namespace IdeaStatiCa.ConRestApiClientUI
{
	/// <summary>
	/// Interaction logic for ConRestApiClientWnd.xaml
	/// </summary>
	public partial class ConRestApiClientWnd : Window
	{
		private readonly IConRestApiClientViewModel _viewModel;

		//private readonly C _sceneController2;
		public ConRestApiClientWnd(IConRestApiClientViewModel viewModel)
		{
			_viewModel = viewModel;
			this.DataContext = _viewModel;
			InitializeComponent();
			mainGrid.Children.Add(new IdeaWebGlScene3D(viewModel));
		}
	}
}
