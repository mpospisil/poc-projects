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
    /// CrossSectionReinforcedCrossSectionIdeaRSOpenModel
    /// </summary>
    [DataContract(Name = "CrossSection_ReinforcedCrossSection-IdeaRS_OpenModel")]
    public partial class CrossSectionReinforcedCrossSectionIdeaRSOpenModel : IValidatableObject
    {
        /// <summary>
        /// Initializes a new instance of the <see cref="CrossSectionReinforcedCrossSectionIdeaRSOpenModel" /> class.
        /// </summary>
        /// <param name="name">name.</param>
        /// <param name="crossSection">crossSection.</param>
        /// <param name="bars">bars.</param>
        /// <param name="stirrups">stirrups.</param>
        /// <param name="tendonBars">tendonBars.</param>
        /// <param name="tendonDucts">tendonDucts.</param>
        /// <param name="id">id.</param>
        public CrossSectionReinforcedCrossSectionIdeaRSOpenModel(string name = default(string), ReferenceElementIdeaRSOpenModel crossSection = default(ReferenceElementIdeaRSOpenModel), List<CrossSectionReinforcedBarIdeaRSOpenModel> bars = default(List<CrossSectionReinforcedBarIdeaRSOpenModel>), List<CrossSectionStirrupIdeaRSOpenModel> stirrups = default(List<CrossSectionStirrupIdeaRSOpenModel>), List<CrossSectionTendonBarIdeaRSOpenModel> tendonBars = default(List<CrossSectionTendonBarIdeaRSOpenModel>), List<CrossSectionTendonDuctIdeaRSOpenModel> tendonDucts = default(List<CrossSectionTendonDuctIdeaRSOpenModel>), int id = default(int))
        {
            this.Name = name;
            this.CrossSection = crossSection;
            this.Bars = bars;
            this.Stirrups = stirrups;
            this.TendonBars = tendonBars;
            this.TendonDucts = tendonDucts;
            this.Id = id;
        }

        /// <summary>
        /// Gets or Sets Name
        /// </summary>
        [DataMember(Name = "name", EmitDefaultValue = true)]
        public string Name { get; set; }

        /// <summary>
        /// Gets or Sets CrossSection
        /// </summary>
        [DataMember(Name = "crossSection", EmitDefaultValue = false)]
        public ReferenceElementIdeaRSOpenModel CrossSection { get; set; }

        /// <summary>
        /// Gets or Sets Bars
        /// </summary>
        [DataMember(Name = "bars", EmitDefaultValue = true)]
        public List<CrossSectionReinforcedBarIdeaRSOpenModel> Bars { get; set; }

        /// <summary>
        /// Gets or Sets Stirrups
        /// </summary>
        [DataMember(Name = "stirrups", EmitDefaultValue = true)]
        public List<CrossSectionStirrupIdeaRSOpenModel> Stirrups { get; set; }

        /// <summary>
        /// Gets or Sets TendonBars
        /// </summary>
        [DataMember(Name = "tendonBars", EmitDefaultValue = true)]
        public List<CrossSectionTendonBarIdeaRSOpenModel> TendonBars { get; set; }

        /// <summary>
        /// Gets or Sets TendonDucts
        /// </summary>
        [DataMember(Name = "tendonDucts", EmitDefaultValue = true)]
        public List<CrossSectionTendonDuctIdeaRSOpenModel> TendonDucts { get; set; }

        /// <summary>
        /// Gets or Sets Id
        /// </summary>
        [DataMember(Name = "id", EmitDefaultValue = false)]
        public int Id { get; set; }

        /// <summary>
        /// Returns the string presentation of the object
        /// </summary>
        /// <returns>String presentation of the object</returns>
        public override string ToString()
        {
            StringBuilder sb = new StringBuilder();
            sb.Append("class CrossSectionReinforcedCrossSectionIdeaRSOpenModel {\n");
            sb.Append("  Name: ").Append(Name).Append("\n");
            sb.Append("  CrossSection: ").Append(CrossSection).Append("\n");
            sb.Append("  Bars: ").Append(Bars).Append("\n");
            sb.Append("  Stirrups: ").Append(Stirrups).Append("\n");
            sb.Append("  TendonBars: ").Append(TendonBars).Append("\n");
            sb.Append("  TendonDucts: ").Append(TendonDucts).Append("\n");
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
