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
using OpenAPIDateConverter = IdeaStatiCa.ConnectionApi.Client.OpenAPIDateConverter;

namespace IdeaStatiCa.ConnectionApi.Model
{
    /// <summary>
    /// Defines a transfer of shear force in bolts.
    /// </summary>
    /// <value>Defines a transfer of shear force in bolts.</value>
    [JsonConverter(typeof(StringEnumConverter))]
    public enum BoltShearType
    {
        /// <summary>
        /// Enum Bearing for value: bearing
        /// </summary>
        [EnumMember(Value = "bearing")]
        Bearing = 1,

        /// <summary>
        /// Enum Interaction for value: interaction
        /// </summary>
        [EnumMember(Value = "interaction")]
        Interaction = 2,

        /// <summary>
        /// Enum Friction for value: friction
        /// </summary>
        [EnumMember(Value = "friction")]
        Friction = 3
    }

}
