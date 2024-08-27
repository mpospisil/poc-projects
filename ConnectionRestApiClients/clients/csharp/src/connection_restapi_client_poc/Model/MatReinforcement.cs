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
    /// Material reinforcement base class
    /// </summary>
    [DataContract(Name = "MatReinforcement")]
    public partial class MatReinforcement : IValidatableObject
    {

        /// <summary>
        /// Gets or Sets BarSurface
        /// </summary>
        [DataMember(Name = "barSurface", EmitDefaultValue = false)]
        public ReinfBarSurface? BarSurface { get; set; }

        /// <summary>
        /// Gets or Sets StateOfThermalExpansion
        /// </summary>
        [DataMember(Name = "stateOfThermalExpansion", EmitDefaultValue = false)]
        public ThermalExpansionState? StateOfThermalExpansion { get; set; }

        /// <summary>
        /// Gets or Sets StateOfThermalConductivity
        /// </summary>
        [DataMember(Name = "stateOfThermalConductivity", EmitDefaultValue = false)]
        public ThermalConductivityState? StateOfThermalConductivity { get; set; }

        /// <summary>
        /// Gets or Sets StateOfThermalSpecificHeat
        /// </summary>
        [DataMember(Name = "stateOfThermalSpecificHeat", EmitDefaultValue = false)]
        public ThermalSpecificHeatState? StateOfThermalSpecificHeat { get; set; }

        /// <summary>
        /// Gets or Sets StateOfThermalStressStrain
        /// </summary>
        [DataMember(Name = "stateOfThermalStressStrain", EmitDefaultValue = false)]
        public ThermalStressStrainState? StateOfThermalStressStrain { get; set; }

        /// <summary>
        /// Gets or Sets StateOfThermalStrain
        /// </summary>
        [DataMember(Name = "stateOfThermalStrain", EmitDefaultValue = false)]
        public ThermalStrainState? StateOfThermalStrain { get; set; }
        /// <summary>
        /// Initializes a new instance of the <see cref="MatReinforcement" /> class.
        /// </summary>
        /// <param name="barSurface">barSurface.</param>
        /// <param name="name">Name of material.</param>
        /// <param name="loadFromLibrary">Load from library - try override properties from library find material by name.</param>
        /// <param name="e">Young&#39;s modulus.</param>
        /// <param name="g">Shear modulus.</param>
        /// <param name="poisson">Poisson&#39;s ratio.</param>
        /// <param name="unitMass">Unit weight.</param>
        /// <param name="specificHeat">Specific heat capacity.</param>
        /// <param name="thermalExpansion">Thermal expansion.</param>
        /// <param name="thermalConductivity">Thermal conductivity.</param>
        /// <param name="isDefaultMaterial">True if material is default material from the code.</param>
        /// <param name="orderInCode">Order of this material in the code.</param>
        /// <param name="stateOfThermalExpansion">stateOfThermalExpansion.</param>
        /// <param name="stateOfThermalConductivity">stateOfThermalConductivity.</param>
        /// <param name="stateOfThermalSpecificHeat">stateOfThermalSpecificHeat.</param>
        /// <param name="stateOfThermalStressStrain">stateOfThermalStressStrain.</param>
        /// <param name="stateOfThermalStrain">stateOfThermalStrain.</param>
        /// <param name="userThermalSpecificHeatCurvature">userThermalSpecificHeatCurvature.</param>
        /// <param name="userThermalConductivityCurvature">userThermalConductivityCurvature.</param>
        /// <param name="userThermalExpansionCurvature">userThermalExpansionCurvature.</param>
        /// <param name="userThermalStrainCurvature">userThermalStrainCurvature.</param>
        /// <param name="userThermalStressStrainCurvature">User-defined curvature for thermal stress,strain { Temperature &#x3D; Θ[K], {x &#x3D; ε[-], y &#x3D; σ[Pa]}}.</param>
        /// <param name="id">Element Id.</param>
        public MatReinforcement(ReinfBarSurface? barSurface = default(ReinfBarSurface?), string name = default(string), bool loadFromLibrary = default(bool), double e = default(double), double g = default(double), double poisson = default(double), double unitMass = default(double), double specificHeat = default(double), double thermalExpansion = default(double), double thermalConductivity = default(double), bool isDefaultMaterial = default(bool), int orderInCode = default(int), ThermalExpansionState? stateOfThermalExpansion = default(ThermalExpansionState?), ThermalConductivityState? stateOfThermalConductivity = default(ThermalConductivityState?), ThermalSpecificHeatState? stateOfThermalSpecificHeat = default(ThermalSpecificHeatState?), ThermalStressStrainState? stateOfThermalStressStrain = default(ThermalStressStrainState?), ThermalStrainState? stateOfThermalStrain = default(ThermalStrainState?), Polygon2D userThermalSpecificHeatCurvature = default(Polygon2D), Polygon2D userThermalConductivityCurvature = default(Polygon2D), Polygon2D userThermalExpansionCurvature = default(Polygon2D), Polygon2D userThermalStrainCurvature = default(Polygon2D), List<TemperatureCurve2D> userThermalStressStrainCurvature = default(List<TemperatureCurve2D>), int id = default(int))
        {
            this.BarSurface = barSurface;
            this.Name = name;
            this.LoadFromLibrary = loadFromLibrary;
            this.E = e;
            this.G = g;
            this.Poisson = poisson;
            this.UnitMass = unitMass;
            this.SpecificHeat = specificHeat;
            this.ThermalExpansion = thermalExpansion;
            this.ThermalConductivity = thermalConductivity;
            this.IsDefaultMaterial = isDefaultMaterial;
            this.OrderInCode = orderInCode;
            this.StateOfThermalExpansion = stateOfThermalExpansion;
            this.StateOfThermalConductivity = stateOfThermalConductivity;
            this.StateOfThermalSpecificHeat = stateOfThermalSpecificHeat;
            this.StateOfThermalStressStrain = stateOfThermalStressStrain;
            this.StateOfThermalStrain = stateOfThermalStrain;
            this.UserThermalSpecificHeatCurvature = userThermalSpecificHeatCurvature;
            this.UserThermalConductivityCurvature = userThermalConductivityCurvature;
            this.UserThermalExpansionCurvature = userThermalExpansionCurvature;
            this.UserThermalStrainCurvature = userThermalStrainCurvature;
            this.UserThermalStressStrainCurvature = userThermalStressStrainCurvature;
            this.Id = id;
        }

        /// <summary>
        /// Name of material
        /// </summary>
        /// <value>Name of material</value>
        [DataMember(Name = "name", EmitDefaultValue = true)]
        public string Name { get; set; }

        /// <summary>
        /// Load from library - try override properties from library find material by name
        /// </summary>
        /// <value>Load from library - try override properties from library find material by name</value>
        [DataMember(Name = "loadFromLibrary", EmitDefaultValue = true)]
        public bool LoadFromLibrary { get; set; }

        /// <summary>
        /// Young&#39;s modulus
        /// </summary>
        /// <value>Young&#39;s modulus</value>
        [DataMember(Name = "e", EmitDefaultValue = false)]
        public double E { get; set; }

        /// <summary>
        /// Shear modulus
        /// </summary>
        /// <value>Shear modulus</value>
        [DataMember(Name = "g", EmitDefaultValue = false)]
        public double G { get; set; }

        /// <summary>
        /// Poisson&#39;s ratio
        /// </summary>
        /// <value>Poisson&#39;s ratio</value>
        [DataMember(Name = "poisson", EmitDefaultValue = false)]
        public double Poisson { get; set; }

        /// <summary>
        /// Unit weight
        /// </summary>
        /// <value>Unit weight</value>
        [DataMember(Name = "unitMass", EmitDefaultValue = false)]
        public double UnitMass { get; set; }

        /// <summary>
        /// Specific heat capacity
        /// </summary>
        /// <value>Specific heat capacity</value>
        [DataMember(Name = "specificHeat", EmitDefaultValue = false)]
        public double SpecificHeat { get; set; }

        /// <summary>
        /// Thermal expansion
        /// </summary>
        /// <value>Thermal expansion</value>
        [DataMember(Name = "thermalExpansion", EmitDefaultValue = false)]
        public double ThermalExpansion { get; set; }

        /// <summary>
        /// Thermal conductivity
        /// </summary>
        /// <value>Thermal conductivity</value>
        [DataMember(Name = "thermalConductivity", EmitDefaultValue = false)]
        public double ThermalConductivity { get; set; }

        /// <summary>
        /// True if material is default material from the code
        /// </summary>
        /// <value>True if material is default material from the code</value>
        [DataMember(Name = "isDefaultMaterial", EmitDefaultValue = true)]
        public bool IsDefaultMaterial { get; set; }

        /// <summary>
        /// Order of this material in the code
        /// </summary>
        /// <value>Order of this material in the code</value>
        [DataMember(Name = "orderInCode", EmitDefaultValue = false)]
        public int OrderInCode { get; set; }

        /// <summary>
        /// Gets or Sets UserThermalSpecificHeatCurvature
        /// </summary>
        [DataMember(Name = "userThermalSpecificHeatCurvature", EmitDefaultValue = false)]
        public Polygon2D UserThermalSpecificHeatCurvature { get; set; }

        /// <summary>
        /// Gets or Sets UserThermalConductivityCurvature
        /// </summary>
        [DataMember(Name = "userThermalConductivityCurvature", EmitDefaultValue = false)]
        public Polygon2D UserThermalConductivityCurvature { get; set; }

        /// <summary>
        /// Gets or Sets UserThermalExpansionCurvature
        /// </summary>
        [DataMember(Name = "userThermalExpansionCurvature", EmitDefaultValue = false)]
        public Polygon2D UserThermalExpansionCurvature { get; set; }

        /// <summary>
        /// Gets or Sets UserThermalStrainCurvature
        /// </summary>
        [DataMember(Name = "userThermalStrainCurvature", EmitDefaultValue = false)]
        public Polygon2D UserThermalStrainCurvature { get; set; }

        /// <summary>
        /// User-defined curvature for thermal stress,strain { Temperature &#x3D; Θ[K], {x &#x3D; ε[-], y &#x3D; σ[Pa]}}
        /// </summary>
        /// <value>User-defined curvature for thermal stress,strain { Temperature &#x3D; Θ[K], {x &#x3D; ε[-], y &#x3D; σ[Pa]}}</value>
        [DataMember(Name = "userThermalStressStrainCurvature", EmitDefaultValue = true)]
        public List<TemperatureCurve2D> UserThermalStressStrainCurvature { get; set; }

        /// <summary>
        /// Element Id
        /// </summary>
        /// <value>Element Id</value>
        [DataMember(Name = "id", EmitDefaultValue = false)]
        public int Id { get; set; }

        /// <summary>
        /// Returns the string presentation of the object
        /// </summary>
        /// <returns>String presentation of the object</returns>
        public override string ToString()
        {
            StringBuilder sb = new StringBuilder();
            sb.Append("class MatReinforcement {\n");
            sb.Append("  BarSurface: ").Append(BarSurface).Append("\n");
            sb.Append("  Name: ").Append(Name).Append("\n");
            sb.Append("  LoadFromLibrary: ").Append(LoadFromLibrary).Append("\n");
            sb.Append("  E: ").Append(E).Append("\n");
            sb.Append("  G: ").Append(G).Append("\n");
            sb.Append("  Poisson: ").Append(Poisson).Append("\n");
            sb.Append("  UnitMass: ").Append(UnitMass).Append("\n");
            sb.Append("  SpecificHeat: ").Append(SpecificHeat).Append("\n");
            sb.Append("  ThermalExpansion: ").Append(ThermalExpansion).Append("\n");
            sb.Append("  ThermalConductivity: ").Append(ThermalConductivity).Append("\n");
            sb.Append("  IsDefaultMaterial: ").Append(IsDefaultMaterial).Append("\n");
            sb.Append("  OrderInCode: ").Append(OrderInCode).Append("\n");
            sb.Append("  StateOfThermalExpansion: ").Append(StateOfThermalExpansion).Append("\n");
            sb.Append("  StateOfThermalConductivity: ").Append(StateOfThermalConductivity).Append("\n");
            sb.Append("  StateOfThermalSpecificHeat: ").Append(StateOfThermalSpecificHeat).Append("\n");
            sb.Append("  StateOfThermalStressStrain: ").Append(StateOfThermalStressStrain).Append("\n");
            sb.Append("  StateOfThermalStrain: ").Append(StateOfThermalStrain).Append("\n");
            sb.Append("  UserThermalSpecificHeatCurvature: ").Append(UserThermalSpecificHeatCurvature).Append("\n");
            sb.Append("  UserThermalConductivityCurvature: ").Append(UserThermalConductivityCurvature).Append("\n");
            sb.Append("  UserThermalExpansionCurvature: ").Append(UserThermalExpansionCurvature).Append("\n");
            sb.Append("  UserThermalStrainCurvature: ").Append(UserThermalStrainCurvature).Append("\n");
            sb.Append("  UserThermalStressStrainCurvature: ").Append(UserThermalStressStrainCurvature).Append("\n");
            sb.Append("  Id: ").Append(Id).Append("\n");
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
