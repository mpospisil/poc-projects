using System;
using System.Runtime.CompilerServices;
using System.Runtime.InteropServices;


namespace WebGlPresenterApp
{
	public class WebGlPresenterApi
	{
		[DllImport("WebGlPresenter.dll", CharSet = CharSet.Ansi)]
		public static extern void OpenWindow();

		[DllImport("WebGlPresenter.dll", CharSet = CharSet.Ansi)]
		public static extern void ShowScene(string scene);
	}
}
