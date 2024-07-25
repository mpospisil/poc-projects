using System;
using System.Runtime.InteropServices;

namespace ConLibClientApp.Core.Services
{
	public class ConLibativeMethods
	{
		[DllImport("ConLibUI.dll", CharSet = CharSet.Unicode)]
		public static extern IntPtr GetPropose(string searchArg);

		[DllImport("ConLibUI.dll", CharSet = CharSet.Unicode)]
		public static extern void FreePropose(IntPtr pString);
	}
}
