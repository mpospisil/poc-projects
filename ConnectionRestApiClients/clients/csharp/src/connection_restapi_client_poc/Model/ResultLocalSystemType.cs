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
    /// Type of local system of result
    /// </summary>
    /// <value>Type of local system of result</value>
    [JsonConverter(typeof(StringEnumConverter))]
    public enum ResultLocalSystemType
    {
        /// <summary>
        /// Enum Local for value: local
        /// </summary>
        [EnumMember(Value = "local")]
        Local = 1,

        /// <summary>
        /// Enum Global for value: global
        /// </summary>
        [EnumMember(Value = "global")]
        Global = 2,

        /// <summary>
        /// Enum Principle for value: principle
        /// </summary>
        [EnumMember(Value = "principle")]
        Principle = 3
    }

}
