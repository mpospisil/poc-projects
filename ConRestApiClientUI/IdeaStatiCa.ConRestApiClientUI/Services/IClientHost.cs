using System.Threading.Tasks;

namespace IdeaStatiCa.ConRestApiClientUI.Services
{
	/// <summary>
	/// Interface for executing scripts asynchronously.
	/// </summary>
	public interface IScriptExecutor
	{
		/// <summary>
		/// Executes a script asynchronously.
		/// </summary>
		/// <param name="script">The script to execute.</param>
		/// <returns>A task that represents the asynchronous operation. The task result contains the script execution result as a string.</returns>
		Task<string> ExecuteScriptAsync(string script);
	}

	/// <summary>
	/// Bridge between the .NET application and the script engine.
	/// </summary>
	public interface IClientHost
	{
		/// <summary>
		/// Attaches a script executor to the client host.
		/// </summary>
		/// <param name="scriptExecutor">The script executor to attach.</param>
		void AttachScriptExecutor(IScriptExecutor scriptExecutor);

		/// <summary>
		/// Detaches the script executor from the client host.
		/// </summary>
		void DetachScriptExecutor();
	}
}
