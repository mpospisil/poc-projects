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
    /// Defines haunches (variyng cross-sections) along the member.    One IdeaRS.OpenModel.Model.Taper may be assigned to multiple &lt;see cref&#x3D;\&quot;T:IdeaRS.OpenModel.Model.Member1D\&quot;&gt;Members&lt;/see&gt;.  Sections of the member not covered by a span will use the member&#39;s cross-section.
    /// </summary>
    [DataContract(Name = "Model_Taper-IdeaRS_OpenModel")]
    public partial class ModelTaperIdeaRSOpenModel : IValidatableObject
    {
        /// <summary>
        /// Initializes a new instance of the <see cref="ModelTaperIdeaRSOpenModel" /> class.
        /// </summary>
        /// <param name="id">Element Id.</param>
        public ModelTaperIdeaRSOpenModel(int id = default(int))
        {
            this.Id = id;
        }

        /// <summary>
        /// Element Id
        /// </summary>
        /// <value>Element Id</value>
        [DataMember(Name = "id", EmitDefaultValue = false)]
        public int Id { get; set; }

        /// <summary>
        /// Returns the string presentation of the object
        /// </summary>
        /// <returns>String presentation of the object</returns>
        public override string ToString()
        {
            StringBuilder sb = new StringBuilder();
            sb.Append("class ModelTaperIdeaRSOpenModel {\n");
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
