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
    /// Posttensioned reinforcement type
    /// </summary>
    /// <value>Posttensioned reinforcement type</value>
    [JsonConverter(typeof(StringEnumConverter))]
    public enum FatigueTypeOfPrestressingSteel
    {
        /// <summary>
        /// Enum PostTensioningSingleStrandsInPlasticDucts for value: postTensioningSingleStrandsInPlasticDucts
        /// </summary>
        [EnumMember(Value = "postTensioningSingleStrandsInPlasticDucts")]
        PostTensioningSingleStrandsInPlasticDucts = 1,

        /// <summary>
        /// Enum PostTensioningStraightTendonsOrCurvedTendonsInPlasticDucts for value: postTensioningStraightTendonsOrCurvedTendonsInPlasticDucts
        /// </summary>
        [EnumMember(Value = "postTensioningStraightTendonsOrCurvedTendonsInPlasticDucts")]
        PostTensioningStraightTendonsOrCurvedTendonsInPlasticDucts = 2,

        /// <summary>
        /// Enum PostTensioningCurvedTendonsInSteelDucts for value: postTensioningCurvedTendonsInSteelDucts
        /// </summary>
        [EnumMember(Value = "postTensioningCurvedTendonsInSteelDucts")]
        PostTensioningCurvedTendonsInSteelDucts = 3,

        /// <summary>
        /// Enum PostTensioningSplicingDevices for value: postTensioningSplicingDevices
        /// </summary>
        [EnumMember(Value = "postTensioningSplicingDevices")]
        PostTensioningSplicingDevices = 4,

        /// <summary>
        /// Enum PreTensioning for value: preTensioning
        /// </summary>
        [EnumMember(Value = "preTensioning")]
        PreTensioning = 5,

        /// <summary>
        /// Enum ExternalTendon for value: externalTendon
        /// </summary>
        [EnumMember(Value = "externalTendon")]
        ExternalTendon = 6
    }

}
