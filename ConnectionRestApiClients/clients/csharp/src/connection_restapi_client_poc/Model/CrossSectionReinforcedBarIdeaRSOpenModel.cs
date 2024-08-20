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
    /// CrossSectionReinforcedBarIdeaRSOpenModel
    /// </summary>
    [DataContract(Name = "CrossSection_ReinforcedBar-IdeaRS_OpenModel")]
    public partial class CrossSectionReinforcedBarIdeaRSOpenModel : IValidatableObject
    {
        /// <summary>
        /// Initializes a new instance of the <see cref="CrossSectionReinforcedBarIdeaRSOpenModel" /> class.
        /// </summary>
        /// <param name="point">point.</param>
        /// <param name="diameter">diameter.</param>
        /// <param name="material">material.</param>
        public CrossSectionReinforcedBarIdeaRSOpenModel(Geometry2DPoint2DIdeaRSOpenModel point = default(Geometry2DPoint2DIdeaRSOpenModel), double diameter = default(double), ReferenceElementIdeaRSOpenModel material = default(ReferenceElementIdeaRSOpenModel))
        {
            this.Point = point;
            this.Diameter = diameter;
            this.Material = material;
        }

        /// <summary>
        /// Gets or Sets Point
        /// </summary>
        [DataMember(Name = "point", EmitDefaultValue = false)]
        public Geometry2DPoint2DIdeaRSOpenModel Point { get; set; }

        /// <summary>
        /// Gets or Sets Diameter
        /// </summary>
        [DataMember(Name = "diameter", EmitDefaultValue = false)]
        public double Diameter { get; set; }

        /// <summary>
        /// Gets or Sets Material
        /// </summary>
        [DataMember(Name = "material", EmitDefaultValue = false)]
        public ReferenceElementIdeaRSOpenModel Material { get; set; }

        /// <summary>
        /// Returns the string presentation of the object
        /// </summary>
        /// <returns>String presentation of the object</returns>
        public override string ToString()
        {
            StringBuilder sb = new StringBuilder();
            sb.Append("class CrossSectionReinforcedBarIdeaRSOpenModel {\n");
            sb.Append("  Point: ").Append(Point).Append("\n");
            sb.Append("  Diameter: ").Append(Diameter).Append("\n");
            sb.Append("  Material: ").Append(Material).Append("\n");
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
