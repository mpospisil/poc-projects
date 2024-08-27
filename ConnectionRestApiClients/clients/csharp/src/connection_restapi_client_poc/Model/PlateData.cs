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
    /// Provides data of the single plate
    /// </summary>
    [DataContract(Name = "PlateData")]
    public partial class PlateData : IValidatableObject
    {
        /// <summary>
        /// Initializes a new instance of the <see cref="PlateData" /> class.
        /// </summary>
        /// <param name="name">Name of the plate.</param>
        /// <param name="thickness">Thickness of the plate.</param>
        /// <param name="material">Name of the material.</param>
        /// <param name="outlinePoints">Outline points.</param>
        /// <param name="origin">origin.</param>
        /// <param name="axisX">axisX.</param>
        /// <param name="axisY">axisY.</param>
        /// <param name="axisZ">axisZ.</param>
        /// <param name="region">Geometry of the plate in svg format. In next version will be mark as OBSOLETE! New use property Geometry.</param>
        /// <param name="geometry">geometry.</param>
        /// <param name="originalModelId">Get or set the identification in the original model  In the case of the imported connection from another application.</param>
        /// <param name="isNegativeObject">Is negative object.</param>
        /// <param name="id">Element Id.</param>
        public PlateData(string name = default(string), double thickness = default(double), string material = default(string), List<Point2D> outlinePoints = default(List<Point2D>), Point3D origin = default(Point3D), Vector3D axisX = default(Vector3D), Vector3D axisY = default(Vector3D), Vector3D axisZ = default(Vector3D), string region = default(string), Region2D geometry = default(Region2D), string originalModelId = default(string), bool isNegativeObject = default(bool), int id = default(int))
        {
            this.Name = name;
            this.Thickness = thickness;
            this.Material = material;
            this.OutlinePoints = outlinePoints;
            this.Origin = origin;
            this.AxisX = axisX;
            this.AxisY = axisY;
            this.AxisZ = axisZ;
            this.Region = region;
            this.Geometry = geometry;
            this.OriginalModelId = originalModelId;
            this.IsNegativeObject = isNegativeObject;
            this.Id = id;
        }

        /// <summary>
        /// Name of the plate
        /// </summary>
        /// <value>Name of the plate</value>
        [DataMember(Name = "name", EmitDefaultValue = true)]
        public string Name { get; set; }

        /// <summary>
        /// Thickness of the plate
        /// </summary>
        /// <value>Thickness of the plate</value>
        [DataMember(Name = "thickness", EmitDefaultValue = false)]
        public double Thickness { get; set; }

        /// <summary>
        /// Name of the material
        /// </summary>
        /// <value>Name of the material</value>
        [DataMember(Name = "material", EmitDefaultValue = true)]
        public string Material { get; set; }

        /// <summary>
        /// Outline points
        /// </summary>
        /// <value>Outline points</value>
        [DataMember(Name = "outlinePoints", EmitDefaultValue = true)]
        public List<Point2D> OutlinePoints { get; set; }

        /// <summary>
        /// Gets or Sets Origin
        /// </summary>
        [DataMember(Name = "origin", EmitDefaultValue = false)]
        public Point3D Origin { get; set; }

        /// <summary>
        /// Gets or Sets AxisX
        /// </summary>
        [DataMember(Name = "axisX", EmitDefaultValue = false)]
        public Vector3D AxisX { get; set; }

        /// <summary>
        /// Gets or Sets AxisY
        /// </summary>
        [DataMember(Name = "axisY", EmitDefaultValue = false)]
        public Vector3D AxisY { get; set; }

        /// <summary>
        /// Gets or Sets AxisZ
        /// </summary>
        [DataMember(Name = "axisZ", EmitDefaultValue = false)]
        public Vector3D AxisZ { get; set; }

        /// <summary>
        /// Geometry of the plate in svg format. In next version will be mark as OBSOLETE! New use property Geometry
        /// </summary>
        /// <value>Geometry of the plate in svg format. In next version will be mark as OBSOLETE! New use property Geometry</value>
        [DataMember(Name = "region", EmitDefaultValue = true)]
        public string Region { get; set; }

        /// <summary>
        /// Gets or Sets Geometry
        /// </summary>
        [DataMember(Name = "geometry", EmitDefaultValue = false)]
        public Region2D Geometry { get; set; }

        /// <summary>
        /// Get or set the identification in the original model  In the case of the imported connection from another application
        /// </summary>
        /// <value>Get or set the identification in the original model  In the case of the imported connection from another application</value>
        [DataMember(Name = "originalModelId", EmitDefaultValue = true)]
        public string OriginalModelId { get; set; }

        /// <summary>
        /// Is negative object
        /// </summary>
        /// <value>Is negative object</value>
        [DataMember(Name = "isNegativeObject", EmitDefaultValue = true)]
        public bool IsNegativeObject { get; set; }

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
            sb.Append("class PlateData {\n");
            sb.Append("  Name: ").Append(Name).Append("\n");
            sb.Append("  Thickness: ").Append(Thickness).Append("\n");
            sb.Append("  Material: ").Append(Material).Append("\n");
            sb.Append("  OutlinePoints: ").Append(OutlinePoints).Append("\n");
            sb.Append("  Origin: ").Append(Origin).Append("\n");
            sb.Append("  AxisX: ").Append(AxisX).Append("\n");
            sb.Append("  AxisY: ").Append(AxisY).Append("\n");
            sb.Append("  AxisZ: ").Append(AxisZ).Append("\n");
            sb.Append("  Region: ").Append(Region).Append("\n");
            sb.Append("  Geometry: ").Append(Geometry).Append("\n");
            sb.Append("  OriginalModelId: ").Append(OriginalModelId).Append("\n");
            sb.Append("  IsNegativeObject: ").Append(IsNegativeObject).Append("\n");
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
