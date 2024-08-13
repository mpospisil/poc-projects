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
    /// StiffnessChekDataIdeaStatiCaConnectionChecks
    /// </summary>
    [DataContract(Name = "StiffnessChekData-IdeaStatiCa_ConnectionChecks")]
    public partial class StiffnessChekDataIdeaStatiCaConnectionChecks : IValidatableObject
    {

        /// <summary>
        /// Gets or Sets ComponentId
        /// </summary>
        [DataMember(Name = "componentId", EmitDefaultValue = false)]
        public StiffnessChekDataLoadComponentIdeaStatiCaConnectionChecks? ComponentId { get; set; }
        /// <summary>
        /// Initializes a new instance of the <see cref="StiffnessChekDataIdeaStatiCaConnectionChecks" /> class.
        /// </summary>
        /// <param name="beamId">beamId.</param>
        /// <param name="component">component.</param>
        /// <param name="componentId">componentId.</param>
        /// <param name="myz">myz.</param>
        /// <param name="mxStart">mxStart.</param>
        /// <param name="myStart">myStart.</param>
        /// <param name="mzStart">mzStart.</param>
        /// <param name="ryz">ryz.</param>
        /// <param name="ryzCapacity">ryzCapacity.</param>
        /// <param name="kyz">kyz.</param>
        /// <param name="kyzClassification">kyzClassification.</param>
        /// <param name="kyzLimitRigid">kyzLimitRigid.</param>
        /// <param name="kyzLimitPinned">kyzLimitPinned.</param>
        /// <param name="nx">nx.</param>
        /// <param name="nxStart">nxStart.</param>
        /// <param name="dx">dx.</param>
        /// <param name="kx">kx.</param>
        /// <param name="points">points.</param>
        /// <param name="pointsShell">pointsShell.</param>
        /// <param name="pointsLinear">pointsLinear.</param>
        /// <param name="nMcrd">nMcrd.</param>
        /// <param name="nMjrd">nMjrd.</param>
        /// <param name="theoreticalLength">theoreticalLength.</param>
        /// <param name="sjini">sjini.</param>
        /// <param name="id">id.</param>
        /// <param name="name">name.</param>
        /// <param name="checkStatus">checkStatus.</param>
        /// <param name="limitCheckStatus">limitCheckStatus.</param>
        /// <param name="loadCaseId">loadCaseId.</param>
        /// <param name="loadCase">loadCase.</param>
        /// <param name="maxUnityCheck">maxUnityCheck.</param>
        /// <param name="form">form.</param>
        public StiffnessChekDataIdeaStatiCaConnectionChecks(int beamId = default(int), string component = default(string), StiffnessChekDataLoadComponentIdeaStatiCaConnectionChecks? componentId = default(StiffnessChekDataLoadComponentIdeaStatiCaConnectionChecks?), double myz = default(double), double mxStart = default(double), double myStart = default(double), double mzStart = default(double), double ryz = default(double), double ryzCapacity = default(double), double kyz = default(double), string kyzClassification = default(string), double kyzLimitRigid = default(double), double kyzLimitPinned = default(double), double nx = default(double), double nxStart = default(double), double dx = default(double), double kx = default(double), List<CIGiCL2DPoint2DCIGeometry2D> points = default(List<CIGiCL2DPoint2DCIGeometry2D>), List<CIGiCL2DPoint2DCIGeometry2D> pointsShell = default(List<CIGiCL2DPoint2DCIGeometry2D>), List<CIGiCL2DPoint2DCIGeometry2D> pointsLinear = default(List<CIGiCL2DPoint2DCIGeometry2D>), double nMcrd = default(double), double nMjrd = default(double), double theoreticalLength = default(double), double sjini = default(double), int id = default(int), string name = default(string), bool checkStatus = default(bool), bool limitCheckStatus = default(bool), int loadCaseId = default(int), string loadCase = default(string), double maxUnityCheck = default(double), string form = default(string))
        {
            this.BeamId = beamId;
            this.Component = component;
            this.ComponentId = componentId;
            this.Myz = myz;
            this.MxStart = mxStart;
            this.MyStart = myStart;
            this.MzStart = mzStart;
            this.Ryz = ryz;
            this.RyzCapacity = ryzCapacity;
            this.Kyz = kyz;
            this.KyzClassification = kyzClassification;
            this.KyzLimitRigid = kyzLimitRigid;
            this.KyzLimitPinned = kyzLimitPinned;
            this.Nx = nx;
            this.NxStart = nxStart;
            this.Dx = dx;
            this.Kx = kx;
            this.Points = points;
            this.PointsShell = pointsShell;
            this.PointsLinear = pointsLinear;
            this.NMcrd = nMcrd;
            this.NMjrd = nMjrd;
            this.TheoreticalLength = theoreticalLength;
            this.Sjini = sjini;
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
        /// Gets or Sets BeamId
        /// </summary>
        [DataMember(Name = "beamId", EmitDefaultValue = false)]
        public int BeamId { get; set; }

        /// <summary>
        /// Gets or Sets Component
        /// </summary>
        [DataMember(Name = "component", EmitDefaultValue = true)]
        public string Component { get; set; }

        /// <summary>
        /// Gets or Sets Myz
        /// </summary>
        [DataMember(Name = "myz", EmitDefaultValue = false)]
        public double Myz { get; set; }

        /// <summary>
        /// Gets or Sets MxStart
        /// </summary>
        [DataMember(Name = "mxStart", EmitDefaultValue = false)]
        public double MxStart { get; set; }

        /// <summary>
        /// Gets or Sets MyStart
        /// </summary>
        [DataMember(Name = "myStart", EmitDefaultValue = false)]
        public double MyStart { get; set; }

        /// <summary>
        /// Gets or Sets MzStart
        /// </summary>
        [DataMember(Name = "mzStart", EmitDefaultValue = false)]
        public double MzStart { get; set; }

        /// <summary>
        /// Gets or Sets Ryz
        /// </summary>
        [DataMember(Name = "ryz", EmitDefaultValue = false)]
        public double Ryz { get; set; }

        /// <summary>
        /// Gets or Sets RyzCapacity
        /// </summary>
        [DataMember(Name = "ryzCapacity", EmitDefaultValue = false)]
        public double RyzCapacity { get; set; }

        /// <summary>
        /// Gets or Sets Kyz
        /// </summary>
        [DataMember(Name = "kyz", EmitDefaultValue = false)]
        public double Kyz { get; set; }

        /// <summary>
        /// Gets or Sets KyzClassification
        /// </summary>
        [DataMember(Name = "kyzClassification", EmitDefaultValue = true)]
        public string KyzClassification { get; set; }

        /// <summary>
        /// Gets or Sets KyzLimitRigid
        /// </summary>
        [DataMember(Name = "kyzLimitRigid", EmitDefaultValue = false)]
        public double KyzLimitRigid { get; set; }

        /// <summary>
        /// Gets or Sets KyzLimitPinned
        /// </summary>
        [DataMember(Name = "kyzLimitPinned", EmitDefaultValue = false)]
        public double KyzLimitPinned { get; set; }

        /// <summary>
        /// Gets or Sets Nx
        /// </summary>
        [DataMember(Name = "nx", EmitDefaultValue = false)]
        public double Nx { get; set; }

        /// <summary>
        /// Gets or Sets NxStart
        /// </summary>
        [DataMember(Name = "nxStart", EmitDefaultValue = false)]
        public double NxStart { get; set; }

        /// <summary>
        /// Gets or Sets Dx
        /// </summary>
        [DataMember(Name = "dx", EmitDefaultValue = false)]
        public double Dx { get; set; }

        /// <summary>
        /// Gets or Sets Kx
        /// </summary>
        [DataMember(Name = "kx", EmitDefaultValue = false)]
        public double Kx { get; set; }

        /// <summary>
        /// Gets or Sets Points
        /// </summary>
        [DataMember(Name = "points", EmitDefaultValue = true)]
        public List<CIGiCL2DPoint2DCIGeometry2D> Points { get; set; }

        /// <summary>
        /// Gets or Sets PointsShell
        /// </summary>
        [DataMember(Name = "pointsShell", EmitDefaultValue = true)]
        public List<CIGiCL2DPoint2DCIGeometry2D> PointsShell { get; set; }

        /// <summary>
        /// Gets or Sets PointsLinear
        /// </summary>
        [DataMember(Name = "pointsLinear", EmitDefaultValue = true)]
        public List<CIGiCL2DPoint2DCIGeometry2D> PointsLinear { get; set; }

        /// <summary>
        /// Gets or Sets NMcrd
        /// </summary>
        [DataMember(Name = "nMcrd", EmitDefaultValue = false)]
        public double NMcrd { get; set; }

        /// <summary>
        /// Gets or Sets NMjrd
        /// </summary>
        [DataMember(Name = "nMjrd", EmitDefaultValue = false)]
        public double NMjrd { get; set; }

        /// <summary>
        /// Gets or Sets TheoreticalLength
        /// </summary>
        [DataMember(Name = "theoreticalLength", EmitDefaultValue = false)]
        public double TheoreticalLength { get; set; }

        /// <summary>
        /// Gets or Sets Sjini
        /// </summary>
        [DataMember(Name = "sjini", EmitDefaultValue = false)]
        public double Sjini { get; set; }

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
            sb.Append("class StiffnessChekDataIdeaStatiCaConnectionChecks {\n");
            sb.Append("  BeamId: ").Append(BeamId).Append("\n");
            sb.Append("  Component: ").Append(Component).Append("\n");
            sb.Append("  ComponentId: ").Append(ComponentId).Append("\n");
            sb.Append("  Myz: ").Append(Myz).Append("\n");
            sb.Append("  MxStart: ").Append(MxStart).Append("\n");
            sb.Append("  MyStart: ").Append(MyStart).Append("\n");
            sb.Append("  MzStart: ").Append(MzStart).Append("\n");
            sb.Append("  Ryz: ").Append(Ryz).Append("\n");
            sb.Append("  RyzCapacity: ").Append(RyzCapacity).Append("\n");
            sb.Append("  Kyz: ").Append(Kyz).Append("\n");
            sb.Append("  KyzClassification: ").Append(KyzClassification).Append("\n");
            sb.Append("  KyzLimitRigid: ").Append(KyzLimitRigid).Append("\n");
            sb.Append("  KyzLimitPinned: ").Append(KyzLimitPinned).Append("\n");
            sb.Append("  Nx: ").Append(Nx).Append("\n");
            sb.Append("  NxStart: ").Append(NxStart).Append("\n");
            sb.Append("  Dx: ").Append(Dx).Append("\n");
            sb.Append("  Kx: ").Append(Kx).Append("\n");
            sb.Append("  Points: ").Append(Points).Append("\n");
            sb.Append("  PointsShell: ").Append(PointsShell).Append("\n");
            sb.Append("  PointsLinear: ").Append(PointsLinear).Append("\n");
            sb.Append("  NMcrd: ").Append(NMcrd).Append("\n");
            sb.Append("  NMjrd: ").Append(NMjrd).Append("\n");
            sb.Append("  TheoreticalLength: ").Append(TheoreticalLength).Append("\n");
            sb.Append("  Sjini: ").Append(Sjini).Append("\n");
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
