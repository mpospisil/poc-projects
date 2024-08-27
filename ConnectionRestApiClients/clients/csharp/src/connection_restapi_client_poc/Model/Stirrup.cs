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
    /// Stirrup
    /// </summary>
    [DataContract(Name = "Stirrup")]
    public partial class Stirrup : IValidatableObject
    {
        /// <summary>
        /// Initializes a new instance of the <see cref="Stirrup" /> class.
        /// </summary>
        /// <param name="geometry">geometry.</param>
        /// <param name="diameter">Diameter.</param>
        /// <param name="material">material.</param>
        /// <param name="anchorageLenght">Anchorage Lenght.</param>
        /// <param name="diameterOfMandrel">Radius of stirrup mandrel - refering to stirrup axis.</param>
        /// <param name="isClosed">Open / Closed stirrup.</param>
        /// <param name="distance">Longitudinal distance between stirrups.</param>
        /// <param name="shearCheck">Status of shear check, not possible for detailing stirrup.</param>
        /// <param name="torsionCheck">Status of torsion check, not possible for detailing stirrup.</param>
        public Stirrup(PolyLine2D geometry = default(PolyLine2D), double diameter = default(double), ReferenceElement material = default(ReferenceElement), double anchorageLenght = default(double), double diameterOfMandrel = default(double), bool isClosed = default(bool), double distance = default(double), bool shearCheck = default(bool), bool torsionCheck = default(bool))
        {
            this.Geometry = geometry;
            this.Diameter = diameter;
            this.Material = material;
            this.AnchorageLenght = anchorageLenght;
            this.DiameterOfMandrel = diameterOfMandrel;
            this.IsClosed = isClosed;
            this.Distance = distance;
            this.ShearCheck = shearCheck;
            this.TorsionCheck = torsionCheck;
        }

        /// <summary>
        /// Gets or Sets Geometry
        /// </summary>
        [DataMember(Name = "geometry", EmitDefaultValue = false)]
        public PolyLine2D Geometry { get; set; }

        /// <summary>
        /// Diameter
        /// </summary>
        /// <value>Diameter</value>
        [DataMember(Name = "diameter", EmitDefaultValue = false)]
        public double Diameter { get; set; }

        /// <summary>
        /// Gets or Sets Material
        /// </summary>
        [DataMember(Name = "material", EmitDefaultValue = false)]
        public ReferenceElement Material { get; set; }

        /// <summary>
        /// Anchorage Lenght
        /// </summary>
        /// <value>Anchorage Lenght</value>
        [DataMember(Name = "anchorageLenght", EmitDefaultValue = false)]
        public double AnchorageLenght { get; set; }

        /// <summary>
        /// Radius of stirrup mandrel - refering to stirrup axis
        /// </summary>
        /// <value>Radius of stirrup mandrel - refering to stirrup axis</value>
        [DataMember(Name = "diameterOfMandrel", EmitDefaultValue = false)]
        public double DiameterOfMandrel { get; set; }

        /// <summary>
        /// Open / Closed stirrup
        /// </summary>
        /// <value>Open / Closed stirrup</value>
        [DataMember(Name = "isClosed", EmitDefaultValue = true)]
        public bool IsClosed { get; set; }

        /// <summary>
        /// Longitudinal distance between stirrups
        /// </summary>
        /// <value>Longitudinal distance between stirrups</value>
        [DataMember(Name = "distance", EmitDefaultValue = false)]
        public double Distance { get; set; }

        /// <summary>
        /// Status of shear check, not possible for detailing stirrup
        /// </summary>
        /// <value>Status of shear check, not possible for detailing stirrup</value>
        [DataMember(Name = "shearCheck", EmitDefaultValue = true)]
        public bool ShearCheck { get; set; }

        /// <summary>
        /// Status of torsion check, not possible for detailing stirrup
        /// </summary>
        /// <value>Status of torsion check, not possible for detailing stirrup</value>
        [DataMember(Name = "torsionCheck", EmitDefaultValue = true)]
        public bool TorsionCheck { get; set; }

        /// <summary>
        /// Returns the string presentation of the object
        /// </summary>
        /// <returns>String presentation of the object</returns>
        public override string ToString()
        {
            StringBuilder sb = new StringBuilder();
            sb.Append("class Stirrup {\n");
            sb.Append("  Geometry: ").Append(Geometry).Append("\n");
            sb.Append("  Diameter: ").Append(Diameter).Append("\n");
            sb.Append("  Material: ").Append(Material).Append("\n");
            sb.Append("  AnchorageLenght: ").Append(AnchorageLenght).Append("\n");
            sb.Append("  DiameterOfMandrel: ").Append(DiameterOfMandrel).Append("\n");
            sb.Append("  IsClosed: ").Append(IsClosed).Append("\n");
            sb.Append("  Distance: ").Append(Distance).Append("\n");
            sb.Append("  ShearCheck: ").Append(ShearCheck).Append("\n");
            sb.Append("  TorsionCheck: ").Append(TorsionCheck).Append("\n");
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
