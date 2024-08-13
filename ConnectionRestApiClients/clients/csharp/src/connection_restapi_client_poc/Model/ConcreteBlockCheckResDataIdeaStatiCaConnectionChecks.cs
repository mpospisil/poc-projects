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
    /// ConcreteBlockCheckResDataIdeaStatiCaConnectionChecks
    /// </summary>
    [DataContract(Name = "ConcreteBlockCheckResData-IdeaStatiCa_ConnectionChecks")]
    public partial class ConcreteBlockCheckResDataIdeaStatiCaConnectionChecks : IValidatableObject
    {

        /// <summary>
        /// Gets or Sets CrtCompCheckIS
        /// </summary>
        [DataMember(Name = "crtCompCheckIS", EmitDefaultValue = false)]
        public DataCrtCompCheckISCIBasicTypes? CrtCompCheckIS { get; set; }
        /// <summary>
        /// Initializes a new instance of the <see cref="ConcreteBlockCheckResDataIdeaStatiCaConnectionChecks" /> class.
        /// </summary>
        /// <param name="fjd">fjd.</param>
        /// <param name="averageStress">averageStress.</param>
        /// <param name="nsd">nsd.</param>
        /// <param name="aeff">aeff.</param>
        /// <param name="aeffCenterGravity">aeffCenterGravity.</param>
        /// <param name="centerTension">centerTension.</param>
        /// <param name="centerCompression">centerCompression.</param>
        /// <param name="aeff2">aeff2.</param>
        /// <param name="supportingRegions">supportingRegions.</param>
        /// <param name="aeffNet">aeffNet.</param>
        /// <param name="unityCheckStress">unityCheckStress.</param>
        /// <param name="kj">kj.</param>
        /// <param name="addBearingWidth">addBearingWidth.</param>
        /// <param name="effAreaOfBasePlates">effAreaOfBasePlates.</param>
        /// <param name="gammaC">gammaC.</param>
        /// <param name="fck">fck.</param>
        /// <param name="fckFactored">fckFactored.</param>
        /// <param name="betaj">betaj.</param>
        /// <param name="alphaCC">alphaCC.</param>
        /// <param name="fc">fc.</param>
        /// <param name="phiCrt">phiCrt.</param>
        /// <param name="omegaCrt">omegaCrt.</param>
        /// <param name="fckExt1">fckExt1.</param>
        /// <param name="fckExt2">fckExt2.</param>
        /// <param name="fckExt">fckExt.</param>
        /// <param name="crtBearingStrength">crtBearingStrength.</param>
        /// <param name="phiC">phiC.</param>
        /// <param name="psiSNIP">psiSNIP.</param>
        /// <param name="phiBSNIP">phiBSNIP.</param>
        /// <param name="gammaBSNIP">gammaBSNIP.</param>
        /// <param name="betaCCHN">betaCCHN.</param>
        /// <param name="betaLCHN">betaLCHN.</param>
        /// <param name="reinforcedConcretePad">reinforcedConcretePad.</param>
        /// <param name="omegaFactor">omegaFactor.</param>
        /// <param name="crtCompCheckIS">crtCompCheckIS.</param>
        /// <param name="gammaM0IS">gammaM0IS.</param>
        /// <param name="basePlateThickness">basePlateThickness.</param>
        /// <param name="basePlateFy">basePlateFy.</param>
        /// <param name="effAreaOffset">effAreaOffset.</param>
        /// <param name="concreteGrade">concreteGrade.</param>
        /// <param name="id">id.</param>
        /// <param name="name">name.</param>
        /// <param name="checkStatus">checkStatus.</param>
        /// <param name="limitCheckStatus">limitCheckStatus.</param>
        /// <param name="loadCaseId">loadCaseId.</param>
        /// <param name="loadCase">loadCase.</param>
        /// <param name="maxUnityCheck">maxUnityCheck.</param>
        /// <param name="form">form.</param>
        public ConcreteBlockCheckResDataIdeaStatiCaConnectionChecks(double fjd = default(double), double averageStress = default(double), double nsd = default(double), double aeff = default(double), string aeffCenterGravity = default(string), string centerTension = default(string), string centerCompression = default(string), double aeff2 = default(double), List<CIGeometry2DIRegion2DCIBasicTypes> supportingRegions = default(List<CIGeometry2DIRegion2DCIBasicTypes>), double aeffNet = default(double), double unityCheckStress = default(double), double kj = default(double), double addBearingWidth = default(double), Dictionary<string, List<List<List<CIGiCL2DPath2DSegmentCIGeometry2D>>>> effAreaOfBasePlates = default(Dictionary<string, List<List<List<CIGiCL2DPath2DSegmentCIGeometry2D>>>>), double gammaC = default(double), double fck = default(double), double fckFactored = default(double), double betaj = default(double), double alphaCC = default(double), double fc = default(double), double phiCrt = default(double), double omegaCrt = default(double), double fckExt1 = default(double), double fckExt2 = default(double), double fckExt = default(double), double crtBearingStrength = default(double), double phiC = default(double), double psiSNIP = default(double), double phiBSNIP = default(double), double gammaBSNIP = default(double), double betaCCHN = default(double), double betaLCHN = default(double), bool reinforcedConcretePad = default(bool), double omegaFactor = default(double), DataCrtCompCheckISCIBasicTypes? crtCompCheckIS = default(DataCrtCompCheckISCIBasicTypes?), double gammaM0IS = default(double), double basePlateThickness = default(double), double basePlateFy = default(double), double effAreaOffset = default(double), string concreteGrade = default(string), int id = default(int), string name = default(string), bool checkStatus = default(bool), bool limitCheckStatus = default(bool), int loadCaseId = default(int), string loadCase = default(string), double maxUnityCheck = default(double), string form = default(string))
        {
            this.Fjd = fjd;
            this.AverageStress = averageStress;
            this.Nsd = nsd;
            this.Aeff = aeff;
            this.AeffCenterGravity = aeffCenterGravity;
            this.CenterTension = centerTension;
            this.CenterCompression = centerCompression;
            this.Aeff2 = aeff2;
            this.SupportingRegions = supportingRegions;
            this.AeffNet = aeffNet;
            this.UnityCheckStress = unityCheckStress;
            this.Kj = kj;
            this.AddBearingWidth = addBearingWidth;
            this.EffAreaOfBasePlates = effAreaOfBasePlates;
            this.GammaC = gammaC;
            this.Fck = fck;
            this.FckFactored = fckFactored;
            this.Betaj = betaj;
            this.AlphaCC = alphaCC;
            this.Fc = fc;
            this.PhiCrt = phiCrt;
            this.OmegaCrt = omegaCrt;
            this.FckExt1 = fckExt1;
            this.FckExt2 = fckExt2;
            this.FckExt = fckExt;
            this.CrtBearingStrength = crtBearingStrength;
            this.PhiC = phiC;
            this.PsiSNIP = psiSNIP;
            this.PhiBSNIP = phiBSNIP;
            this.GammaBSNIP = gammaBSNIP;
            this.BetaCCHN = betaCCHN;
            this.BetaLCHN = betaLCHN;
            this.ReinforcedConcretePad = reinforcedConcretePad;
            this.OmegaFactor = omegaFactor;
            this.CrtCompCheckIS = crtCompCheckIS;
            this.GammaM0IS = gammaM0IS;
            this.BasePlateThickness = basePlateThickness;
            this.BasePlateFy = basePlateFy;
            this.EffAreaOffset = effAreaOffset;
            this.ConcreteGrade = concreteGrade;
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
        /// Gets or Sets Fjd
        /// </summary>
        [DataMember(Name = "fjd", EmitDefaultValue = false)]
        public double Fjd { get; set; }

        /// <summary>
        /// Gets or Sets AverageStress
        /// </summary>
        [DataMember(Name = "averageStress", EmitDefaultValue = false)]
        public double AverageStress { get; set; }

        /// <summary>
        /// Gets or Sets Nsd
        /// </summary>
        [DataMember(Name = "nsd", EmitDefaultValue = false)]
        public double Nsd { get; set; }

        /// <summary>
        /// Gets or Sets Aeff
        /// </summary>
        [DataMember(Name = "aeff", EmitDefaultValue = false)]
        public double Aeff { get; set; }

        /// <summary>
        /// Gets or Sets AeffCenterGravity
        /// </summary>
        [DataMember(Name = "aeffCenterGravity", EmitDefaultValue = false)]
        public string AeffCenterGravity { get; set; }

        /// <summary>
        /// Gets or Sets CenterTension
        /// </summary>
        [DataMember(Name = "centerTension", EmitDefaultValue = false)]
        public string CenterTension { get; set; }

        /// <summary>
        /// Gets or Sets CenterCompression
        /// </summary>
        [DataMember(Name = "centerCompression", EmitDefaultValue = false)]
        public string CenterCompression { get; set; }

        /// <summary>
        /// Gets or Sets Aeff2
        /// </summary>
        [DataMember(Name = "aeff2", EmitDefaultValue = false)]
        public double Aeff2 { get; set; }

        /// <summary>
        /// Gets or Sets SupportingRegions
        /// </summary>
        [DataMember(Name = "supportingRegions", EmitDefaultValue = true)]
        public List<CIGeometry2DIRegion2DCIBasicTypes> SupportingRegions { get; set; }

        /// <summary>
        /// Gets or Sets AeffNet
        /// </summary>
        [DataMember(Name = "aeffNet", EmitDefaultValue = false)]
        public double AeffNet { get; set; }

        /// <summary>
        /// Gets or Sets UnityCheckStress
        /// </summary>
        [DataMember(Name = "unityCheckStress", EmitDefaultValue = false)]
        public double UnityCheckStress { get; set; }

        /// <summary>
        /// Gets or Sets Kj
        /// </summary>
        [DataMember(Name = "kj", EmitDefaultValue = false)]
        public double Kj { get; set; }

        /// <summary>
        /// Gets or Sets AddBearingWidth
        /// </summary>
        [DataMember(Name = "addBearingWidth", EmitDefaultValue = false)]
        public double AddBearingWidth { get; set; }

        /// <summary>
        /// Gets or Sets EffAreaOfBasePlates
        /// </summary>
        [DataMember(Name = "effAreaOfBasePlates", EmitDefaultValue = true)]
        public Dictionary<string, List<List<List<CIGiCL2DPath2DSegmentCIGeometry2D>>>> EffAreaOfBasePlates { get; set; }

        /// <summary>
        /// Gets or Sets GammaC
        /// </summary>
        [DataMember(Name = "gammaC", EmitDefaultValue = false)]
        public double GammaC { get; set; }

        /// <summary>
        /// Gets or Sets Fck
        /// </summary>
        [DataMember(Name = "fck", EmitDefaultValue = false)]
        public double Fck { get; set; }

        /// <summary>
        /// Gets or Sets FckFactored
        /// </summary>
        [DataMember(Name = "fckFactored", EmitDefaultValue = false)]
        public double FckFactored { get; set; }

        /// <summary>
        /// Gets or Sets Betaj
        /// </summary>
        [DataMember(Name = "betaj", EmitDefaultValue = false)]
        public double Betaj { get; set; }

        /// <summary>
        /// Gets or Sets AlphaCC
        /// </summary>
        [DataMember(Name = "alphaCC", EmitDefaultValue = false)]
        public double AlphaCC { get; set; }

        /// <summary>
        /// Gets or Sets Fc
        /// </summary>
        [DataMember(Name = "fc", EmitDefaultValue = false)]
        public double Fc { get; set; }

        /// <summary>
        /// Gets or Sets PhiCrt
        /// </summary>
        [DataMember(Name = "phiCrt", EmitDefaultValue = false)]
        public double PhiCrt { get; set; }

        /// <summary>
        /// Gets or Sets OmegaCrt
        /// </summary>
        [DataMember(Name = "omegaCrt", EmitDefaultValue = false)]
        public double OmegaCrt { get; set; }

        /// <summary>
        /// Gets or Sets FckExt1
        /// </summary>
        [DataMember(Name = "fckExt1", EmitDefaultValue = false)]
        public double FckExt1 { get; set; }

        /// <summary>
        /// Gets or Sets FckExt2
        /// </summary>
        [DataMember(Name = "fckExt2", EmitDefaultValue = false)]
        public double FckExt2 { get; set; }

        /// <summary>
        /// Gets or Sets FckExt
        /// </summary>
        [DataMember(Name = "fckExt", EmitDefaultValue = false)]
        public double FckExt { get; set; }

        /// <summary>
        /// Gets or Sets CrtBearingStrength
        /// </summary>
        [DataMember(Name = "crtBearingStrength", EmitDefaultValue = false)]
        public double CrtBearingStrength { get; set; }

        /// <summary>
        /// Gets or Sets PhiC
        /// </summary>
        [DataMember(Name = "phiC", EmitDefaultValue = false)]
        public double PhiC { get; set; }

        /// <summary>
        /// Gets or Sets PsiSNIP
        /// </summary>
        [DataMember(Name = "psi_SNIP", EmitDefaultValue = false)]
        public double PsiSNIP { get; set; }

        /// <summary>
        /// Gets or Sets PhiBSNIP
        /// </summary>
        [DataMember(Name = "phiB_SNIP", EmitDefaultValue = false)]
        public double PhiBSNIP { get; set; }

        /// <summary>
        /// Gets or Sets GammaBSNIP
        /// </summary>
        [DataMember(Name = "gammaB_SNIP", EmitDefaultValue = false)]
        public double GammaBSNIP { get; set; }

        /// <summary>
        /// Gets or Sets BetaCCHN
        /// </summary>
        [DataMember(Name = "betaC_CHN", EmitDefaultValue = false)]
        public double BetaCCHN { get; set; }

        /// <summary>
        /// Gets or Sets BetaLCHN
        /// </summary>
        [DataMember(Name = "betaL_CHN", EmitDefaultValue = false)]
        public double BetaLCHN { get; set; }

        /// <summary>
        /// Gets or Sets ReinforcedConcretePad
        /// </summary>
        [DataMember(Name = "reinforcedConcretePad", EmitDefaultValue = true)]
        public bool ReinforcedConcretePad { get; set; }

        /// <summary>
        /// Gets or Sets OmegaFactor
        /// </summary>
        [DataMember(Name = "omegaFactor", EmitDefaultValue = false)]
        public double OmegaFactor { get; set; }

        /// <summary>
        /// Gets or Sets GammaM0IS
        /// </summary>
        [DataMember(Name = "gammaM0_IS", EmitDefaultValue = false)]
        public double GammaM0IS { get; set; }

        /// <summary>
        /// Gets or Sets BasePlateThickness
        /// </summary>
        [DataMember(Name = "basePlateThickness", EmitDefaultValue = false)]
        public double BasePlateThickness { get; set; }

        /// <summary>
        /// Gets or Sets BasePlateFy
        /// </summary>
        [DataMember(Name = "basePlateFy", EmitDefaultValue = false)]
        public double BasePlateFy { get; set; }

        /// <summary>
        /// Gets or Sets EffAreaOffset
        /// </summary>
        [DataMember(Name = "effAreaOffset", EmitDefaultValue = false)]
        public double EffAreaOffset { get; set; }

        /// <summary>
        /// Gets or Sets ConcreteGrade
        /// </summary>
        [DataMember(Name = "concreteGrade", EmitDefaultValue = true)]
        public string ConcreteGrade { get; set; }

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
            sb.Append("class ConcreteBlockCheckResDataIdeaStatiCaConnectionChecks {\n");
            sb.Append("  Fjd: ").Append(Fjd).Append("\n");
            sb.Append("  AverageStress: ").Append(AverageStress).Append("\n");
            sb.Append("  Nsd: ").Append(Nsd).Append("\n");
            sb.Append("  Aeff: ").Append(Aeff).Append("\n");
            sb.Append("  AeffCenterGravity: ").Append(AeffCenterGravity).Append("\n");
            sb.Append("  CenterTension: ").Append(CenterTension).Append("\n");
            sb.Append("  CenterCompression: ").Append(CenterCompression).Append("\n");
            sb.Append("  Aeff2: ").Append(Aeff2).Append("\n");
            sb.Append("  SupportingRegions: ").Append(SupportingRegions).Append("\n");
            sb.Append("  AeffNet: ").Append(AeffNet).Append("\n");
            sb.Append("  UnityCheckStress: ").Append(UnityCheckStress).Append("\n");
            sb.Append("  Kj: ").Append(Kj).Append("\n");
            sb.Append("  AddBearingWidth: ").Append(AddBearingWidth).Append("\n");
            sb.Append("  EffAreaOfBasePlates: ").Append(EffAreaOfBasePlates).Append("\n");
            sb.Append("  GammaC: ").Append(GammaC).Append("\n");
            sb.Append("  Fck: ").Append(Fck).Append("\n");
            sb.Append("  FckFactored: ").Append(FckFactored).Append("\n");
            sb.Append("  Betaj: ").Append(Betaj).Append("\n");
            sb.Append("  AlphaCC: ").Append(AlphaCC).Append("\n");
            sb.Append("  Fc: ").Append(Fc).Append("\n");
            sb.Append("  PhiCrt: ").Append(PhiCrt).Append("\n");
            sb.Append("  OmegaCrt: ").Append(OmegaCrt).Append("\n");
            sb.Append("  FckExt1: ").Append(FckExt1).Append("\n");
            sb.Append("  FckExt2: ").Append(FckExt2).Append("\n");
            sb.Append("  FckExt: ").Append(FckExt).Append("\n");
            sb.Append("  CrtBearingStrength: ").Append(CrtBearingStrength).Append("\n");
            sb.Append("  PhiC: ").Append(PhiC).Append("\n");
            sb.Append("  PsiSNIP: ").Append(PsiSNIP).Append("\n");
            sb.Append("  PhiBSNIP: ").Append(PhiBSNIP).Append("\n");
            sb.Append("  GammaBSNIP: ").Append(GammaBSNIP).Append("\n");
            sb.Append("  BetaCCHN: ").Append(BetaCCHN).Append("\n");
            sb.Append("  BetaLCHN: ").Append(BetaLCHN).Append("\n");
            sb.Append("  ReinforcedConcretePad: ").Append(ReinforcedConcretePad).Append("\n");
            sb.Append("  OmegaFactor: ").Append(OmegaFactor).Append("\n");
            sb.Append("  CrtCompCheckIS: ").Append(CrtCompCheckIS).Append("\n");
            sb.Append("  GammaM0IS: ").Append(GammaM0IS).Append("\n");
            sb.Append("  BasePlateThickness: ").Append(BasePlateThickness).Append("\n");
            sb.Append("  BasePlateFy: ").Append(BasePlateFy).Append("\n");
            sb.Append("  EffAreaOffset: ").Append(EffAreaOffset).Append("\n");
            sb.Append("  ConcreteGrade: ").Append(ConcreteGrade).Append("\n");
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
