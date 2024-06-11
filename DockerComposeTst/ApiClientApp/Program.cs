using System.Net.Http.Json;

namespace ApiClientApp
{
	internal class Program
	{
		static async Task<int> Main(string[] args)
		{
			Console.WriteLine("Hello, World!");

			HttpClient client = new HttpClient();
			using (HttpResponseMessage response = await client.GetAsync("http://apiservice:8080/WeatherForecast"))
			{
				using (Stream stream = await response.Content.ReadAsStreamAsync())
				using (StreamReader reader = new StreamReader(stream))
				{
					string result = await reader.ReadToEndAsync();
					Console.WriteLine(result);
				}
			}

			return 0;
		}
	}
}
