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
    /// ProjectCheckResDataIdeaStatiCaConnectionChecks
    /// </summary>
    [DataContract(Name = "ProjectCheckResData-IdeaStatiCa_ConnectionChecks")]
    public partial class ProjectCheckResDataIdeaStatiCaConnectionChecks : IValidatableObject
    {
        /// <summary>
        /// Initializes a new instance of the <see cref="ProjectCheckResDataIdeaStatiCaConnectionChecks" /> class.
        /// </summary>
        /// <param name="item">item.</param>
        /// <param name="itemInfo">itemInfo.</param>
        /// <param name="id">id.</param>
        /// <param name="name">name.</param>
        /// <param name="checkStatus">checkStatus.</param>
        /// <param name="limitCheckStatus">limitCheckStatus.</param>
        /// <param name="loadCaseId">loadCaseId.</param>
        /// <param name="loadCase">loadCase.</param>
        /// <param name="maxUnityCheck">maxUnityCheck.</param>
        /// <param name="form">form.</param>
        public ProjectCheckResDataIdeaStatiCaConnectionChecks(string item = default(string), string itemInfo = default(string), int id = default(int), string name = default(string), bool checkStatus = default(bool), bool limitCheckStatus = default(bool), int loadCaseId = default(int), string loadCase = default(string), double maxUnityCheck = default(double), string form = default(string))
        {
            this.Item = item;
            this.ItemInfo = itemInfo;
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
        /// Gets or Sets Item
        /// </summary>
        [DataMember(Name = "item", EmitDefaultValue = true)]
        public string Item { get; set; }

        /// <summary>
        /// Gets or Sets ItemInfo
        /// </summary>
        [DataMember(Name = "itemInfo", EmitDefaultValue = true)]
        public string ItemInfo { get; set; }

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
            sb.Append("class ProjectCheckResDataIdeaStatiCaConnectionChecks {\n");
            sb.Append("  Item: ").Append(Item).Append("\n");
            sb.Append("  ItemInfo: ").Append(ItemInfo).Append("\n");
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
