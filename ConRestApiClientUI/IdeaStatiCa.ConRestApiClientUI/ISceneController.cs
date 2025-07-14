using System.Threading.Tasks;

namespace IdeaStatiCa.ConRestApiClientUI
{
	public interface ISceneController
	{
		void ShowWindow();
		Task PresentAsync(string sceneData);
	}
}
