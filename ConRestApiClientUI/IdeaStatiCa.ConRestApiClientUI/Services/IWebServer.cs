using System.Threading.Tasks;

namespace IdeaStatiCa.ConRestApiClientUI.Services
{
	public interface IWebServer
	{
		Task StartAsync();
		Task StopAsync();

		string GetUrl();
	}
}
