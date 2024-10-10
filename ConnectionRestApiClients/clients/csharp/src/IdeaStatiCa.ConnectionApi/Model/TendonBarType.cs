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
    /// Tendon bar type
    /// </summary>
    /// <value>Tendon bar type</value>
    [JsonConverter(typeof(StringEnumConverter))]
    public enum TendonBarType
    {
        /// <summary>
        /// Enum Posttensioned for value: posttensioned
        /// </summary>
        [EnumMember(Value = "posttensioned")]
        Posttensioned = 1,

        /// <summary>
        /// Enum Pretensioned for value: pretensioned
        /// </summary>
        [EnumMember(Value = "pretensioned")]
        Pretensioned = 2
    }

}