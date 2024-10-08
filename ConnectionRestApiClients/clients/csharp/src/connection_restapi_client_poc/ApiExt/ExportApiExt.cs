﻿using System;
using System.IO;
using System.Threading.Tasks;

namespace connection_restapi_client_poc.Api
{
	/// <summary>
	/// 
	/// </summary>
	public interface IExportApiExtAsync : IExportApiAsync
	{
		/// <summary>
		/// Save the connection to the IFC format
		/// </summary>
		/// <param name="projectId">Identifier of the open connection project in the service</param>
		/// <param name="connectionId">ID of the connection in <paramref name="projectId"/></param>
		/// <param name="filePath">The full path to the IFC file which will be created</param>
		/// <returns></returns>
		Task ExportConToIfcFileAsync(Guid projectId, int connectionId, string filePath);
	}

	/// <inheritdoc cref="IExportApiExtAsync" />
	public class ExportApiExt : ExportApi, IExportApiExtAsync
	{
		/// <summary>
		/// Constructor
		/// </summary>
		/// <param name="client"></param>
		/// <param name="asyncClient"></param>
		/// <param name="configuration"></param>
		public ExportApiExt(connection_restapi_client_poc.Client.ISynchronousClient client, connection_restapi_client_poc.Client.IAsynchronousClient asyncClient, connection_restapi_client_poc.Client.IReadableConfiguration configuration) : base(client, asyncClient, configuration)
		{
		}

		/// <inheritdoc cref="IExportApiExtAsync.ExportConToIfcFileAsync(Guid, int, string)"/>/param>
		/// <returns></returns>
		public async Task ExportConToIfcFileAsync(Guid projectId, int connectionId, string filePath)
		{
			var response = await base.ExportConnectionIFCWithHttpInfoAsync(projectId, connectionId, "text/plain");
			string ifc = (string)response.Data;

			// Write the string to the file
#if NETSTANDARD2_1_OR_GREATER
			await File.AppendAllTextAsync(filePath, ifc);
#else
			File.WriteAllText(filePath, ifc);
#endif
		}
	}
}
