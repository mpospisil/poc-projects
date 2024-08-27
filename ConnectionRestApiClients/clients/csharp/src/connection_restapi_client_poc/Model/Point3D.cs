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
    /// Represents an x- , y- an z-coordinates in three-dimensional space.
    /// </summary>
    [DataContract(Name = "Point3D")]
    public partial class Point3D : IValidatableObject
    {
        /// <summary>
        /// Initializes a new instance of the <see cref="Point3D" /> class.
        /// </summary>
        /// <param name="x">Gets or sets the X-coordinate value.</param>
        /// <param name="y">Gets or sets the Y-coordinate value.</param>
        /// <param name="z">Gets or sets the Z-coordinate value.</param>
        /// <param name="id">Element Id.</param>
        public Point3D(double x = default(double), double y = default(double), double z = default(double), int id = default(int))
        {
            this.X = x;
            this.Y = y;
            this.Z = z;
            this.Id = id;
        }

        /// <summary>
        /// Gets or sets the X-coordinate value
        /// </summary>
        /// <value>Gets or sets the X-coordinate value</value>
        [DataMember(Name = "x", EmitDefaultValue = false)]
        public double X { get; set; }

        /// <summary>
        /// Gets or sets the Y-coordinate value
        /// </summary>
        /// <value>Gets or sets the Y-coordinate value</value>
        [DataMember(Name = "y", EmitDefaultValue = false)]
        public double Y { get; set; }

        /// <summary>
        /// Gets or sets the Z-coordinate value
        /// </summary>
        /// <value>Gets or sets the Z-coordinate value</value>
        [DataMember(Name = "z", EmitDefaultValue = false)]
        public double Z { get; set; }

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
            sb.Append("class Point3D {\n");
            sb.Append("  X: ").Append(X).Append("\n");
            sb.Append("  Y: ").Append(Y).Append("\n");
            sb.Append("  Z: ").Append(Z).Append("\n");
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
