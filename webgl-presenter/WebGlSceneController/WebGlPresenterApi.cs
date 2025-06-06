using System.Runtime.InteropServices;


namespace WebGlSceneController
{
	internal class WebGlPresenterApi
	{
		[DllImport("WebGlPresenter.dll", CharSet = CharSet.Ansi)]
		internal static extern void OpenWindow();

		[DllImport("WebGlPresenter.dll", CharSet = CharSet.Ansi)]
		internal static extern void ShowScene(string scene);
	}
}
