﻿using IdeaRS.OpenModel;
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
        public static async Task ImportIOM_Multiple(ConnectionApiClient conClient) 
        {
            string filePath = "Inputs/multiple_connections.xml";
            
            //Read IOM to see which connections are in the file.
            IdeaRS.OpenModel.OpenModelContainer openModel = Tools.OpenModelContainerFromFile(filePath);
            List<int> avaliableConPoints = openModel.OpenModel.ConnectionPoint.Select(x => x.Id).ToList();  

            Console.WriteLine("Points avaliable for import: " + String.Join(",", avaliableConPoints));
            Console.WriteLine("Provide list of points to import seperated by comma. (eg 1, 3, 4)");

            List<int> connectionsToCreate = new List<int>();

            while (connectionsToCreate.Count < 1)
            {
                string input = Console.ReadLine();

                if (input != null)
                {
                    foreach (var item in input.Split(','))
                    {
                        item.Trim();
                        if (int.TryParse(item, out int conItem))
                            connectionsToCreate.Add(conItem);
                    }
                    if (connectionsToCreate.Count > 0)
                        break;
                }
                Console.WriteLine("Connections not input correctly, please provide atleast one connection");
            }

            ConProject conProject = await conClient.Project.CreateProjectFromIomFileAsync(filePath, connectionsToCreate);

            //Get projectId Guid
            Guid projectId = conProject.ProjectId;

            string saveFilePath = "connection-file-from-IOM-multiple.ideaCon";

            await conClient.Project.SaveProjectAsync(projectId, saveFilePath);
        }
    }
}
