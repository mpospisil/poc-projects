using connection_restapi_client_poc;
using connection_restapi_client_poc.Model;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CodeSamples
{
    public partial class ClientExamples
    {
        public static async Task ImportIOM_NOTWORKING(ConnectionApiClient conClient) 
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
    }
}
