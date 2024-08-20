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
    /// IdeaStatiCaApiConnectionModelConLoadEffectSectionLoadIdeaStatiCaApi
    /// </summary>
    [DataContract(Name = "IdeaStatiCa_Api_Connection_Model_ConLoadEffectSectionLoad-IdeaStatiCa_Api")]
    public partial class IdeaStatiCaApiConnectionModelConLoadEffectSectionLoadIdeaStatiCaApi : IValidatableObject
    {
        /// <summary>
        /// Initializes a new instance of the <see cref="IdeaStatiCaApiConnectionModelConLoadEffectSectionLoadIdeaStatiCaApi" /> class.
        /// </summary>
        /// <param name="n">n.</param>
        /// <param name="vy">vy.</param>
        /// <param name="vz">vz.</param>
        /// <param name="mx">mx.</param>
        /// <param name="my">my.</param>
        /// <param name="mz">mz.</param>
        public IdeaStatiCaApiConnectionModelConLoadEffectSectionLoadIdeaStatiCaApi(double n = default(double), double vy = default(double), double vz = default(double), double mx = default(double), double my = default(double), double mz = default(double))
        {
            this.N = n;
            this.Vy = vy;
            this.Vz = vz;
            this.Mx = mx;
            this.My = my;
            this.Mz = mz;
        }

        /// <summary>
        /// Gets or Sets N
        /// </summary>
        [DataMember(Name = "n", EmitDefaultValue = false)]
        public double N { get; set; }

        /// <summary>
        /// Gets or Sets Vy
        /// </summary>
        [DataMember(Name = "vy", EmitDefaultValue = false)]
        public double Vy { get; set; }

        /// <summary>
        /// Gets or Sets Vz
        /// </summary>
        [DataMember(Name = "vz", EmitDefaultValue = false)]
        public double Vz { get; set; }

        /// <summary>
        /// Gets or Sets Mx
        /// </summary>
        [DataMember(Name = "mx", EmitDefaultValue = false)]
        public double Mx { get; set; }

        /// <summary>
        /// Gets or Sets My
        /// </summary>
        [DataMember(Name = "my", EmitDefaultValue = false)]
        public double My { get; set; }

        /// <summary>
        /// Gets or Sets Mz
        /// </summary>
        [DataMember(Name = "mz", EmitDefaultValue = false)]
        public double Mz { get; set; }

        /// <summary>
        /// Returns the string presentation of the object
        /// </summary>
        /// <returns>String presentation of the object</returns>
        public override string ToString()
        {
            StringBuilder sb = new StringBuilder();
            sb.Append("class IdeaStatiCaApiConnectionModelConLoadEffectSectionLoadIdeaStatiCaApi {\n");
            sb.Append("  N: ").Append(N).Append("\n");
            sb.Append("  Vy: ").Append(Vy).Append("\n");
            sb.Append("  Vz: ").Append(Vz).Append("\n");
            sb.Append("  Mx: ").Append(Mx).Append("\n");
            sb.Append("  My: ").Append(My).Append("\n");
            sb.Append("  Mz: ").Append(Mz).Append("\n");
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