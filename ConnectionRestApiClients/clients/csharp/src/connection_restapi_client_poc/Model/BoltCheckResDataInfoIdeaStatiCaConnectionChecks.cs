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
    /// BoltCheckResDataInfoIdeaStatiCaConnectionChecks
    /// </summary>
    [DataContract(Name = "BoltCheckResDataInfo-IdeaStatiCa_ConnectionChecks")]
    public partial class BoltCheckResDataInfoIdeaStatiCaConnectionChecks : IValidatableObject
    {
        /// <summary>
        /// Initializes a new instance of the <see cref="BoltCheckResDataInfoIdeaStatiCaConnectionChecks" /> class.
        /// </summary>
        /// <param name="boltTensionResistance">boltTensionResistance.</param>
        /// <param name="compressionResistance">compressionResistance.</param>
        /// <param name="momentResistance">momentResistance.</param>
        /// <param name="boltPunchingResistance">boltPunchingResistance.</param>
        /// <param name="boltShearResistance">boltShearResistance.</param>
        /// <param name="boltShearResistanceAnchor">boltShearResistanceAnchor.</param>
        /// <param name="boltShearResistanceTension">boltShearResistanceTension.</param>
        /// <param name="anchorStiffness">anchorStiffness.</param>
        /// <param name="slipResistanceCoeff">slipResistanceCoeff.</param>
        /// <param name="standOffGap">standOffGap.</param>
        /// <param name="boltPreloadedForce">boltPreloadedForce.</param>
        /// <param name="id">id.</param>
        /// <param name="name">name.</param>
        /// <param name="checkStatus">checkStatus.</param>
        /// <param name="limitCheckStatus">limitCheckStatus.</param>
        /// <param name="loadCaseId">loadCaseId.</param>
        /// <param name="loadCase">loadCase.</param>
        /// <param name="maxUnityCheck">maxUnityCheck.</param>
        /// <param name="form">form.</param>
        public BoltCheckResDataInfoIdeaStatiCaConnectionChecks(double boltTensionResistance = default(double), double compressionResistance = default(double), double momentResistance = default(double), double boltPunchingResistance = default(double), double boltShearResistance = default(double), double boltShearResistanceAnchor = default(double), double boltShearResistanceTension = default(double), double anchorStiffness = default(double), double slipResistanceCoeff = default(double), double standOffGap = default(double), double boltPreloadedForce = default(double), int id = default(int), string name = default(string), bool checkStatus = default(bool), bool limitCheckStatus = default(bool), int loadCaseId = default(int), string loadCase = default(string), double maxUnityCheck = default(double), string form = default(string))
        {
            this.BoltTensionResistance = boltTensionResistance;
            this.CompressionResistance = compressionResistance;
            this.MomentResistance = momentResistance;
            this.BoltPunchingResistance = boltPunchingResistance;
            this.BoltShearResistance = boltShearResistance;
            this.BoltShearResistanceAnchor = boltShearResistanceAnchor;
            this.BoltShearResistanceTension = boltShearResistanceTension;
            this.AnchorStiffness = anchorStiffness;
            this.SlipResistanceCoeff = slipResistanceCoeff;
            this.StandOffGap = standOffGap;
            this.BoltPreloadedForce = boltPreloadedForce;
            this.Id = id;
            this.Name = name;
            this.CheckStatus = checkStatus;
            this.LimitCheckStatus = limitCheckStatus;
            this.LoadCaseId = loadCaseId;
            this.LoadCase = loadCase;
            this.MaxUnityCheck = maxUnityCheck;
            this.Form = form;
        }

        /// <summary>
        /// Gets or Sets BoltTensionResistance
        /// </summary>
        [DataMember(Name = "boltTensionResistance", EmitDefaultValue = false)]
        public double BoltTensionResistance { get; set; }

        /// <summary>
        /// Gets or Sets CompressionResistance
        /// </summary>
        [DataMember(Name = "compressionResistance", EmitDefaultValue = false)]
        public double CompressionResistance { get; set; }

        /// <summary>
        /// Gets or Sets MomentResistance
        /// </summary>
        [DataMember(Name = "momentResistance", EmitDefaultValue = false)]
        public double MomentResistance { get; set; }

        /// <summary>
        /// Gets or Sets BoltPunchingResistance
        /// </summary>
        [DataMember(Name = "boltPunchingResistance", EmitDefaultValue = false)]
        public double BoltPunchingResistance { get; set; }

        /// <summary>
        /// Gets or Sets BoltShearResistance
        /// </summary>
        [DataMember(Name = "boltShearResistance", EmitDefaultValue = false)]
        public double BoltShearResistance { get; set; }

        /// <summary>
        /// Gets or Sets BoltShearResistanceAnchor
        /// </summary>
        [DataMember(Name = "boltShearResistanceAnchor", EmitDefaultValue = false)]
        public double BoltShearResistanceAnchor { get; set; }

        /// <summary>
        /// Gets or Sets BoltShearResistanceTension
        /// </summary>
        [DataMember(Name = "boltShearResistanceTension", EmitDefaultValue = false)]
        public double BoltShearResistanceTension { get; set; }

        /// <summary>
        /// Gets or Sets AnchorStiffness
        /// </summary>
        [DataMember(Name = "anchorStiffness", EmitDefaultValue = false)]
        public double AnchorStiffness { get; set; }

        /// <summary>
        /// Gets or Sets SlipResistanceCoeff
        /// </summary>
        [DataMember(Name = "slipResistanceCoeff", EmitDefaultValue = false)]
        public double SlipResistanceCoeff { get; set; }

        /// <summary>
        /// Gets or Sets StandOffGap
        /// </summary>
        [DataMember(Name = "standOffGap", EmitDefaultValue = false)]
        public double StandOffGap { get; set; }

        /// <summary>
        /// Gets or Sets BoltPreloadedForce
        /// </summary>
        [DataMember(Name = "boltPreloadedForce", EmitDefaultValue = false)]
        public double BoltPreloadedForce { get; set; }

        /// <summary>
        /// Gets or Sets Id
        /// </summary>
        [DataMember(Name = "id", EmitDefaultValue = false)]
        public int Id { get; set; }

        /// <summary>
        /// Gets or Sets Name
        /// </summary>
        [DataMember(Name = "name", EmitDefaultValue = true)]
        public string Name { get; set; }

        /// <summary>
        /// Gets or Sets CheckStatus
        /// </summary>
        [DataMember(Name = "checkStatus", EmitDefaultValue = true)]
        public bool CheckStatus { get; set; }

        /// <summary>
        /// Gets or Sets LimitCheckStatus
        /// </summary>
        [DataMember(Name = "limitCheckStatus", EmitDefaultValue = true)]
        public bool LimitCheckStatus { get; set; }

        /// <summary>
        /// Gets or Sets LoadCaseId
        /// </summary>
        [DataMember(Name = "loadCaseId", EmitDefaultValue = false)]
        public int LoadCaseId { get; set; }

        /// <summary>
        /// Gets or Sets LoadCase
        /// </summary>
        [DataMember(Name = "loadCase", EmitDefaultValue = true)]
        public string LoadCase { get; set; }

        /// <summary>
        /// Gets or Sets MaxUnityCheck
        /// </summary>
        [DataMember(Name = "maxUnityCheck", EmitDefaultValue = false)]
        public double MaxUnityCheck { get; set; }

        /// <summary>
        /// Gets or Sets Form
        /// </summary>
        [DataMember(Name = "form", EmitDefaultValue = true)]
        public string Form { get; set; }

        /// <summary>
        /// Returns the string presentation of the object
        /// </summary>
        /// <returns>String presentation of the object</returns>
        public override string ToString()
        {
            StringBuilder sb = new StringBuilder();
            sb.Append("class BoltCheckResDataInfoIdeaStatiCaConnectionChecks {\n");
            sb.Append("  BoltTensionResistance: ").Append(BoltTensionResistance).Append("\n");
            sb.Append("  CompressionResistance: ").Append(CompressionResistance).Append("\n");
            sb.Append("  MomentResistance: ").Append(MomentResistance).Append("\n");
            sb.Append("  BoltPunchingResistance: ").Append(BoltPunchingResistance).Append("\n");
            sb.Append("  BoltShearResistance: ").Append(BoltShearResistance).Append("\n");
            sb.Append("  BoltShearResistanceAnchor: ").Append(BoltShearResistanceAnchor).Append("\n");
            sb.Append("  BoltShearResistanceTension: ").Append(BoltShearResistanceTension).Append("\n");
            sb.Append("  AnchorStiffness: ").Append(AnchorStiffness).Append("\n");
            sb.Append("  SlipResistanceCoeff: ").Append(SlipResistanceCoeff).Append("\n");
            sb.Append("  StandOffGap: ").Append(StandOffGap).Append("\n");
            sb.Append("  BoltPreloadedForce: ").Append(BoltPreloadedForce).Append("\n");
            sb.Append("  Id: ").Append(Id).Append("\n");
            sb.Append("  Name: ").Append(Name).Append("\n");
            sb.Append("  CheckStatus: ").Append(CheckStatus).Append("\n");
            sb.Append("  LimitCheckStatus: ").Append(LimitCheckStatus).Append("\n");
            sb.Append("  LoadCaseId: ").Append(LoadCaseId).Append("\n");
            sb.Append("  LoadCase: ").Append(LoadCase).Append("\n");
            sb.Append("  MaxUnityCheck: ").Append(MaxUnityCheck).Append("\n");
            sb.Append("  Form: ").Append(Form).Append("\n");
            sb.Append("}\n");
            return sb.ToString();
        }

        /// <summary>
        /// Returns the JSON string presentation of the object
        /// </summary>
        /// <returns>JSON string presentation of the object</returns>
        public virtual string ToJson()
        {
            return Newtonsoft.Json.JsonConvert.SerializeObject(this, Newtonsoft.Json.Formatting.Indented);
        }

        /// <summary>
        /// To validate all properties of the instance
        /// </summary>
        /// <param name="validationContext">Validation context</param>
        /// <returns>Validation Result</returns>
        IEnumerable<ValidationResult> IValidatableObject.Validate(ValidationContext validationContext)
        {
            yield break;
        }
    }

}
