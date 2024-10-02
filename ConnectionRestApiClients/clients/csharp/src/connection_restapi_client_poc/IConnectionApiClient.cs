using connection_restapi_client_poc.Api;
using connection_restapi_client_poc.Model;
using System;
using System.Threading.Tasks;

namespace connection_restapi_client_poc
{
	/// <summary>
	/// 
	/// </summary>
	public interface IConnectionApiClient : IDisposable
#if NETSTANDARD2_1_OR_GREATER
		, IAsyncDisposable
#endif
	{
		/// <summary>
		/// Open idea connection project in ConnectionRestApi service
		/// </summary>
		/// <param name="path">Idea con file</param>
		/// <returns></returns>
		Task<ConProject> OpenProjectAsync(string path);

		string ClientId { get; }

		Guid ProjectId { get; }

		ICalculationApiAsync Calculation { get; }
		IExportApiAsync Export { get; }
		ILoadEffectApiAsync LoadEffect { get; }
		IMaterialApiAsync Material { get; }
		IMemberApiAsync Member { get; }
		IOperationApiAsync Operation { get; }
		IParameterApiAsync Parameter { get; }
		IPresentationApiAsync Presentation { get; }
		IProjectApiAsync Project { get; }
		IReportApiAsync Report { get; }
		ITemplateApiAsync Template { get; }
	}
}
