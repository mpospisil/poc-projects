using System.IO;
using System.Threading.Tasks;

namespace IdeaStatiCa.ConRestApiClientUI
{
	/// <summary>
	/// Responsible for controlling data which presented data in scene3D in <see cref="IdeaStatiCa.ConRestApiClientUI.IdeaWebGlScene3D"/>
	/// </summary>
	public interface ISceneController
	{
		/// <summary>
		/// Show the window contains  WPF Control <see cref="IdeaStatiCa.ConRestApiClientUI.IdeaWebGlScene3D"/>
		/// 
		/// </summary>
		void ShowWindow();

		/// <summary>
		/// Displays scene in the attached  WPF Control <see cref="IdeaStatiCa.ConRestApiClientUI.IdeaWebGlScene3D"/>
		/// </summary>
		/// <param name="sceneData"></param>
		/// <returns></returns>
		Task PresentAsync(string sceneData);

		Task<Stream> CaptureSceneAsImage();
	}
}
