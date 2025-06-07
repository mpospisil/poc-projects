using System.Threading.Tasks;

namespace WebGlSceneController
{
	public class SceneController
	{
		private bool isOpen = false;

		public bool IsOpen { get => isOpen; set => isOpen = value; }

		public Task OpenWindowAsync()
		{
			return Task.Run(() =>
			{
				WebGlPresenterApi.OpenWindow();
				IsOpen = true;
			});
		}

		public Task ShowSceneAsync(string sceneData)
		{
			return Task.Run(() =>
			{
				var javaScript = $"window.myExportedTypeScriptApi.myTypeScriptFunction('{sceneData}')";
				WebGlPresenterApi.ShowScene(javaScript);
			});
		}
	}
}
