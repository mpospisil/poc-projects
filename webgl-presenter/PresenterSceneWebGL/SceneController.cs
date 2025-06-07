using System.Threading.Tasks;
using WebUI4CSharp;

namespace PresenterSceneWebGL
{
	public class SceneController
	{
		private bool isOpen = false;
		WebUIWindow WebUI_wnd { get; set; }

		public bool IsOpen { get => isOpen; set => isOpen = value; }

		public SceneController()
		{
			WebUI_wnd = new WebUIWindow();
			WebUI_wnd.SetRootFolder("C:\\deve\\poc-projects-2\\webgl-presenter\\frontend\\build");
			WebUI_wnd.SetSize(550, 450);
		}

		public Task OpenWindowAsync()
		{
			return Task.Run(() =>
			{
				WebUI_wnd.Show("index.html");
			});
		}

		public Task ShowSceneAsync(string sceneData)
		{
			return Task.Run(() =>
			{
				var javaScript = $"window.myExportedTypeScriptApi.myTypeScriptFunction('{sceneData}')";
				WebUI_wnd.Run(javaScript);
			});
		}
	}
}
