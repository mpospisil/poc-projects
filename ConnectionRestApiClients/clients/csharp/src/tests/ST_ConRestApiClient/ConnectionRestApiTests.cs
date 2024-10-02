using connection_restapi_client_poc;
using FluentAssertions;

namespace ST_ConRestApiClient
{
	public class ConnectionRestApiTests : ConRestApiBaseTest
	{
		[SetUp]
		public async Task SetUp()
		{
			//if (this.RunServer)
			//{
			//	ConnectionApiClient = await ApiFactory.CreateConnectionApiClient();
			//}
			//else
			//{
			//	if (ApiUri == null)
			//	{
			//		throw new Exception("ApiUri is not set");
			//	}

			//	ConnectionApiClient = await ApiFactory.CreateConnectionApiClient(ApiUri);
			//}

			ConnectionApiClient = await ApiFactory.CreateConnectionApiClient();

			string connProjectFilePath = Path.Combine(ProjectPath, "Simple-1-ECEN.ideaCon");
			this.Project = await ConnectionApiClient.OpenProjectAsync(connProjectFilePath);
			this.ActiveProjectId = Project.ProjectId;
			if (this.ActiveProjectId == Guid.Empty)
			{
				throw new Exception("Project is not opened");
			}

			this.Project = await ConnectionApiClient.Project.GetProjectDataAsync(ActiveProjectId);

			Project.Should().NotBeNull();
			Project.ProjectId.Should().NotBe(Guid.Empty);
		}

		[TearDown]
		public void TearDown()
		{
			if (ConnectionApiClient != null)
			{
				ConnectionApiClient.Dispose();
			}
		}

		[Test]
		public async Task ShouldGetConProjectData()
		{
			var projectData = await ConnectionApiClient!.Project.GetProjectDataAsync(ActiveProjectId);

			projectData.Should().NotBeNull();
			projectData.ProjectInfo.Name.Should().Be("Name - Simple-1-ECEN");
			projectData.ProjectInfo.Description.Should().Be("Description - Simple-1-ECEN");
			projectData.ProjectInfo.ProjectNumber.Should().Be("12345");
		}
	}
}