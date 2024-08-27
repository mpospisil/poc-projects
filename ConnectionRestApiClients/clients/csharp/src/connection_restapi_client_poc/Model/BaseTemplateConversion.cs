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
    /// BaseTemplateConversion
    /// </summary>
    [DataContract(Name = "BaseTemplateConversion")]
    public partial class BaseTemplateConversion : IValidatableObject
    {
        /// <summary>
        /// Initializes a new instance of the <see cref="BaseTemplateConversion" /> class.
        /// </summary>
        /// <param name="originalValue">originalValue.</param>
        /// <param name="originalTemplateId">originalTemplateId.</param>
        /// <param name="newValue">newValue.</param>
        /// <param name="description">description.</param>
        /// <param name="newTemplateId">newTemplateId.</param>
        /// <param name="newElement">newElement.</param>
        public BaseTemplateConversion(string originalValue = default(string), string originalTemplateId = default(string), string newValue = default(string), string description = default(string), string newTemplateId = default(string), SelectedElement newElement = default(SelectedElement))
        {
            this.OriginalValue = originalValue;
            this.OriginalTemplateId = originalTemplateId;
            this.NewValue = newValue;
            this.Description = description;
            this.NewTemplateId = newTemplateId;
            this.NewElement = newElement;
        }

        /// <summary>
        /// Gets or Sets OriginalValue
        /// </summary>
        [DataMember(Name = "originalValue", EmitDefaultValue = true)]
        public string OriginalValue { get; set; }

        /// <summary>
        /// Gets or Sets OriginalTemplateId
        /// </summary>
        [DataMember(Name = "originalTemplateId", EmitDefaultValue = true)]
        public string OriginalTemplateId { get; set; }

        /// <summary>
        /// Gets or Sets NewValue
        /// </summary>
        [DataMember(Name = "newValue", EmitDefaultValue = true)]
        public string NewValue { get; set; }

        /// <summary>
        /// Gets or Sets Description
        /// </summary>
        [DataMember(Name = "description", EmitDefaultValue = true)]
        public string Description { get; set; }

        /// <summary>
        /// Gets or Sets NewTemplateId
        /// </summary>
        [DataMember(Name = "newTemplateId", EmitDefaultValue = true)]
        public string NewTemplateId { get; set; }

        /// <summary>
        /// Gets or Sets NewElement
        /// </summary>
        [DataMember(Name = "newElement", EmitDefaultValue = false)]
        public SelectedElement NewElement { get; set; }

        /// <summary>
        /// Returns the string presentation of the object
        /// </summary>
        /// <returns>String presentation of the object</returns>
        public override string ToString()
        {
            StringBuilder sb = new StringBuilder();
            sb.Append("class BaseTemplateConversion {\n");
            sb.Append("  OriginalValue: ").Append(OriginalValue).Append("\n");
            sb.Append("  OriginalTemplateId: ").Append(OriginalTemplateId).Append("\n");
            sb.Append("  NewValue: ").Append(NewValue).Append("\n");
            sb.Append("  Description: ").Append(Description).Append("\n");
            sb.Append("  NewTemplateId: ").Append(NewTemplateId).Append("\n");
            sb.Append("  NewElement: ").Append(NewElement).Append("\n");
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
