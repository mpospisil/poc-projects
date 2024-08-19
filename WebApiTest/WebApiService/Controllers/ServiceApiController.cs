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


		/// <summary>
		/// Uploads a binary file.
		/// </summary>
		/// <param name="file">The binary file to upload.</param>
		/// <returns>A JSON object indicating the result of the upload.</returns>
		[HttpPost("upload")]
		[ProducesResponseType(200)]
		[ProducesResponseType(400)]
		public async Task<IActionResult> UploadFile(IFormFile file)
		{
			if (file == null || file.Length == 0)
			{
				return BadRequest(new { message = "File is empty or not provided." });
			}

			using (var stream = new MemoryStream())
			{
				await file.CopyToAsync(stream);
			}

			return Ok(new { message = "File uploaded successfully.", fileName = file.FileName, fileSize = file.Length });
		}
	}
}
