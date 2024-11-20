using System;
using System.IO;
using System.Net;
using System.Text;
using System.Threading;
using System.Threading.Tasks;

namespace IdeaStatiCa.ConRestApiClientUI.Services
{
	public class WebServer : IWebServer
	{
		private HttpListener _listener;
		private readonly string _rootDir;
		CancellationTokenSource _cts;
		private string _url;
		Task _executionTask;

		public WebServer(string url = "http://localhost:8080/", string rootDir = null)
		{
			_url = url;
			_cts = new CancellationTokenSource();
			if (!string.IsNullOrEmpty(rootDir))
			{
				_rootDir = rootDir;
			}
			else
			{
				_rootDir = Path.Combine(AppDomain.CurrentDomain.BaseDirectory, "static");
			}
			_listener = new HttpListener();
		}

		public async Task StartAsync()
		{
			if (_listener.IsListening)
			{
				throw new InvalidOperationException("The server is already running.");
			}

			_listener.Prefixes.Add(_url);
			_listener.Start();

			var token = _cts.Token;

			_executionTask = Task.Run(async () => 
			{
				while (!token.IsCancellationRequested)
				{
					try
					{
						HttpListenerContext context = await _listener.GetContextAsync();
						HttpListenerRequest request = context.Request;
						HttpListenerResponse response = context.Response;

						string filePath = Path.Combine(_rootDir, request.Url.LocalPath.TrimStart('/'));
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
					catch
					{
					}
				}
			}, token);


			await Task.CompletedTask;
		}

		public async Task StopAsync()
		{
			if(_cts != null)
			{
				if (_listener?.IsListening == true)
				{
					_listener.Stop();
					_listener = null;
				}

				_cts.Cancel();

				if (_executionTask != null)
				{
					await _executionTask;
				}

				_executionTask = null;
				_cts.Dispose();
				_cts = null;
			}
		}

		public string GetUrl()
		{
			return _url;
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
	}
}
