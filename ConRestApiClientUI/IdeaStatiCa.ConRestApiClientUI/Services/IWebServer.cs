using System.Threading.Tasks;

namespace IdeaStatiCa.ConRestApiClientUI.Services
{
	/// <summary>
	/// Represents a web server interface with methods to start and stop the server,
	/// retrieve the server URL, and check if the server is currently listening.
	/// </summary>
	public interface IWebServer
	{
		/// <summary>
		/// Starts the web server asynchronously.
		/// </summary>
		/// <returns>A task that represents the asynchronous start operation.</returns>
		Task StartAsync();

		/// <summary>
		/// Stops the web server asynchronously.
		/// </summary>
		/// <returns>A task that represents the asynchronous stop operation.</returns>
		Task StopAsync();

		/// <summary>
		/// Gets the URL of the web server.
		/// </summary>
		/// <returns>The URL of the web server as a string.</returns>
		string GetUrl();

		/// <summary>
		/// Gets a value indicating whether the web server is currently listening for requests.
		/// </summary>
		bool IsListening { get; }
	}
}
