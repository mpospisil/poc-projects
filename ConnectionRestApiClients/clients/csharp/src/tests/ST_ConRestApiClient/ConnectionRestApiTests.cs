using connection_restapi_client_poc;
using connection_restapi_client_poc.Model;
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

		[Test]
		public async Task ShouldCloseProject()
		{
			await ConnectionApiClient!.Project!.CloseProjectAsync(ActiveProjectId.ToString());
		}

		[Test]
		public async Task ShouldGetConnections()
		{
			var connections = await ConnectionApiClient!.Connection!.GetAllConnectionsDataAsync(ActiveProjectId);
			connections.Should().NotBeNull();
			connections.Count.Should().Be(3);

			var con1 = connections[0];
			con1.Id.Should().Be(1);
			con1.AnalysisType.Should().Be(ConAnalysisTypeEnum.StressStrain);
			con1.Name.Should().Be("1Col-2Beams-Welded");
			con1.Description.Should().Be("Welded connection");

			var con2 = connections[1];
			con2.Id.Should().Be(2);
			con2.AnalysisType.Should().Be(ConAnalysisTypeEnum.Stiffness);

			var con3 = connections[2];
		}

		[Test]
		public async Task ShouldGetConnection()
		{
			// request connection id = 2
			var con2 = await ConnectionApiClient!.Connection!.GetConnectionDataAsync(ActiveProjectId, 2);
			con2.Id.Should().Be(2);
			con2.AnalysisType.Should().Be(ConAnalysisTypeEnum.Stiffness);
		}

		[Test]
		public async Task ShouldDownloadConnection()
		{
			string tempFileName = Path.GetTempFileName()!;
			try
			{
				await ConnectionApiClient!.Project!.DownloadProjectAsync(ActiveProjectId, tempFileName);

				bool fileExists = File.Exists(tempFileName);
				fileExists.Should().BeTrue("Ideacon project should be downloaded");

				FileInfo fileInfo = new FileInfo(tempFileName);
				long fileSize = fileInfo.Length;

				fileSize.Should().BeGreaterThan(0, "The downloaded file should not be empty");
			}
			finally
			{
				File.Delete(tempFileName);
			}
		}

		public async Task ShouldUpdateConnection()
		{
			const string NewConnectionName = "Updated name";
			var con1 = await ConnectionApiClient!.Connection!.GetConnectionDataAsync(ActiveProjectId, 1);
			con1.Id.Should().Be(1);

			con1.Name.Should().Be("1Col-2Beams-Welded");
			con1.Name = NewConnectionName;

			var updatedConnection1 = await ConnectionApiClient!.Connection!.UpdateConnectionDataAsync(ActiveProjectId, 1, con1);

			updatedConnection1.Id.Should().Be(1);
			updatedConnection1.Name.Should().Be(NewConnectionName, "The data in the response should include updated name of connection");

			var con1_updated = await ConnectionApiClient!.Connection!.GetConnectionDataAsync(ActiveProjectId, 1);
			updatedConnection1.Id.Should().Be(1);
			updatedConnection1.Name.Should().Be(NewConnectionName, "The change should be persistent");
		}

		[Test]
		public async Task ShouldGetConnectionIOMModel()
		{
			var con1 = await ConnectionApiClient!.Connection!.GetConnectionDataAsync(ActiveProjectId, 1);
			var conData = await ConnectionApiClient!.Export!.ExportConnectionDataAsync(ActiveProjectId, con1.Id);
			conData.Should().NotBeNull();
		}

		//[Test]
		//public async Task ShouldGetAllMembers()
		//{
		//	var members = await ConnApiController!.GetMembersAsync(1, CancellationToken.None);
		//	members.Count.Should().Be(3);

		//	var mem1 = members[0];
		//	mem1.Id.Should().Be(1);
		//	mem1.Name.Should().Be("C");
		//	mem1.CrossSectionId.Should().Be(1);
		//	mem1.Active.Should().BeTrue();
		//	mem1.IsBearing.Should().BeTrue();
		//	mem1.IsContinuous.Should().BeTrue();
		//	mem1.MirrorY.Should().BeFalse();
		//	mem1.MirrorZ.Should().BeFalse();

		//	var mem2 = members[1];
		//	mem2.Id.Should().Be(2);
		//	mem2.Name.Should().Be("B1");
		//	mem2.CrossSectionId.Should().Be(2);
		//	mem2.Active.Should().BeTrue();
		//	mem2.IsBearing.Should().BeFalse();
		//	mem2.IsContinuous.Should().BeFalse();
		//	mem2.MirrorY.Should().BeFalse();
		//	mem2.MirrorZ.Should().BeFalse();

		//	var mem3 = members[2];
		//	mem3.Id.Should().Be(3);
		//	mem3.Name.Should().Be("B2");
		//	mem3.CrossSectionId.Should().Be(3);
		//	mem3.Active.Should().BeTrue();
		//	mem3.IsBearing.Should().BeFalse();
		//	mem3.IsContinuous.Should().BeFalse();
		//	mem3.MirrorY.Should().BeFalse();
		//	mem3.MirrorZ.Should().BeFalse();
		//}

		//[Test]
		//public async Task ShouldGetOneMember()
		//{
		//	var member = await ConnApiController!.GetMemberAsync(1, 1, CancellationToken.None);

		//	member.Id.Should().Be(1);
		//	member.Name.Should().Be("C");
		//	member.CrossSectionId.Should().Be(1);
		//	member.Active.Should().BeTrue();
		//	member.IsBearing.Should().BeTrue();
		//	member.IsContinuous.Should().BeTrue();
		//	member.MirrorY.Should().BeFalse();
		//	member.MirrorZ.Should().BeFalse();
		//}

		//[Test]
		//public async Task SetBearingMember()
		//{
		//	var member = await ConnApiController!.GetMemberAsync(1, 1, CancellationToken.None);

		//	member.Id.Should().Be(1);
		//	member.Name.Should().Be("C");
		//	member.CrossSectionId.Should().Be(1);
		//	member.Active.Should().BeTrue();
		//	member.IsBearing.Should().BeTrue();
		//	member.IsContinuous.Should().BeTrue();
		//	member.MirrorY.Should().BeFalse();
		//	member.MirrorZ.Should().BeFalse();

		//	var bearingMember = await ConnApiController!.SetBearingMemberAsync(1, 2, CancellationToken.None);
		//	bearingMember.IsBearing.Should().BeTrue();

		//	member = await ConnApiController!.GetMemberAsync(1, 1, CancellationToken.None);
		//	member.IsBearing.Should().BeFalse();
		//}

		//[Test]
		//public async Task ShouldUpdateMember()
		//{
		//	var member = await ConnApiController!.GetMemberAsync(3, 1, CancellationToken.None);

		//	member.Name = "D";
		//	member.CrossSectionId = 2;
		//	member.IsContinuous = false;
		//	member.MirrorY = true;
		//	member.MirrorZ = true;

		//	var updatedMember = await ConnApiController!.UpdateMemberAsync(3, 1, member, CancellationToken.None);
		//	updatedMember.Name.Should().Be("D");
		//	updatedMember.CrossSectionId?.Should().Be(2);
		//	updatedMember.IsContinuous.Should().BeFalse();
		//	updatedMember.MirrorY.Should().BeTrue();
		//	updatedMember.MirrorZ.Should().BeTrue();
		//}


		//[Test]
		//public async Task ShouldGetConnectionIOMConnectionData()
		//{
		//	var con1 = Project!.Connections.First();
		//	con1.Id.Should().Be(1);

		//	var connectionData = await ConnApiController!.ExportConnectionIomConnectionData(1, CancellationToken.None);
		//	connectionData.Should().NotBeNull();
		//}

		//[Test]
		//public async Task ShouldExportConnectionToIfc()
		//{
		//	var con1 = Project!.Connections.First();
		//	con1.Id.Should().Be(1);

		//	using (var ifcDataStream = await ConnApiController!.ExportToIfcAsync(con1.Id, CancellationToken.None))
		//	{
		//		ifcDataStream.Should().NotBeNull();
		//		ifcDataStream.Length.Should().BeGreaterThan(0);
		//	}
		//}

		//[Test]
		//public async Task ShouldCalculateStressStrain()
		//{
		//	var con1 = Project!.Connections.First();
		//	con1.Id.Should().Be(1);

		//	List<int> conToCalc = new List<int>() { con1.Id };
		//	var cbfemResults = await ConnApiController!.CalculateAsync(conToCalc);
		//	cbfemResults.Should().NotBeNull();
		//	cbfemResults.Count.Should().Be(1);
		//	var res1 = cbfemResults[0];
		//	res1.Passed.Should().BeTrue();
		//	res1.ResultSummary.Count.Should().Be(4);
		//}

		//[Test]
		//public async Task ShouldCalculateBuckling()
		//{
		//	var con1 = Project!.Connections.First();
		//	con1.Id.Should().Be(1);

		//	List<int> conToCalc = new List<int>() { con1.Id };
		//	var cbfemResults = await ConnApiController!.CalculateAsync(conToCalc, ConAnalysisTypeEnum.Buckling);
		//	cbfemResults.Should().NotBeNull();
		//	cbfemResults.Count.Should().Be(1);
		//	var res1 = cbfemResults[0];
		//	res1.Passed.Should().BeTrue();
		//	res1.ResultSummary.Count.Should().Be(4);

		//	//check buckling
		//	var bucklingResult = res1.ResultSummary.Last();
		//	bucklingResult.Skipped.Should().BeFalse();
		//	bucklingResult.Name.Equals("Buckling");
		//}

		//[Test]
		//public async Task ShouldGetResult()
		//{
		//	string connProjectFilePath = Path.Combine(ProjectPath, "Parametric.ideaCon");
		//	var project = await ConnApiController!.OpenProjectAsync(connProjectFilePath, CancellationToken.None);

		//	var con1 = project.Connections.First();
		//	List<int> conToCalc = new List<int>() { con1.Id };

		//	var cbfemResults = await ConnApiController!.ResultsAsync(conToCalc, CancellationToken.None);
		//	cbfemResults.Should().BeEmpty();

		//	await ConnApiController.CalculateAsync(conToCalc, ConAnalysisTypeEnum.Stress_Strain);

		//	cbfemResults = await ConnApiController!.ResultsAsync(conToCalc, CancellationToken.None);
		//	cbfemResults.Should().NotBeEmpty();

		//}

		//[Test]
		//public async Task ShouldGetProductionCost()
		//{
		//	var con1 = Project!.Connections.First();
		//	var cost = await ConnApiController!.GetProductionCostAsync(con1.Id, CancellationToken.None);
		//	cost.Should().NotBeNull();
		//	cost.TotalEstimatedCost.Should().BeGreaterThan(0);
		//}

		//[Test]
		//public async Task ShouldGetAndUpdateConnectionSetup()
		//{
		//	var connectionSetup = await ConnApiController!.GetConnectionSetupAsync(CancellationToken.None);

		//	connectionSetup.HssLimitPlasticStrain.Should().Be(0.01);

		//	connectionSetup.HssLimitPlasticStrain = 0.02;

		//	var updateResponse = await ConnApiController!.UpdateConnectionSetupAsync(connectionSetup, CancellationToken.None);

		//	var updatedConnectionSetup = await ConnApiController!.GetConnectionSetupAsync(CancellationToken.None);

		//	updatedConnectionSetup.HssLimitPlasticStrain.Should().Be(0.02);
		//}

		//[Test]
		//public async Task ShouldGetSceneData()
		//{
		//	var con1 = Project!.Connections.First();
		//	var sceneData = await ConnApiController!.GetDataScene3DAsync(con1.Id);
		//	sceneData.Should().NotBeNull();
		//	sceneData.Should().NotBeEmpty();
		//}

	}
}