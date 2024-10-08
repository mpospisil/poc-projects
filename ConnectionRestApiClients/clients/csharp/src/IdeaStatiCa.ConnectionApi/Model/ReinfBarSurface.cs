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
    /// Reinforcement bar surface
    /// </summary>
    /// <value>Reinforcement bar surface</value>
    [JsonConverter(typeof(StringEnumConverter))]
    public enum ReinfBarSurface
    {
        /// <summary>
        /// Enum Smooth for value: smooth
        /// </summary>
        [EnumMember(Value = "smooth")]
        Smooth = 1,

        /// <summary>
        /// Enum Ribbed for value: ribbed
        /// </summary>
        [EnumMember(Value = "ribbed")]
        Ribbed = 2
    }

}
