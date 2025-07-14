using System.Diagnostics;
using System.Runtime.InteropServices;

namespace IdeaStatiCa.ConRestApiClientUI
{
	public interface IClientHost
	{

	}

	[System.Runtime.InteropServices.ComVisible(true)]
	[ClassInterface(ClassInterfaceType.AutoDual)]
	public class ClientHost : IClientHost
	{
		public void Run(string param)
		{
			Debug.WriteLine($"ClientHost.Run {param}");
		}

		public void PageLoaded()
		{

			Debug.WriteLine($"PageLoaded");
		}
	}
}
