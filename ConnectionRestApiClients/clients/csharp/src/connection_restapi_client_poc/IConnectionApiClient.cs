﻿using connection_restapi_client_poc.Api;
using connection_restapi_client_poc.Model;
using System;
using System.Threading.Tasks;

namespace connection_restapi_client_poc
{
	/// <summary>
	/// Client for accessing IdeaStatiCa.ConnectionRestApi
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

		/// <summary>
		/// ClientID - assigned by the service
		/// </summary>
		string ClientId { get; }

		/// <summary>
		/// Id of the open project on the service side
		/// </summary>
		Guid ProjectId { get; }

		/// <summary>
		/// Get Calculation API
		/// </summary>
		ICalculationApiAsync Calculation { get; }

		/// <summary>
		/// Get Connection API
		/// </summary>
		IConnectionApiAsync Connection { get; }

		/// <summary>
		/// Get Export API
		/// </summary>
		IExportApiExtAsync Export { get; }

		/// <summary>
		/// Get LoadEffect API
		/// </summary>
		ILoadEffectApiAsync LoadEffect { get; }

		/// <summary>
		/// Get Material API
		/// </summary>
		IMaterialApiAsync Material { get; }

		/// <summary>
		/// Get Member API
		/// </summary>
		IMemberApiAsync Member { get; }

		/// <summary>
		/// Get Operation API
		/// </summary>
		IOperationApiAsync Operation { get; }

		/// <summary>
		/// Get Parameter API
		/// </summary>
		IParameterApiAsync Parameter { get; }

		/// <summary>
		/// Get Presentation API
		/// </summary>
		IPresentationApiAsync Presentation { get; }

		/// <summary>
		/// Get Project API
		/// </summary>
		IProjectApiExtAsync Project { get; }

		/// <summary>
		/// Get Report API
		/// </summary>
		IReportApiAsync Report { get; }

		/// <summary>
		/// Get Template API
		/// </summary>
		ITemplateApiAsync Template { get; }
	}
}
