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
    /// Defines Data_WeldTypeCode-CI_BasicTypes
    /// </summary>
    [JsonConverter(typeof(StringEnumConverter))]
    public enum DataWeldTypeCodeCIBasicTypes
    {
        /// <summary>
        /// Enum NotSpecified for value: notSpecified
        /// </summary>
        [EnumMember(Value = "notSpecified")]
        NotSpecified = 1,

        /// <summary>
        /// Enum Fillet for value: fillet
        /// </summary>
        [EnumMember(Value = "fillet")]
        Fillet = 2,

        /// <summary>
        /// Enum DoubleFillet for value: doubleFillet
        /// </summary>
        [EnumMember(Value = "doubleFillet")]
        DoubleFillet = 3,

        /// <summary>
        /// Enum Bevel for value: bevel
        /// </summary>
        [EnumMember(Value = "bevel")]
        Bevel = 4,

        /// <summary>
        /// Enum Pjp for value: pjp
        /// </summary>
        [EnumMember(Value = "pjp")]
        Pjp = 5,

        /// <summary>
        /// Enum PjpRear for value: pjpRear
        /// </summary>
        [EnumMember(Value = "pjpRear")]
        PjpRear = 6,

        /// <summary>
        /// Enum LengthAtHaunch for value: lengthAtHaunch
        /// </summary>
        [EnumMember(Value = "lengthAtHaunch")]
        LengthAtHaunch = 7,

        /// <summary>
        /// Enum FilletRear for value: filletRear
        /// </summary>
        [EnumMember(Value = "filletRear")]
        FilletRear = 8,

        /// <summary>
        /// Enum Contact for value: contact
        /// </summary>
        [EnumMember(Value = "contact")]
        Contact = 9,

        /// <summary>
        /// Enum Intermittent for value: intermittent
        /// </summary>
        [EnumMember(Value = "intermittent")]
        Intermittent = 10
    }

}
