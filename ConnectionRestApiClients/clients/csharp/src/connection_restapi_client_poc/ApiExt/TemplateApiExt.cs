using connection_restapi_client_poc.Model;
using System;
using System.IO;
using System.Text;
using System.Threading.Tasks;

namespace connection_restapi_client_poc.Api
{
    public interface ITemplateApiAsyncExt : ITemplateApiAsync
    {
        ConTemplateMappingGetParam ImportTemplateFromFile(string fileName);
    }

    public class TemplateApiExt : TemplateApi, ITemplateApiAsyncExt
    {
        public TemplateApiExt(connection_restapi_client_poc.Client.ISynchronousClient client, connection_restapi_client_poc.Client.IAsynchronousClient asyncClient, connection_restapi_client_poc.Client.IReadableConfiguration configuration) : base(client, asyncClient, configuration)
        {
        }

        public ConTemplateMappingGetParam ImportTemplateFromFile(string filePath)
        {
            ConTemplateMappingGetParam templateParams = new ConTemplateMappingGetParam();

            try
            {
                if (!File.Exists(filePath))
                    throw new FileNotFoundException($"The file '{filePath}' was not found.");

                // Read the file content with UTF-16 (Unicode) encoding
                templateParams.Template = File.ReadAllText(filePath, Encoding.Unicode);

                Console.WriteLine("File read successfully.");

            }
            catch (Exception ex)
            {
                Console.WriteLine($"Error: {ex.Message}");
            }

            return templateParams;
        }
    }
}
