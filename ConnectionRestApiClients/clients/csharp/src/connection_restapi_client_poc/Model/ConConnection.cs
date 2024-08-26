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
    /// ConConnection
    /// </summary>
    [DataContract(Name = "ConConnection")]
    public partial class ConConnection : IValidatableObject
    {

        /// <summary>
        /// Gets or Sets AnalysisType
        /// </summary>
        [DataMember(Name = "analysisType", EmitDefaultValue = false)]
        public ConAnalysisTypeEnum? AnalysisType { get; set; }
        /// <summary>
        /// Initializes a new instance of the <see cref="ConConnection" /> class.
        /// </summary>
        /// <param name="id">id.</param>
        /// <param name="identifier">identifier.</param>
        /// <param name="name">name.</param>
        /// <param name="description">description.</param>
        /// <param name="analysisType">analysisType.</param>
        /// <param name="loadOptions">loadOptions.</param>
        /// <param name="bearingMemberId">bearingMemberId.</param>
        public ConConnection(int id = default(int), string identifier = default(string), string name = default(string), string description = default(string), ConAnalysisTypeEnum? analysisType = default(ConAnalysisTypeEnum?), ConLoadingOptions loadOptions = default(ConLoadingOptions), int bearingMemberId = default(int))
        {
            this.Id = id;
            this.Identifier = identifier;
            this.Name = name;
            this.Description = description;
            this.AnalysisType = analysisType;
            this.LoadOptions = loadOptions;
            this.BearingMemberId = bearingMemberId;
        }

        /// <summary>
        /// Gets or Sets Id
        /// </summary>
        [DataMember(Name = "id", EmitDefaultValue = false)]
        public int Id { get; set; }

        /// <summary>
        /// Gets or Sets Identifier
        /// </summary>
        [DataMember(Name = "identifier", EmitDefaultValue = true)]
        public string Identifier { get; set; }

        /// <summary>
        /// Gets or Sets Name
        /// </summary>
        [DataMember(Name = "name", EmitDefaultValue = true)]
        public string Name { get; set; }

        /// <summary>
        /// Gets or Sets Description
        /// </summary>
        [DataMember(Name = "description", EmitDefaultValue = true)]
        public string Description { get; set; }

        /// <summary>
        /// Gets or Sets LoadOptions
        /// </summary>
        [DataMember(Name = "loadOptions", EmitDefaultValue = false)]
        public ConLoadingOptions LoadOptions { get; set; }

        /// <summary>
        /// Gets or Sets BearingMemberId
        /// </summary>
        [DataMember(Name = "bearingMemberId", EmitDefaultValue = false)]
        public int BearingMemberId { get; set; }

        /// <summary>
        /// Gets or Sets IsCalculated
        /// </summary>
        [DataMember(Name = "isCalculated", EmitDefaultValue = true)]
        public bool IsCalculated { get; private set; }

        /// <summary>
        /// Returns false as IsCalculated should not be serialized given that it's read-only.
        /// </summary>
        /// <returns>false (boolean)</returns>
        public bool ShouldSerializeIsCalculated()
        {
            return false;
        }
        /// <summary>
        /// Returns the string presentation of the object
        /// </summary>
        /// <returns>String presentation of the object</returns>
        public override string ToString()
        {
            StringBuilder sb = new StringBuilder();
            sb.Append("class ConConnection {\n");
            sb.Append("  Id: ").Append(Id).Append("\n");
            sb.Append("  Identifier: ").Append(Identifier).Append("\n");
            sb.Append("  Name: ").Append(Name).Append("\n");
            sb.Append("  Description: ").Append(Description).Append("\n");
            sb.Append("  AnalysisType: ").Append(AnalysisType).Append("\n");
            sb.Append("  LoadOptions: ").Append(LoadOptions).Append("\n");
            sb.Append("  BearingMemberId: ").Append(BearingMemberId).Append("\n");
            sb.Append("  IsCalculated: ").Append(IsCalculated).Append("\n");
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