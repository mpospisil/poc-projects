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
    /// Type of loading
    /// </summary>
    /// <value>Type of loading</value>
    [JsonConverter(typeof(StringEnumConverter))]
    public enum ResultLoadingTypeIdeaRSOpenModel
    {
        /// <summary>
        /// Enum LoadCase for value: loadCase
        /// </summary>
        [EnumMember(Value = "loadCase")]
        LoadCase = 1,

        /// <summary>
        /// Enum Combination for value: combination
        /// </summary>
        [EnumMember(Value = "combination")]
        Combination = 2,

        /// <summary>
        /// Enum ResultClass for value: resultClass
        /// </summary>
        [EnumMember(Value = "resultClass")]
        ResultClass = 3
    }

}
