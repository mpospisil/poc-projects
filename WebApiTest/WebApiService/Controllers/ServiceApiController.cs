using Microsoft.AspNetCore.Mvc;

namespace MyApi.Controllers
{
	[ApiController]
	[Route("api/[controller]")]
	public class ServiceApiController : ControllerBase
	{
		/// <summary>
		/// Gets a list of values.
		/// </summary>
		/// <returns>A list of strings.</returns>
		[HttpGet]
		[ProducesResponseType(typeof(IEnumerable<string>), 200)]
		public IActionResult GetValues()
		{
			var values = new List<string> { "value1", "value2" };
			return Ok(values);
		}
	}
}
