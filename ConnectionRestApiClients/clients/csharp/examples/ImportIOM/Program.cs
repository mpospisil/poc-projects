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
                string filePath = "inputs/mulitple_connections.xml";
                
                ConProject conProject = await conclient.Project.ImportIOMAsync(OpenProjectFromFileAsync(filePath);

                //Get projectId Guid
                Guid projectId = conProject.ProjectId;
                var connections = await conclient.Connection.GetAllConnectionsDataAsync(projectId);
                int connectionId = connections[0].Id;

                string templateFilePath = "inputs/mulitple_connections.xml";

                //FIX Param --> Params
                ConTemplateMappingGetParam templateImport = conclient.Template.ImportTemplateFromFile(templateFilePath);

                //FIX TemplateConversions --> ConTemplateMappings??
                TemplateConversions conversionMapping = await conclient.Template.GetDefaultTemplateMappingAsync(projectId, connectionId, templateImport);

                ConTemplateApplyParam applyParam = new ConTemplateApplyParam();
                applyParam.ConnectionTemplate = templateImport.Template;

                //TO DO: We can do some custom mapping if we would like to.
                applyParam.Mapping = conversionMapping;

                var result = conclient.Template.ApplyTemplateAsync(projectId, connectionId, applyParam);

                //FIX Parameter --> Params
                ConCalculationParameter calculationParams = new ConCalculationParameter();
                calculationParams.ConnectionIds = new List<int> { connectionId };

                List<ConResultSummary> results = await conclient.Calculation.CalculateAsync(projectId, calculationParams);

                string saveFilePath = "corner-template-applied.ideaCon";

                await conclient.Project.SaveProjectAsync(projectId, saveFilePath);

            }
            catch (Exception ex)
            {
            }
        }
    }
}