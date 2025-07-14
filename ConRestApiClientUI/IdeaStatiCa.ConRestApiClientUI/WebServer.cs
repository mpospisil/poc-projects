using System;
using System.IO;
using System.Net;
using System.Text;
using System.Threading.Tasks;

namespace IdeaStatiCa.ConRestApiClientUI
{
	public interface IWebServer
	{
		void Start(string url);
	}


	public class WebServer : IDisposable, IWebServer
	{
		private bool disposedValue;
		private readonly HttpListener _listener;
		private readonly string _rootDir;
		private Task ListenerTask { get; set; }

		public WebServer(string rootDir)
		{
			_rootDir = rootDir;
			_listener = new HttpListener();
		}

		public void Start(string url)
		{
			if (_listener.IsListening)
			{
				throw new InvalidOperationException("The server is already running.");
			}

			string baseDirectory = Path.Combine(AppDomain.CurrentDomain.BaseDirectory, _rootDir);
			string prefix = url;

			_listener.Prefixes.Add(prefix);
			_listener.Start();

			ListenerTask = Task.Run(async () => 
			{
					while (true)
					{
						HttpListenerContext context = await _listener.GetContextAsync();
						HttpListenerRequest request = context.Request;
						HttpListenerResponse response = context.Response;

						string filePath = Path.Combine(baseDirectory, request.Url.LocalPath.TrimStart('/'));
						if (File.Exists(filePath))
						{
							byte[] fileBytes = File.ReadAllBytes(filePath);
							response.ContentType = GetContentType(filePath);
							response.ContentLength64 = fileBytes.Length;
							await response.OutputStream.WriteAsync(fileBytes, 0, fileBytes.Length);
						}
						else
						{
							response.StatusCode = (int)HttpStatusCode.NotFound;
							byte[] errorBytes = Encoding.UTF8.GetBytes("404 - File Not Found");
							response.ContentLength64 = errorBytes.Length;
							await response.OutputStream.WriteAsync(errorBytes, 0, errorBytes.Length);
						}

						response.OutputStream.Close();
					}
			});
		}

		private static string GetContentType(string filePath)
		{
			string extension = Path.GetExtension(filePath).ToLowerInvariant();
			switch (extension)
			{
				case ".html":
					return "text/html";
				case ".css":
					return "text/css";
				case ".js":
					return "application/javascript";
				case ".png":
					return "image/png";
				case ".jpg":
					return "image/jpeg";
				case ".gif":
					return "image/gif";
				default:
					return "application/octet-stream";
			}
		}

		protected virtual void Dispose(bool disposing)
		{
			if (!disposedValue)
			{
				if (disposing)
				{
					if(_listener.IsListening)
					{
						_listener.Stop();
					}

					if (_listener is IDisposable disposable)
					{
						disposable.Dispose();
				}

				// TODO: free unmanaged resources (unmanaged objects) and override finalizer
				// TODO: set large fields to null
				disposedValue = true;
			}
		}

		// // TODO: override finalizer only if 'Dispose(bool disposing)' has code to free unmanaged resources
		// ~WebServer()
		// {
		//     // Do not change this code. Put cleanup code in 'Dispose(bool disposing)' method
		//     Dispose(disposing: false);
		}

		public void Dispose()
		{
			// Do not change this code. Put cleanup code in 'Dispose(bool disposing)' method
			Dispose(disposing: true);
			GC.SuppressFinalize(this);
		}
	}
}
