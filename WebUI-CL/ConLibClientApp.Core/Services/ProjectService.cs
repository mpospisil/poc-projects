using ConLibClientApp.Core.Models;
using System;
using System.Diagnostics;
using System.Runtime.InteropServices;
using System.Threading.Tasks;

namespace ConLibClientApp.Core.Services
{
	public class ProjectService : IProjectService
	{
		public async Task<ProjectInfo> CreateProjectAsync()
		{
			string arg = "Martin XXX";
			IntPtr resultPtr = ConLibativeMethods.GetPropose(arg);
			if(resultPtr == IntPtr.Zero)
			{
				throw new Exception("No proposal");
			}

			var result = Marshal.PtrToStringUni(resultPtr);

			string resultCopy = result!;

			ConLibativeMethods.FreePropose(resultPtr);

			Debug.WriteLine(resultCopy);

			var projInfo = new ProjectInfo() { Id = "1" };
			return await Task.FromResult(projInfo);
		}
	}
}
