using System.Runtime.InteropServices;


namespace WebGlSceneController
{
	public class WebGlPresenterApi
	{
		[DllImport("WebGlPresenter.dll", CharSet = CharSet.Ansi)]
		public static extern void OpenWindow();

		[DllImport("WebGlPresenter.dll", CharSet = CharSet.Ansi)]
		public static extern void ShowScene(string scene);
	}
}
