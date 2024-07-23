using ConLibClientApp.Core.Models;
using System.Threading.Tasks;

namespace ConLibClientApp.Core.Services
{
	public interface IProjectService
	{
		public Task<ProjectInfo> CreateProjectAsync();
	}
}
