using IdeaStatiCa.ConnectionApi;
using IdeaStatiCa.ConnectionApi.Model;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CodeSamples
{
    public partial class ClientExamples
    {
        public static async Task GenerateReport_NOTWORKING(ConnectionApiClient conClient)
        {
            string filePath = "Inputs/HSS_norm_cond.ideaCon";
            ConProject conProject = await conClient.Project.OpenProjectFromFileAsync(filePath);

            //Get projectId Guid
            Guid projectId = conProject.ProjectId;
            var connections = await conClient.Connection.GetAllConnectionsDataAsync(projectId);
            int connectionId = connections[0].Id;

            //TO DO - FIX REPORT GENERATION
            //Generate Report
            //conclient.Report.GeneratePdfAsync()

            //Change Member Size


            //Close the opened project.
            await conClient.Project.CloseProjectAsync(projectId.ToString());
        }
    }
}
