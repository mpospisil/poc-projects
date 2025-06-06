using System;
using System.Runtime.InteropServices;


namespace WebGlPresenterApp
{
	public class WebGlPresenterApi
	{
		[DllImport("WebGlPresenter.dll", CharSet = CharSet.Ansi)]
		public static extern void ShowScene(string searchArg);
	}
}
