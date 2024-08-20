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
    /// Provides data of the folded plate
    /// </summary>
    [DataContract(Name = "Connection_FoldedPlateData-IdeaRS_OpenModel")]
    public partial class ConnectionFoldedPlateDataIdeaRSOpenModel : IValidatableObject
    {
        /// <summary>
        /// Initializes a new instance of the <see cref="ConnectionFoldedPlateDataIdeaRSOpenModel" /> class.
        /// </summary>
        /// <param name="plates">List of plates belong to folded plate.</param>
        /// <param name="bends">List of bends connected plates of foldedplate.</param>
        public ConnectionFoldedPlateDataIdeaRSOpenModel(List<ConnectionPlateDataIdeaRSOpenModel> plates = default(List<ConnectionPlateDataIdeaRSOpenModel>), List<ConnectionBendDataIdeaRSOpenModel> bends = default(List<ConnectionBendDataIdeaRSOpenModel>))
        {
            this.Plates = plates;
            this.Bends = bends;
        }

        /// <summary>
        /// List of plates belong to folded plate
        /// </summary>
        /// <value>List of plates belong to folded plate</value>
        [DataMember(Name = "plates", EmitDefaultValue = true)]
        public List<ConnectionPlateDataIdeaRSOpenModel> Plates { get; set; }

        /// <summary>
        /// List of bends connected plates of foldedplate
        /// </summary>
        /// <value>List of bends connected plates of foldedplate</value>
        [DataMember(Name = "bends", EmitDefaultValue = true)]
        public List<ConnectionBendDataIdeaRSOpenModel> Bends { get; set; }

        /// <summary>
        /// Returns the string presentation of the object
        /// </summary>
        /// <returns>String presentation of the object</returns>
        public override string ToString()
        {
            StringBuilder sb = new StringBuilder();
            sb.Append("class ConnectionFoldedPlateDataIdeaRSOpenModel {\n");
            sb.Append("  Plates: ").Append(Plates).Append("\n");
            sb.Append("  Bends: ").Append(Bends).Append("\n");
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