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
using OpenAPIDateConverter = IdeaStatiCa.ConnectionApi.Client.OpenAPIDateConverter;

namespace IdeaStatiCa.ConnectionApi.Model
{
    /// <summary>
    /// Loading identification
    /// </summary>
    [DataContract(Name = "Loading")]
    public partial class Loading : IValidatableObject
    {

        /// <summary>
        /// Gets or Sets LoadingType
        /// </summary>
        [DataMember(Name = "loadingType", EmitDefaultValue = false)]
        public LoadingType? LoadingType { get; set; }
        /// <summary>
        /// Initializes a new instance of the <see cref="Loading" /> class.
        /// </summary>
        /// <param name="loadingType">loadingType.</param>
        /// <param name="id">Id of loading.</param>
        public Loading(LoadingType? loadingType = default(LoadingType?), int id = default(int))
        {
            this.LoadingType = loadingType;
            this.Id = id;
        }

        /// <summary>
        /// Id of loading
        /// </summary>
        /// <value>Id of loading</value>
        [DataMember(Name = "id", EmitDefaultValue = false)]
        public int Id { get; set; }

        /// <summary>
        /// Returns the string presentation of the object
        /// </summary>
        /// <returns>String presentation of the object</returns>
        public override string ToString()
        {
            StringBuilder sb = new StringBuilder();
            sb.Append("class Loading {\n");
            sb.Append("  LoadingType: ").Append(LoadingType).Append("\n");
            sb.Append("  Id: ").Append(Id).Append("\n");
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
