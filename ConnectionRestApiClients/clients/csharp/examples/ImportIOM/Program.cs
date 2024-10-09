using connection_restapi_client_poc.Model;
using connection_restapi_client_poc;

namespace ImportIOM
{
    internal class Program
    {
        static async Task Main(string[] args)
        {
            ConnectionApiClientFactory clientFactory = new ConnectionApiClientFactory("http://localhost:5000");

            ConnectionApiClient conclient = (ConnectionApiClient)await clientFactory.CreateConnectionApiClient();

            try
            {
                //TO DO: FIX IOM IMPORT

                //string filePath = "inputs/mulitple_connections.xml";
                //ConProject conProject = await conclient.Project.CreateProjectFromIomFileAsync(filePath);

                ////Get projectId Guid
                //Guid projectId = conProject.ProjectId;
                //var connections = await conclient.Connection.GetAllConnectionsDataAsync(projectId);
                //int connectionId = connections[0].Id;

                ////FIX Parameter --> Params
                //ConCalculationParameter calculationParams = new ConCalculationParameter();
                //calculationParams.ConnectionIds = new List<int> { connectionId };
                //List<ConResultSummary> results = await conclient.Calculation.CalculateAsync(projectId, calculationParams);

                //string saveFilePath = "connection-file-from-IOM.ideaCon";

                //await conclient.Project.SaveProjectAsync(projectId, saveFilePath);

            }
            catch (Exception ex)
            {
            }
        }
    }
}