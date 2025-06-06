using System.Threading.Tasks;

namespace WebGlSceneController
{
	public class SceneController
	{
		public Task OpenWindowAsync()
		{
			return Task.Run(() =>
			{
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
