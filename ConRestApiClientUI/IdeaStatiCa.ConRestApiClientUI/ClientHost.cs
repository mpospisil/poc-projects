using System.Diagnostics;

namespace IdeaStatiCa.ConRestApiClientUI
{
	[System.Runtime.InteropServices.ComVisible(true)]
	public class ClientHost
	{
		public void Run(string param)
		{
			Debug.WriteLine($"ClientHost.Run {param}");
		}
	}
}
