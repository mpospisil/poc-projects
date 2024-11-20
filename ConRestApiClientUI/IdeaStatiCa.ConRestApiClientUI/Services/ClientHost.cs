using System.Diagnostics;

namespace IdeaStatiCa.ConRestApiClientUI.Services
{
	[System.Runtime.InteropServices.ComVisible(true)]
	public class ClientHost : IClientHost
	{
		public void Run(string param)
		{
			Debug.WriteLine($"ClientHost.Run {param}");
		}
	}
}
