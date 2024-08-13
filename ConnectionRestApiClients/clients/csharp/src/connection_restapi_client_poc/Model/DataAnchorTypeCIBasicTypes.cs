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
    /// Defines Data_AnchorType-CI_BasicTypes
    /// </summary>
    [JsonConverter(typeof(StringEnumConverter))]
    public enum DataAnchorTypeCIBasicTypes
    {
        /// <summary>
        /// Enum Straight for value: straight
        /// </summary>
        [EnumMember(Value = "straight")]
        Straight = 1,

        /// <summary>
        /// Enum WasherPlateCircular for value: washerPlateCircular
        /// </summary>
        [EnumMember(Value = "washerPlateCircular")]
        WasherPlateCircular = 2,

        /// <summary>
        /// Enum WasherPlateRectangular for value: washerPlateRectangular
        /// </summary>
        [EnumMember(Value = "washerPlateRectangular")]
        WasherPlateRectangular = 3,

        /// <summary>
        /// Enum Hook for value: hook
        /// </summary>
        [EnumMember(Value = "hook")]
        Hook = 4
    }

}
