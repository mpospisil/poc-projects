using System.Diagnostics;
using System.Threading.Tasks;

namespace IdeaStatiCa.ConRestApiClientUI.Services
{
	[System.Runtime.InteropServices.ComVisible(true)]
	public class ClientHost : IClientHost, IScriptExecutor
	{
		private IScriptExecutor _attachedScriptExecutor;

		public void AttachScriptExecutor(IScriptExecutor scriptExecutor)
		{
			this._attachedScriptExecutor = scriptExecutor;
		}

		public void DetachScriptExecutor()
		{
			this._attachedScriptExecutor = null;
		}

		public Task<string> ExecuteScriptAsync(string script)
		{
			if(this._attachedScriptExecutor == null)
			{
				throw new System.InvalidOperationException("No script executor attached.");
			}

			return this._attachedScriptExecutor.ExecuteScriptAsync(script);
		}

		public void Run(string param)
		{
			Debug.WriteLine($"ClientHost.Run {param}");
		}
	}
}
