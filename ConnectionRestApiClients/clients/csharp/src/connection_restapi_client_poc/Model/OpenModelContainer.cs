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
    /// OpenModelContainer is used to keep structural data and results of a finite element analysis in one place.  The main reason is easier moving (passing) pass the instance of OpenModel and corresponding instace of OpenModelResults.
    /// </summary>
    [DataContract(Name = "OpenModelContainer")]
    public partial class OpenModelContainer : IValidatableObject
    {
        /// <summary>
        /// Initializes a new instance of the <see cref="OpenModelContainer" /> class.
        /// </summary>
        /// <param name="openModel">openModel.</param>
        /// <param name="openModelResult">openModelResult.</param>
        public OpenModelContainer(OpenModel openModel = default(OpenModel), OpenModelResult openModelResult = default(OpenModelResult))
        {
            this.OpenModel = openModel;
            this.OpenModelResult = openModelResult;
        }

        /// <summary>
        /// Gets or Sets OpenModel
        /// </summary>
        [DataMember(Name = "openModel", EmitDefaultValue = false)]
        public OpenModel OpenModel { get; set; }

        /// <summary>
        /// Gets or Sets OpenModelResult
        /// </summary>
        [DataMember(Name = "openModelResult", EmitDefaultValue = false)]
        public OpenModelResult OpenModelResult { get; set; }

        /// <summary>
        /// Returns the string presentation of the object
        /// </summary>
        /// <returns>String presentation of the object</returns>
        public override string ToString()
        {
            StringBuilder sb = new StringBuilder();
            sb.Append("class OpenModelContainer {\n");
            sb.Append("  OpenModel: ").Append(OpenModel).Append("\n");
            sb.Append("  OpenModelResult: ").Append(OpenModelResult).Append("\n");
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
