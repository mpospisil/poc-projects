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
    /// Check value for Plate
    /// </summary>
    [DataContract(Name = "Connection_CheckResPlate-IdeaRS_OpenModel")]
    public partial class ConnectionCheckResPlateIdeaRSOpenModel : IValidatableObject
    {
        /// <summary>
        /// Initializes a new instance of the <see cref="ConnectionCheckResPlateIdeaRSOpenModel" /> class.
        /// </summary>
        /// <param name="name">Name of Plate.</param>
        /// <param name="checkStatus">Status of the Check.</param>
        /// <param name="loadCaseId">Id of Load Case.</param>
        /// <param name="maxStrain">Max Strain.</param>
        /// <param name="maxStress">Max Stress.</param>
        /// <param name="items">In case of presentation of groups plates (uncoiled beams).</param>
        public ConnectionCheckResPlateIdeaRSOpenModel(string name = default(string), bool checkStatus = default(bool), int loadCaseId = default(int), double maxStrain = default(double), double maxStress = default(double), List<int> items = default(List<int>))
        {
            this.Name = name;
            this.CheckStatus = checkStatus;
            this.LoadCaseId = loadCaseId;
            this.MaxStrain = maxStrain;
            this.MaxStress = maxStress;
            this.Items = items;
        }

        /// <summary>
        /// Name of Plate
        /// </summary>
        /// <value>Name of Plate</value>
        [DataMember(Name = "name", EmitDefaultValue = true)]
        public string Name { get; set; }

        /// <summary>
        /// Status of the Check
        /// </summary>
        /// <value>Status of the Check</value>
        [DataMember(Name = "checkStatus", EmitDefaultValue = true)]
        public bool CheckStatus { get; set; }

        /// <summary>
        /// Id of Load Case
        /// </summary>
        /// <value>Id of Load Case</value>
        [DataMember(Name = "loadCaseId", EmitDefaultValue = false)]
        public int LoadCaseId { get; set; }

        /// <summary>
        /// Max Strain
        /// </summary>
        /// <value>Max Strain</value>
        [DataMember(Name = "maxStrain", EmitDefaultValue = false)]
        public double MaxStrain { get; set; }

        /// <summary>
        /// Max Stress
        /// </summary>
        /// <value>Max Stress</value>
        [DataMember(Name = "maxStress", EmitDefaultValue = false)]
        public double MaxStress { get; set; }

        /// <summary>
        /// In case of presentation of groups plates (uncoiled beams)
        /// </summary>
        /// <value>In case of presentation of groups plates (uncoiled beams)</value>
        [DataMember(Name = "items", EmitDefaultValue = true)]
        public List<int> Items { get; set; }

        /// <summary>
        /// Returns the string presentation of the object
        /// </summary>
        /// <returns>String presentation of the object</returns>
        public override string ToString()
        {
            StringBuilder sb = new StringBuilder();
            sb.Append("class ConnectionCheckResPlateIdeaRSOpenModel {\n");
            sb.Append("  Name: ").Append(Name).Append("\n");
            sb.Append("  CheckStatus: ").Append(CheckStatus).Append("\n");
            sb.Append("  LoadCaseId: ").Append(LoadCaseId).Append("\n");
            sb.Append("  MaxStrain: ").Append(MaxStrain).Append("\n");
            sb.Append("  MaxStress: ").Append(MaxStress).Append("\n");
            sb.Append("  Items: ").Append(Items).Append("\n");
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