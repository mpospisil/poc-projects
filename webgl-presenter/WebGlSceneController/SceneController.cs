using System.Threading.Tasks;

namespace WebGlSceneController
{
	public class SceneController
	{
		private bool isOpen = false;
		public Task OpenWindowAsync()
		{
			return Task.Run(() =>
			{
				isOpen = true;
				WebGlPresenterApi.OpenWindow();
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
