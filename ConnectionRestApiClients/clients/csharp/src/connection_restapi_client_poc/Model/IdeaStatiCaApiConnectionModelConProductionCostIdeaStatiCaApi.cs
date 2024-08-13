/*
 * Connection Rest API 1.0
 *
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 1.0
 * Generated by: https://github.com/openapitools/openapi-generator.git
 */


using System;
using System.Collections;
using System.Collections.Generic;
using System.Collections.ObjectModel;
using System.Linq;
using System.IO;
using System.Runtime.Serialization;
using System.Text;
using System.Text.RegularExpressions;
using Newtonsoft.Json;
using Newtonsoft.Json.Converters;
using Newtonsoft.Json.Linq;
using System.ComponentModel.DataAnnotations;
using OpenAPIDateConverter = connection_restapi_client_poc.Client.OpenAPIDateConverter;

namespace connection_restapi_client_poc.Model
{
    /// <summary>
    /// IdeaStatiCaApiConnectionModelConProductionCostIdeaStatiCaApi
    /// </summary>
    [DataContract(Name = "IdeaStatiCa_Api_Connection_Model_ConProductionCost-IdeaStatiCa_Api")]
    public partial class IdeaStatiCaApiConnectionModelConProductionCostIdeaStatiCaApi : IValidatableObject
    {
        /// <summary>
        /// Initializes a new instance of the <see cref="IdeaStatiCaApiConnectionModelConProductionCostIdeaStatiCaApi" /> class.
        /// </summary>
        /// <param name="totalEstimatedCost">totalEstimatedCost.</param>
        public IdeaStatiCaApiConnectionModelConProductionCostIdeaStatiCaApi(double totalEstimatedCost = default(double))
        {
            this.TotalEstimatedCost = totalEstimatedCost;
        }

        /// <summary>
        /// Gets or Sets TotalEstimatedCost
        /// </summary>
        [DataMember(Name = "totalEstimatedCost", EmitDefaultValue = false)]
        public double TotalEstimatedCost { get; set; }

        /// <summary>
        /// Returns the string presentation of the object
        /// </summary>
        /// <returns>String presentation of the object</returns>
        public override string ToString()
        {
            StringBuilder sb = new StringBuilder();
            sb.Append("class IdeaStatiCaApiConnectionModelConProductionCostIdeaStatiCaApi {\n");
            sb.Append("  TotalEstimatedCost: ").Append(TotalEstimatedCost).Append("\n");
            sb.Append("}\n");
            return sb.ToString();
        }

        /// <summary>
        /// Returns the JSON string presentation of the object
        /// </summary>
        /// <returns>JSON string presentation of the object</returns>
        public virtual string ToJson()
        {
            return Newtonsoft.Json.JsonConvert.SerializeObject(this, Newtonsoft.Json.Formatting.Indented);
        }

        /// <summary>
        /// To validate all properties of the instance
        /// </summary>
        /// <param name="validationContext">Validation context</param>
        /// <returns>Validation Result</returns>
        IEnumerable<ValidationResult> IValidatableObject.Validate(ValidationContext validationContext)
        {
            yield break;
        }
    }

}
