using connection_restapi_client_poc.Model;
using connection_restapi_client_poc;

namespace UpdateLoadEffect
{
    internal class Program
    {
        static async Task Main(string[] args)
        {
            ConnectionApiClientFactory clientFactory = new ConnectionApiClientFactory("http://localhost:5000");
            ConnectionApiClient conclient = (ConnectionApiClient)await clientFactory.CreateConnectionApiClient();

            try
            {
                string filePath = "inputs/simple knee connection.ideaCon";
                ConProject conProject = await conclient.Project.OpenProjectFromFileAsync(filePath);

                //Get projectId Guid
                Guid projectId = conProject.ProjectId;
                var connections = await conclient.Connection.GetAllConnectionsDataAsync(projectId);
                int connectionId = connections[0].Id;

                ConLoadSettings loadSettings = await conclient.LoadEffect.GetLoadSettingsAsync(projectId, connectionId);

                Console.WriteLine(loadSettings.ToString());

                //Get Load Effects
                List<ConLoadEffect> loadEffects = await conclient.LoadEffect.GetLoadEffectsAsync(projectId, connectionId);

                double effectMultiplier = 1.25;
                
                ConLoadEffect loadEffectBasis = null;

                for (int i = 0; i < loadEffects.Count; i++)
                {
                    if (i == 0)
                    {
                        loadEffectBasis = loadEffects[i];
                        continue;
                    }

                    ConLoadEffect loadEffect = loadEffects[i];
                    //FIX: LoadEffect provides all the member loadings - even if LoadsInEquilibrium is set to False. Is this correct??

                    for (int j = 0; j < loadEffect.MemberLoadings.Count; j++) 
                    {
                        ConLoadEffectMemberLoad loading = loadEffect.MemberLoadings[j];
                        ConLoadEffectMemberLoad loadingBasis = loadEffectBasis.MemberLoadings[j];

                        loading.SectionLoad.N = loadingBasis.SectionLoad.N * effectMultiplier;
                        loading.SectionLoad.Vy = loadingBasis.SectionLoad.Vy * effectMultiplier;
                        loading.SectionLoad.Vz = loadingBasis.SectionLoad.Vz * effectMultiplier; 
                        loading.SectionLoad.Mz = loadingBasis.SectionLoad.Mz * effectMultiplier;
                        loading.SectionLoad.My = loadingBasis.SectionLoad.My * effectMultiplier;
                        loading.SectionLoad.Mx = loadingBasis.SectionLoad.Mx * effectMultiplier;
                    }

                     await conclient.LoadEffect.UpdateLoadEffectAsync(projectId, connectionId, loadEffect.Id, loadEffect);

                    //Increase each increment by 25% of the original value.
                    effectMultiplier += 0.25;
                }

                //Save updated file.
                string saveFilePath = "updated-load-effects.ideaCon";

                await conclient.Project.SaveProjectAsync(projectId, saveFilePath);

                Console.WriteLine("File saved to: " + saveFilePath);

            }
            catch (Exception ex)
            {
                Console.WriteLine(ex.ToString());
            }
        }
    }
}