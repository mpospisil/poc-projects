using System.Diagnostics;

namespace IdeaStatiCa.ConRestApiClientUI
{
	public interface IClientHost
	{

	}

	[System.Runtime.InteropServices.ComVisible(true)]
	public class ClientHost : IClientHost
	{
		public void Run(string param)
		{
			Debug.WriteLine($"ClientHost.Run {param}");
		}
	}
}
