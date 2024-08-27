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
    /// WeldEvaluation
    /// </summary>
    /// <value>WeldEvaluation</value>
    [JsonConverter(typeof(StringEnumConverter))]
    public enum WeldEvaluation
    {
        /// <summary>
        /// Enum MaxForceElement for value: maxForceElement
        /// </summary>
        [EnumMember(Value = "maxForceElement")]
        MaxForceElement = 1,

        /// <summary>
        /// Enum ForceResultant for value: forceResultant
        /// </summary>
        [EnumMember(Value = "forceResultant")]
        ForceResultant = 2,

        /// <summary>
        /// Enum ApplyPlasticWelds for value: applyPlasticWelds
        /// </summary>
        [EnumMember(Value = "applyPlasticWelds")]
        ApplyPlasticWelds = 3
    }

}
