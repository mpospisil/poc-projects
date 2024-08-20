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
    /// Represents a region in two-dimensional space included outline (border) and openings.
    /// </summary>
    [DataContract(Name = "Geometry2D_Region2D-IdeaRS_OpenModel")]
    public partial class Geometry2DRegion2DIdeaRSOpenModel : IValidatableObject
    {
        /// <summary>
        /// Initializes a new instance of the <see cref="Geometry2DRegion2DIdeaRSOpenModel" /> class.
        /// </summary>
        /// <param name="outline">outline.</param>
        /// <param name="openings">Gets or sets the list of openings in the Region2D..</param>
        public Geometry2DRegion2DIdeaRSOpenModel(Geometry2DPolyLine2DIdeaRSOpenModel outline = default(Geometry2DPolyLine2DIdeaRSOpenModel), List<Geometry2DPolyLine2DIdeaRSOpenModel> openings = default(List<Geometry2DPolyLine2DIdeaRSOpenModel>))
        {
            this.Outline = outline;
            this.Openings = openings;
        }

        /// <summary>
        /// Gets or Sets Outline
        /// </summary>
        [DataMember(Name = "outline", EmitDefaultValue = false)]
        public Geometry2DPolyLine2DIdeaRSOpenModel Outline { get; set; }

        /// <summary>
        /// Gets or sets the list of openings in the Region2D.
        /// </summary>
        /// <value>Gets or sets the list of openings in the Region2D.</value>
        [DataMember(Name = "openings", EmitDefaultValue = true)]
        public List<Geometry2DPolyLine2DIdeaRSOpenModel> Openings { get; set; }

        /// <summary>
        /// Returns the string presentation of the object
        /// </summary>
        /// <returns>String presentation of the object</returns>
        public override string ToString()
        {
            StringBuilder sb = new StringBuilder();
            sb.Append("class Geometry2DRegion2DIdeaRSOpenModel {\n");
            sb.Append("  Outline: ").Append(Outline).Append("\n");
            sb.Append("  Openings: ").Append(Openings).Append("\n");
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