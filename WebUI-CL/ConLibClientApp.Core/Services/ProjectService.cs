using ConLibClientApp.Core.Models;
using System.Threading.Tasks;

namespace ConLibClientApp.Core.Services
{
	public class ProjectService : IProjectService
	{
		public async Task<ProjectInfo> CreateProjectAsync()
		{
			var projInfo = new ProjectInfo() { Id = "1" };
			return await Task.FromResult(projInfo);
		}
	}
}
