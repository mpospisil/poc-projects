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
    /// IdeaStatiCaApiConnectionModelConLoadEffectMemberLoadIdeaStatiCaApi
    /// </summary>
    [DataContract(Name = "IdeaStatiCa_Api_Connection_Model_ConLoadEffectMemberLoad-IdeaStatiCa_Api")]
    public partial class IdeaStatiCaApiConnectionModelConLoadEffectMemberLoadIdeaStatiCaApi : IValidatableObject
    {

        /// <summary>
        /// Gets or Sets Position
        /// </summary>
        [DataMember(Name = "position", EmitDefaultValue = false)]
        public IdeaStatiCaApiConnectionModelConLoadEffectPositionEnumIdeaStatiCaApi? Position { get; set; }
        /// <summary>
        /// Initializes a new instance of the <see cref="IdeaStatiCaApiConnectionModelConLoadEffectMemberLoadIdeaStatiCaApi" /> class.
        /// </summary>
        /// <param name="memberId">memberId.</param>
        /// <param name="position">position.</param>
        /// <param name="sectionLoad">sectionLoad.</param>
        public IdeaStatiCaApiConnectionModelConLoadEffectMemberLoadIdeaStatiCaApi(int memberId = default(int), IdeaStatiCaApiConnectionModelConLoadEffectPositionEnumIdeaStatiCaApi? position = default(IdeaStatiCaApiConnectionModelConLoadEffectPositionEnumIdeaStatiCaApi?), IdeaStatiCaApiConnectionModelConLoadEffectSectionLoadIdeaStatiCaApi sectionLoad = default(IdeaStatiCaApiConnectionModelConLoadEffectSectionLoadIdeaStatiCaApi))
        {
            this.MemberId = memberId;
            this.Position = position;
            this.SectionLoad = sectionLoad;
        }

        /// <summary>
        /// Gets or Sets MemberId
        /// </summary>
        [DataMember(Name = "memberId", EmitDefaultValue = false)]
        public int MemberId { get; set; }

        /// <summary>
        /// Gets or Sets SectionLoad
        /// </summary>
        [DataMember(Name = "sectionLoad", EmitDefaultValue = false)]
        public IdeaStatiCaApiConnectionModelConLoadEffectSectionLoadIdeaStatiCaApi SectionLoad { get; set; }

        /// <summary>
        /// Returns the string presentation of the object
        /// </summary>
        /// <returns>String presentation of the object</returns>
        public override string ToString()
        {
            StringBuilder sb = new StringBuilder();
            sb.Append("class IdeaStatiCaApiConnectionModelConLoadEffectMemberLoadIdeaStatiCaApi {\n");
            sb.Append("  MemberId: ").Append(MemberId).Append("\n");
            sb.Append("  Position: ").Append(Position).Append("\n");
            sb.Append("  SectionLoad: ").Append(SectionLoad).Append("\n");
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
