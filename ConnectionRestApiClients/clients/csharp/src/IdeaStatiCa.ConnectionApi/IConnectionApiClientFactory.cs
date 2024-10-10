using System;
using System.Threading.Tasks;

namespace connection_restapi_client_poc
{
	/// <summary>
	/// Factory for creating instances of <see cref="IConnectionApiClient"/>
	/// </summary>
	public interface IConnectionApiClientFactory
	{
		/// <summary>
		/// Create an instance of IConnectionApiClient
		/// </summary>
		/// <returns>Instance of <see cref="IConnectionApiClient"/></returns>
		Task<IConnectionApiClient> CreateConnectionApiClient();
	}
}
