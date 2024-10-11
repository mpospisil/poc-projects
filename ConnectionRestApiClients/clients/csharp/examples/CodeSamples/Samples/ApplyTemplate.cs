﻿using IdeaStatiCa.ConnectionApi;
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
        public static async Task ApplyTemplate(ConnectionApiClient conClient)
        {
            string filePath = "inputs/corner-empty.ideaCon";
            ConProject conProject = await conClient.Project.OpenProjectFromFileAsync(filePath);

            //Get projectId Guid
            Guid projectId = conProject.ProjectId;
            var connections = await conClient.Connection.GetAllConnectionsDataAsync(projectId);
            int connectionId = connections[0].Id;

            string templateFilePath = "inputs/template-I-corner.contemp";

            //FIX Param --> Params
            ConTemplateMappingGetParam templateImport = conClient.Template.ImportTemplateFromFile(templateFilePath);

            //FIX TemplateConversions --> ConTemplateMappings??
            TemplateConversions conversionMapping = await conClient.Template.GetDefaultTemplateMappingAsync(projectId, connectionId, templateImport);

            ConTemplateApplyParam applyParam = new ConTemplateApplyParam();
            applyParam.ConnectionTemplate = templateImport.Template;

            //TO DO: We can do some custom mapping if we would like to.
            applyParam.Mapping = conversionMapping;

            var result = conClient.Template.ApplyTemplateAsync(projectId, connectionId, applyParam);

            //FIX Parameter --> Params
            ConCalculationParameter calculationParams = new ConCalculationParameter();
            calculationParams.ConnectionIds = new List<int> { connectionId };

            //Calculate the project with the applied template
            List<ConResultSummary> results = await conClient.Calculation.CalculateAsync(projectId, calculationParams);

            string exampleFolder = GetExampleFolderPathOnDesktop("ApplyTemplate");
            string fileName = "corner-template-applied.ideaCon";
            string saveFilePath = Path.Combine(exampleFolder, fileName);

            //Save the applied template
            await conClient.Project.SaveProjectAsync(projectId, saveFilePath);

            //Close the opened project.
            await conClient.Project.CloseProjectAsync(projectId.ToString());
        }
    }
}
