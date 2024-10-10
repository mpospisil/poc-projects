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
    /// Type of curvature - thermal specific heat
    /// </summary>
    /// <value>Type of curvature - thermal specific heat</value>
    [JsonConverter(typeof(StringEnumConverter))]
    public enum ThermalSpecificHeatState
    {
        /// <summary>
        /// Enum None for value: none
        /// </summary>
        [EnumMember(Value = "none")]
        None = 1,

        /// <summary>
        /// Enum Code for value: code
        /// </summary>
        [EnumMember(Value = "code")]
        Code = 2,

        /// <summary>
        /// Enum User for value: user
        /// </summary>
        [EnumMember(Value = "user")]
        User = 3
    }

}