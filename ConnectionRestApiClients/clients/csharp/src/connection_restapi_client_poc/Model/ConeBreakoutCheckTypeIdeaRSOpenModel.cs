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
    /// Defines ConeBreakoutCheckType-IdeaRS_OpenModel
    /// </summary>
    [JsonConverter(typeof(StringEnumConverter))]
    public enum ConeBreakoutCheckTypeIdeaRSOpenModel
    {
        /// <summary>
        /// Enum Both for value: both
        /// </summary>
        [EnumMember(Value = "both")]
        Both = 1,

        /// <summary>
        /// Enum Tension for value: tension
        /// </summary>
        [EnumMember(Value = "tension")]
        Tension = 2,

        /// <summary>
        /// Enum Shear for value: shear
        /// </summary>
        [EnumMember(Value = "shear")]
        Shear = 3,

        /// <summary>
        /// Enum None for value: none
        /// </summary>
        [EnumMember(Value = "none")]
        None = 4
    }

}
