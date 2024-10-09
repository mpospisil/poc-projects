using connection_restapi_client_poc;
using connection_restapi_client_poc.Api;
using connection_restapi_client_poc.Model;

namespace GenerateReport
{
    internal class Program
    {
        static async Task Main(string[] args)
        {

            ConnectionApiClientFactory clientFactory = new ConnectionApiClientFactory("http://localhost:5000");
            
            ConnectionApiClient conclient = (ConnectionApiClient)await clientFactory.CreateConnectionApiClient();

            try
            {
                string filePath = "inputs/HSS_norm_cond.ideaCon";
                ConProject conProject = await conclient.Project.OpenProjectFromFileAsync(filePath);

                //Get projectId Guid
                Guid projectId = conProject.ProjectId;
                var connections = await conclient.Connection.GetAllConnectionsDataAsync(projectId);
                int connectionId = connections[0].Id;

                //TO DO - FIX REPORT GENERATION
                //Generate Report
                //conclient.Report.GeneratePdfAsync()


                //Change Member Size



                //Generate Report Again



                string saveFilePath = "member-size-update.ideaCon";

                await conclient.Project.SaveProjectAsync(projectId, saveFilePath);
            }
            catch (Exception ex)
            {
            }
        }
    }
}