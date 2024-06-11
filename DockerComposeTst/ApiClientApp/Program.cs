using System.Net.Http.Json;

namespace ApiClientApp
{
	internal class Program
	{
		static async void Main(string[] args)
		{
			Console.WriteLine("Hello, World!");

			HttpClient client = new HttpClient();
			using (HttpResponseMessage response = await client.GetAsync("https://localhost:5001/WeatherForecast"))
			{
				response.Content.ReadAsStreamAsync().Result.CopyTo(Console.OpenStandardOutput());
			}
		}
	}
}
