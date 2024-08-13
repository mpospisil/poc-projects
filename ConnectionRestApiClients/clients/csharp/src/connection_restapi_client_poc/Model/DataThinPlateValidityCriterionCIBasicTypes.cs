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
    /// DataThinPlateValidityCriterionCIBasicTypes
    /// </summary>
    [DataContract(Name = "Data_ThinPlateValidityCriterion-CI_BasicTypes")]
    public partial class DataThinPlateValidityCriterionCIBasicTypes : IValidatableObject
    {
        /// <summary>
        /// Initializes a new instance of the <see cref="DataThinPlateValidityCriterionCIBasicTypes" /> class.
        /// </summary>
        /// <param name="valueName">valueName.</param>
        /// <param name="value">value.</param>
        /// <param name="limit">limit.</param>
        public DataThinPlateValidityCriterionCIBasicTypes(string valueName = default(string), double value = default(double), double limit = default(double))
        {
            this.ValueName = valueName;
            this.Value = value;
            this.Limit = limit;
        }

        /// <summary>
        /// Gets or Sets ValueName
        /// </summary>
        [DataMember(Name = "valueName", EmitDefaultValue = true)]
        public string ValueName { get; set; }

        /// <summary>
        /// Gets or Sets Value
        /// </summary>
        [DataMember(Name = "value", EmitDefaultValue = false)]
        public double Value { get; set; }

        /// <summary>
        /// Gets or Sets Limit
        /// </summary>
        [DataMember(Name = "limit", EmitDefaultValue = false)]
        public double Limit { get; set; }

        /// <summary>
        /// Returns the string presentation of the object
        /// </summary>
        /// <returns>String presentation of the object</returns>
        public override string ToString()
        {
            StringBuilder sb = new StringBuilder();
            sb.Append("class DataThinPlateValidityCriterionCIBasicTypes {\n");
            sb.Append("  ValueName: ").Append(ValueName).Append("\n");
            sb.Append("  Value: ").Append(Value).Append("\n");
            sb.Append("  Limit: ").Append(Limit).Append("\n");
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
