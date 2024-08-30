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
    /// DrawData
    /// </summary>
    [DataContract(Name = "DrawData")]
    public partial class DrawData : IValidatableObject
    {
        /// <summary>
        /// Initializes a new instance of the <see cref="DrawData" /> class.
        /// </summary>
        /// <param name="groups">groups.</param>
        /// <param name="vertices">vertices.</param>
        /// <param name="normals">normals.</param>
        public DrawData(List<IGroup> groups = default(List<IGroup>), List<double> vertices = default(List<double>), List<double> normals = default(List<double>))
        {
            this.Groups = groups;
            this.Vertices = vertices;
            this.Normals = normals;
        }

        /// <summary>
        /// Gets or Sets Groups
        /// </summary>
        [DataMember(Name = "groups", EmitDefaultValue = true)]
        public List<IGroup> Groups { get; set; }

        /// <summary>
        /// Gets or Sets Vertices
        /// </summary>
        [DataMember(Name = "vertices", EmitDefaultValue = true)]
        public List<double> Vertices { get; set; }

        /// <summary>
        /// Gets or Sets Normals
        /// </summary>
        [DataMember(Name = "normals", EmitDefaultValue = true)]
        public List<double> Normals { get; set; }

        /// <summary>
        /// Returns the string presentation of the object
        /// </summary>
        /// <returns>String presentation of the object</returns>
        public override string ToString()
        {
            StringBuilder sb = new StringBuilder();
            sb.Append("class DrawData {\n");
            sb.Append("  Groups: ").Append(Groups).Append("\n");
            sb.Append("  Vertices: ").Append(Vertices).Append("\n");
            sb.Append("  Normals: ").Append(Normals).Append("\n");
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
