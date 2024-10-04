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
		/// Create an instance of IConnectionApiClient that is connected to the service which listens on <paramref name="uri"/>
		/// </summary>
		/// <returns>Instance of <see cref="IConnectionApiClient"/></returns>
		Task<IConnectionApiClient> CreateConnectionApiClient();
	}
}
