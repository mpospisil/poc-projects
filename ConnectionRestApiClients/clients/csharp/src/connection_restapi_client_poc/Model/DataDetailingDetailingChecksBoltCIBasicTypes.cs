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
    /// DataDetailingDetailingChecksBoltCIBasicTypes
    /// </summary>
    [DataContract(Name = "Data_Detailing_DetailingChecksBolt-CI_BasicTypes")]
    public partial class DataDetailingDetailingChecksBoltCIBasicTypes : IValidatableObject
    {
        /// <summary>
        /// Initializes a new instance of the <see cref="DataDetailingDetailingChecksBoltCIBasicTypes" /> class.
        /// </summary>
        /// <param name="isAnchor">isAnchor.</param>
        /// <param name="connectorID">connectorID.</param>
        /// <param name="results">results.</param>
        public DataDetailingDetailingChecksBoltCIBasicTypes(bool isAnchor = default(bool), int connectorID = default(int), List<DataDetailingIDetailingCheckCIBasicTypes> results = default(List<DataDetailingIDetailingCheckCIBasicTypes>))
        {
            this.IsAnchor = isAnchor;
            this.ConnectorID = connectorID;
            this.Results = results;
        }

        /// <summary>
        /// Gets or Sets IsAnchor
        /// </summary>
        [DataMember(Name = "isAnchor", EmitDefaultValue = true)]
        public bool IsAnchor { get; set; }

        /// <summary>
        /// Gets or Sets ConnectorID
        /// </summary>
        [DataMember(Name = "connectorID", EmitDefaultValue = false)]
        public int ConnectorID { get; set; }

        /// <summary>
        /// Gets or Sets Results
        /// </summary>
        [DataMember(Name = "results", EmitDefaultValue = true)]
        public List<DataDetailingIDetailingCheckCIBasicTypes> Results { get; set; }

        /// <summary>
        /// Returns the string presentation of the object
        /// </summary>
        /// <returns>String presentation of the object</returns>
        public override string ToString()
        {
            StringBuilder sb = new StringBuilder();
            sb.Append("class DataDetailingDetailingChecksBoltCIBasicTypes {\n");
            sb.Append("  IsAnchor: ").Append(IsAnchor).Append("\n");
            sb.Append("  ConnectorID: ").Append(ConnectorID).Append("\n");
            sb.Append("  Results: ").Append(Results).Append("\n");
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
