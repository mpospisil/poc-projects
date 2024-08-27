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
    /// Open model
    /// </summary>
    [DataContract(Name = "OpenModel")]
    public partial class OpenModel : IValidatableObject
    {
        /// <summary>
        /// Initializes a new instance of the <see cref="OpenModel" /> class.
        /// </summary>
        /// <param name="varVersion">Data format version.</param>
        /// <param name="originSettings">OriginProject.</param>
        /// <param name="point3D">List of Point3D.</param>
        /// <param name="lineSegment3D">List of LineSegment3D.</param>
        /// <param name="arcSegment3D">List of ArcSegment3D.</param>
        /// <param name="polyLine3D">List of PolyLine3D.</param>
        /// <param name="region3D">List of Region3D.</param>
        /// <param name="matConcrete">List of MatConcrete.</param>
        /// <param name="matReinforcement">List of MatReinforcement.</param>
        /// <param name="matSteel">List of MatSteel.</param>
        /// <param name="matPrestressSteel">List of MatPrestressSteel.</param>
        /// <param name="matWelding">List of MatWelding.</param>
        /// <param name="crossSection">List of CrossSection.</param>
        /// <param name="reinforcedCrossSection">List of Reinforced CrossSection.</param>
        /// <param name="hingeElement1D">List of hinge elements 1D.</param>
        /// <param name="opening">List of openings for Detail.</param>
        /// <param name="dappedEnd">List of dapped ends in Detail.</param>
        /// <param name="patchDevice">List of dapped ends in Detail.</param>
        /// <param name="element1D">List of Elements 1D.</param>
        /// <param name="beam">List of Elements 1D.</param>
        /// <param name="member1D">List of Member 1D.</param>
        /// <param name="element2D">List of Elements 2D.</param>
        /// <param name="wall">List of Elements 2D.</param>
        /// <param name="member2D">List of Member 2D.</param>
        /// <param name="rigidLink">List of Rigid link.</param>
        /// <param name="pointOnLine3D">List of Point on line 3D.</param>
        /// <param name="pointSupportNode">List of Point support in node.</param>
        /// <param name="lineSupportSegment">List of Line support on segment.</param>
        /// <param name="loadsInPoint">List of point load impulses in this load case.</param>
        /// <param name="loadsOnLine">List of line load impulses in this load case.</param>
        /// <param name="strainLoadsOnLine">List of generalized strain load impulses along the line in this load case..</param>
        /// <param name="pointLoadsOnLine">List of point load impulses in this load case.</param>
        /// <param name="loadsOnSurface">List surafce load in this load case.</param>
        /// <param name="settlements">Settlements in this load case.</param>
        /// <param name="temperatureLoadsOnLine">List of temperature load in this load case.</param>
        /// <param name="loadGroup">List of Load groups.</param>
        /// <param name="loadCase">List of Load cases.</param>
        /// <param name="combiInput">List of Combinations.</param>
        /// <param name="attribute">List of attributes.</param>
        /// <param name="connectionPoint">List of Connection Points.</param>
        /// <param name="connections">List of Connection data.</param>
        /// <param name="reinforcement">List of reinforcement in IDEA StatiCa Detail.</param>
        /// <param name="isdModel">List of Details.</param>
        /// <param name="initialImperfectionOfPoint">List of InitialmperfectionOfPoint.</param>
        /// <param name="tendon">Tendon.</param>
        /// <param name="resultClass">Result Class.</param>
        /// <param name="designMember">Design Member.</param>
        /// <param name="subStructure">Design Member.</param>
        /// <param name="connectionSetup">connectionSetup.</param>
        /// <param name="projectData">Defines certain data about user project..</param>
        /// <param name="checkMember">List of the Check members.</param>
        /// <param name="concreteCheckSection">List of the concrete check section.</param>
        /// <param name="concreteSetup">concreteSetup.</param>
        /// <param name="projectDataConcrete">Project data concrete.</param>
        /// <param name="rebarShape">Gets or sets the rebars shapes.</param>
        /// <param name="rebarGeneral">Gets or sets the rebar General collection.</param>
        /// <param name="rebarSingle">Gets or sets the rebar single collection.</param>
        /// <param name="rebarStirrups">Gets or sets the rebar group (stirrups) collection.</param>
        /// <param name="taper">taper.</param>
        /// <param name="span">span.</param>
        /// <param name="solidBlocks3D">List of Solid Blocks 3D.</param>
        /// <param name="surfaceSupports3D">List of Surface Supports 3D.</param>
        /// <param name="basePlates3D">List of Base Plates 3D.</param>
        /// <param name="anchors3D">List of Anchors 3D.</param>
        /// <param name="detailLoadCase">List of Load cases.</param>
        /// <param name="detailCombination">List of Combinations.</param>
        public OpenModel(int varVersion = default(int), Object originSettings = default(Object), List<Point3D> point3D = default(List<Point3D>), List<LineSegment3D> lineSegment3D = default(List<LineSegment3D>), List<ArcSegment3D> arcSegment3D = default(List<ArcSegment3D>), List<PolyLine3D> polyLine3D = default(List<PolyLine3D>), List<Region3D> region3D = default(List<Region3D>), List<MatConcrete> matConcrete = default(List<MatConcrete>), List<MatReinforcement> matReinforcement = default(List<MatReinforcement>), List<MatSteel> matSteel = default(List<MatSteel>), List<MatPrestressSteel> matPrestressSteel = default(List<MatPrestressSteel>), List<MatWelding> matWelding = default(List<MatWelding>), List<CrossSection> crossSection = default(List<CrossSection>), List<ReinforcedCrossSection> reinforcedCrossSection = default(List<ReinforcedCrossSection>), List<HingeElement1D> hingeElement1D = default(List<HingeElement1D>), List<Opening> opening = default(List<Opening>), List<DappedEnd> dappedEnd = default(List<DappedEnd>), List<PatchDevice> patchDevice = default(List<PatchDevice>), List<Element1D> element1D = default(List<Element1D>), List<Beam> beam = default(List<Beam>), List<Member1D> member1D = default(List<Member1D>), List<Element2D> element2D = default(List<Element2D>), List<Wall> wall = default(List<Wall>), List<Member2D> member2D = default(List<Member2D>), List<RigidLink> rigidLink = default(List<RigidLink>), List<PointOnLine3D> pointOnLine3D = default(List<PointOnLine3D>), List<PointSupportNode> pointSupportNode = default(List<PointSupportNode>), List<LineSupportSegment> lineSupportSegment = default(List<LineSupportSegment>), List<LoadInPoint> loadsInPoint = default(List<LoadInPoint>), List<LoadOnLine> loadsOnLine = default(List<LoadOnLine>), List<StrainLoadOnLine> strainLoadsOnLine = default(List<StrainLoadOnLine>), List<PointLoadOnLine> pointLoadsOnLine = default(List<PointLoadOnLine>), List<LoadOnSurface> loadsOnSurface = default(List<LoadOnSurface>), List<Settlement> settlements = default(List<Settlement>), List<TemperatureLoadOnLine> temperatureLoadsOnLine = default(List<TemperatureLoadOnLine>), List<LoadGroup> loadGroup = default(List<LoadGroup>), List<LoadCase> loadCase = default(List<LoadCase>), List<CombiInput> combiInput = default(List<CombiInput>), List<Object> attribute = default(List<Object>), List<ConnectionPoint> connectionPoint = default(List<ConnectionPoint>), List<ConnectionData> connections = default(List<ConnectionData>), List<Reinforcement> reinforcement = default(List<Reinforcement>), List<ISDModel> isdModel = default(List<ISDModel>), List<InitialImperfectionOfPoint> initialImperfectionOfPoint = default(List<InitialImperfectionOfPoint>), List<Tendon> tendon = default(List<Tendon>), List<ResultClass> resultClass = default(List<ResultClass>), List<DesignMember> designMember = default(List<DesignMember>), List<SubStructure> subStructure = default(List<SubStructure>), ConnectionSetup connectionSetup = default(ConnectionSetup), Object projectData = default(Object), List<CheckMember> checkMember = default(List<CheckMember>), List<CheckSection> concreteCheckSection = default(List<CheckSection>), ConcreteSetup concreteSetup = default(ConcreteSetup), Object projectDataConcrete = default(Object), List<RebarShape> rebarShape = default(List<RebarShape>), List<RebarGeneral> rebarGeneral = default(List<RebarGeneral>), List<RebarSingle> rebarSingle = default(List<RebarSingle>), List<RebarStirrups> rebarStirrups = default(List<RebarStirrups>), List<Taper> taper = default(List<Taper>), List<Span> span = default(List<Span>), List<SolidBlock3D> solidBlocks3D = default(List<SolidBlock3D>), List<SurfaceSupport3D> surfaceSupports3D = default(List<SurfaceSupport3D>), List<BasePlate3D> basePlates3D = default(List<BasePlate3D>), List<Anchor3D> anchors3D = default(List<Anchor3D>), List<DetailLoadCase> detailLoadCase = default(List<DetailLoadCase>), List<DetailCombination> detailCombination = default(List<DetailCombination>))
        {
            this.VarVersion = varVersion;
            this.OriginSettings = originSettings;
            this.Point3D = point3D;
            this.LineSegment3D = lineSegment3D;
            this.ArcSegment3D = arcSegment3D;
            this.PolyLine3D = polyLine3D;
            this.Region3D = region3D;
            this.MatConcrete = matConcrete;
            this.MatReinforcement = matReinforcement;
            this.MatSteel = matSteel;
            this.MatPrestressSteel = matPrestressSteel;
            this.MatWelding = matWelding;
            this.CrossSection = crossSection;
            this.ReinforcedCrossSection = reinforcedCrossSection;
            this.HingeElement1D = hingeElement1D;
            this.Opening = opening;
            this.DappedEnd = dappedEnd;
            this.PatchDevice = patchDevice;
            this.Element1D = element1D;
            this.Beam = beam;
            this.Member1D = member1D;
            this.Element2D = element2D;
            this.Wall = wall;
            this.Member2D = member2D;
            this.RigidLink = rigidLink;
            this.PointOnLine3D = pointOnLine3D;
            this.PointSupportNode = pointSupportNode;
            this.LineSupportSegment = lineSupportSegment;
            this.LoadsInPoint = loadsInPoint;
            this.LoadsOnLine = loadsOnLine;
            this.StrainLoadsOnLine = strainLoadsOnLine;
            this.PointLoadsOnLine = pointLoadsOnLine;
            this.LoadsOnSurface = loadsOnSurface;
            this.Settlements = settlements;
            this.TemperatureLoadsOnLine = temperatureLoadsOnLine;
            this.LoadGroup = loadGroup;
            this.LoadCase = loadCase;
            this.CombiInput = combiInput;
            this.Attribute = attribute;
            this.ConnectionPoint = connectionPoint;
            this.Connections = connections;
            this.Reinforcement = reinforcement;
            this.IsdModel = isdModel;
            this.InitialImperfectionOfPoint = initialImperfectionOfPoint;
            this.Tendon = tendon;
            this.ResultClass = resultClass;
            this.DesignMember = designMember;
            this.SubStructure = subStructure;
            this.ConnectionSetup = connectionSetup;
            this.ProjectData = projectData;
            this.CheckMember = checkMember;
            this.ConcreteCheckSection = concreteCheckSection;
            this.ConcreteSetup = concreteSetup;
            this.ProjectDataConcrete = projectDataConcrete;
            this.RebarShape = rebarShape;
            this.RebarGeneral = rebarGeneral;
            this.RebarSingle = rebarSingle;
            this.RebarStirrups = rebarStirrups;
            this.Taper = taper;
            this.Span = span;
            this.SolidBlocks3D = solidBlocks3D;
            this.SurfaceSupports3D = surfaceSupports3D;
            this.BasePlates3D = basePlates3D;
            this.Anchors3D = anchors3D;
            this.DetailLoadCase = detailLoadCase;
            this.DetailCombination = detailCombination;
        }

        /// <summary>
        /// Data format version
        /// </summary>
        /// <value>Data format version</value>
        [DataMember(Name = "version", EmitDefaultValue = false)]
        public int VarVersion { get; set; }

        /// <summary>
        /// OriginProject
        /// </summary>
        /// <value>OriginProject</value>
        [DataMember(Name = "originSettings", EmitDefaultValue = false)]
        public Object OriginSettings { get; set; }

        /// <summary>
        /// List of Point3D
        /// </summary>
        /// <value>List of Point3D</value>
        [DataMember(Name = "point3D", EmitDefaultValue = true)]
        public List<Point3D> Point3D { get; set; }

        /// <summary>
        /// List of LineSegment3D
        /// </summary>
        /// <value>List of LineSegment3D</value>
        [DataMember(Name = "lineSegment3D", EmitDefaultValue = true)]
        public List<LineSegment3D> LineSegment3D { get; set; }

        /// <summary>
        /// List of ArcSegment3D
        /// </summary>
        /// <value>List of ArcSegment3D</value>
        [DataMember(Name = "arcSegment3D", EmitDefaultValue = true)]
        public List<ArcSegment3D> ArcSegment3D { get; set; }

        /// <summary>
        /// List of PolyLine3D
        /// </summary>
        /// <value>List of PolyLine3D</value>
        [DataMember(Name = "polyLine3D", EmitDefaultValue = true)]
        public List<PolyLine3D> PolyLine3D { get; set; }

        /// <summary>
        /// List of Region3D
        /// </summary>
        /// <value>List of Region3D</value>
        [DataMember(Name = "region3D", EmitDefaultValue = true)]
        public List<Region3D> Region3D { get; set; }

        /// <summary>
        /// List of MatConcrete
        /// </summary>
        /// <value>List of MatConcrete</value>
        [DataMember(Name = "matConcrete", EmitDefaultValue = true)]
        public List<MatConcrete> MatConcrete { get; set; }

        /// <summary>
        /// List of MatReinforcement
        /// </summary>
        /// <value>List of MatReinforcement</value>
        [DataMember(Name = "matReinforcement", EmitDefaultValue = true)]
        public List<MatReinforcement> MatReinforcement { get; set; }

        /// <summary>
        /// List of MatSteel
        /// </summary>
        /// <value>List of MatSteel</value>
        [DataMember(Name = "matSteel", EmitDefaultValue = true)]
        public List<MatSteel> MatSteel { get; set; }

        /// <summary>
        /// List of MatPrestressSteel
        /// </summary>
        /// <value>List of MatPrestressSteel</value>
        [DataMember(Name = "matPrestressSteel", EmitDefaultValue = true)]
        public List<MatPrestressSteel> MatPrestressSteel { get; set; }

        /// <summary>
        /// List of MatWelding
        /// </summary>
        /// <value>List of MatWelding</value>
        [DataMember(Name = "matWelding", EmitDefaultValue = true)]
        public List<MatWelding> MatWelding { get; set; }

        /// <summary>
        /// List of CrossSection
        /// </summary>
        /// <value>List of CrossSection</value>
        [DataMember(Name = "crossSection", EmitDefaultValue = true)]
        public List<CrossSection> CrossSection { get; set; }

        /// <summary>
        /// List of Reinforced CrossSection
        /// </summary>
        /// <value>List of Reinforced CrossSection</value>
        [DataMember(Name = "reinforcedCrossSection", EmitDefaultValue = true)]
        public List<ReinforcedCrossSection> ReinforcedCrossSection { get; set; }

        /// <summary>
        /// List of hinge elements 1D
        /// </summary>
        /// <value>List of hinge elements 1D</value>
        [DataMember(Name = "hingeElement1D", EmitDefaultValue = true)]
        public List<HingeElement1D> HingeElement1D { get; set; }

        /// <summary>
        /// List of openings for Detail
        /// </summary>
        /// <value>List of openings for Detail</value>
        [DataMember(Name = "opening", EmitDefaultValue = true)]
        public List<Opening> Opening { get; set; }

        /// <summary>
        /// List of dapped ends in Detail
        /// </summary>
        /// <value>List of dapped ends in Detail</value>
        [DataMember(Name = "dappedEnd", EmitDefaultValue = true)]
        public List<DappedEnd> DappedEnd { get; set; }

        /// <summary>
        /// List of dapped ends in Detail
        /// </summary>
        /// <value>List of dapped ends in Detail</value>
        [DataMember(Name = "patchDevice", EmitDefaultValue = true)]
        public List<PatchDevice> PatchDevice { get; set; }

        /// <summary>
        /// List of Elements 1D
        /// </summary>
        /// <value>List of Elements 1D</value>
        [DataMember(Name = "element1D", EmitDefaultValue = true)]
        public List<Element1D> Element1D { get; set; }

        /// <summary>
        /// List of Elements 1D
        /// </summary>
        /// <value>List of Elements 1D</value>
        [DataMember(Name = "beam", EmitDefaultValue = true)]
        public List<Beam> Beam { get; set; }

        /// <summary>
        /// List of Member 1D
        /// </summary>
        /// <value>List of Member 1D</value>
        [DataMember(Name = "member1D", EmitDefaultValue = true)]
        public List<Member1D> Member1D { get; set; }

        /// <summary>
        /// List of Elements 2D
        /// </summary>
        /// <value>List of Elements 2D</value>
        [DataMember(Name = "element2D", EmitDefaultValue = true)]
        public List<Element2D> Element2D { get; set; }

        /// <summary>
        /// List of Elements 2D
        /// </summary>
        /// <value>List of Elements 2D</value>
        [DataMember(Name = "wall", EmitDefaultValue = true)]
        public List<Wall> Wall { get; set; }

        /// <summary>
        /// List of Member 2D
        /// </summary>
        /// <value>List of Member 2D</value>
        [DataMember(Name = "member2D", EmitDefaultValue = true)]
        public List<Member2D> Member2D { get; set; }

        /// <summary>
        /// List of Rigid link
        /// </summary>
        /// <value>List of Rigid link</value>
        [DataMember(Name = "rigidLink", EmitDefaultValue = true)]
        public List<RigidLink> RigidLink { get; set; }

        /// <summary>
        /// List of Point on line 3D
        /// </summary>
        /// <value>List of Point on line 3D</value>
        [DataMember(Name = "pointOnLine3D", EmitDefaultValue = true)]
        public List<PointOnLine3D> PointOnLine3D { get; set; }

        /// <summary>
        /// List of Point support in node
        /// </summary>
        /// <value>List of Point support in node</value>
        [DataMember(Name = "pointSupportNode", EmitDefaultValue = true)]
        public List<PointSupportNode> PointSupportNode { get; set; }

        /// <summary>
        /// List of Line support on segment
        /// </summary>
        /// <value>List of Line support on segment</value>
        [DataMember(Name = "lineSupportSegment", EmitDefaultValue = true)]
        public List<LineSupportSegment> LineSupportSegment { get; set; }

        /// <summary>
        /// List of point load impulses in this load case
        /// </summary>
        /// <value>List of point load impulses in this load case</value>
        [DataMember(Name = "loadsInPoint", EmitDefaultValue = true)]
        public List<LoadInPoint> LoadsInPoint { get; set; }

        /// <summary>
        /// List of line load impulses in this load case
        /// </summary>
        /// <value>List of line load impulses in this load case</value>
        [DataMember(Name = "loadsOnLine", EmitDefaultValue = true)]
        public List<LoadOnLine> LoadsOnLine { get; set; }

        /// <summary>
        /// List of generalized strain load impulses along the line in this load case.
        /// </summary>
        /// <value>List of generalized strain load impulses along the line in this load case.</value>
        [DataMember(Name = "strainLoadsOnLine", EmitDefaultValue = true)]
        public List<StrainLoadOnLine> StrainLoadsOnLine { get; set; }

        /// <summary>
        /// List of point load impulses in this load case
        /// </summary>
        /// <value>List of point load impulses in this load case</value>
        [DataMember(Name = "pointLoadsOnLine", EmitDefaultValue = true)]
        public List<PointLoadOnLine> PointLoadsOnLine { get; set; }

        /// <summary>
        /// List surafce load in this load case
        /// </summary>
        /// <value>List surafce load in this load case</value>
        [DataMember(Name = "loadsOnSurface", EmitDefaultValue = true)]
        public List<LoadOnSurface> LoadsOnSurface { get; set; }

        /// <summary>
        /// Settlements in this load case
        /// </summary>
        /// <value>Settlements in this load case</value>
        [DataMember(Name = "settlements", EmitDefaultValue = true)]
        public List<Settlement> Settlements { get; set; }

        /// <summary>
        /// List of temperature load in this load case
        /// </summary>
        /// <value>List of temperature load in this load case</value>
        [DataMember(Name = "temperatureLoadsOnLine", EmitDefaultValue = true)]
        public List<TemperatureLoadOnLine> TemperatureLoadsOnLine { get; set; }

        /// <summary>
        /// List of Load groups
        /// </summary>
        /// <value>List of Load groups</value>
        [DataMember(Name = "loadGroup", EmitDefaultValue = true)]
        public List<LoadGroup> LoadGroup { get; set; }

        /// <summary>
        /// List of Load cases
        /// </summary>
        /// <value>List of Load cases</value>
        [DataMember(Name = "loadCase", EmitDefaultValue = true)]
        public List<LoadCase> LoadCase { get; set; }

        /// <summary>
        /// List of Combinations
        /// </summary>
        /// <value>List of Combinations</value>
        [DataMember(Name = "combiInput", EmitDefaultValue = true)]
        public List<CombiInput> CombiInput { get; set; }

        /// <summary>
        /// List of attributes
        /// </summary>
        /// <value>List of attributes</value>
        [DataMember(Name = "attribute", EmitDefaultValue = true)]
        public List<Object> Attribute { get; set; }

        /// <summary>
        /// List of Connection Points
        /// </summary>
        /// <value>List of Connection Points</value>
        [DataMember(Name = "connectionPoint", EmitDefaultValue = true)]
        public List<ConnectionPoint> ConnectionPoint { get; set; }

        /// <summary>
        /// List of Connection data
        /// </summary>
        /// <value>List of Connection data</value>
        [DataMember(Name = "connections", EmitDefaultValue = true)]
        public List<ConnectionData> Connections { get; set; }

        /// <summary>
        /// List of reinforcement in IDEA StatiCa Detail
        /// </summary>
        /// <value>List of reinforcement in IDEA StatiCa Detail</value>
        [DataMember(Name = "reinforcement", EmitDefaultValue = true)]
        public List<Reinforcement> Reinforcement { get; set; }

        /// <summary>
        /// List of Details
        /// </summary>
        /// <value>List of Details</value>
        [DataMember(Name = "isdModel", EmitDefaultValue = true)]
        public List<ISDModel> IsdModel { get; set; }

        /// <summary>
        /// List of InitialmperfectionOfPoint
        /// </summary>
        /// <value>List of InitialmperfectionOfPoint</value>
        [DataMember(Name = "initialImperfectionOfPoint", EmitDefaultValue = true)]
        public List<InitialImperfectionOfPoint> InitialImperfectionOfPoint { get; set; }

        /// <summary>
        /// Tendon
        /// </summary>
        /// <value>Tendon</value>
        [DataMember(Name = "tendon", EmitDefaultValue = true)]
        public List<Tendon> Tendon { get; set; }

        /// <summary>
        /// Result Class
        /// </summary>
        /// <value>Result Class</value>
        [DataMember(Name = "resultClass", EmitDefaultValue = true)]
        public List<ResultClass> ResultClass { get; set; }

        /// <summary>
        /// Design Member
        /// </summary>
        /// <value>Design Member</value>
        [DataMember(Name = "designMember", EmitDefaultValue = true)]
        public List<DesignMember> DesignMember { get; set; }

        /// <summary>
        /// Design Member
        /// </summary>
        /// <value>Design Member</value>
        [DataMember(Name = "subStructure", EmitDefaultValue = true)]
        public List<SubStructure> SubStructure { get; set; }

        /// <summary>
        /// Gets or Sets ConnectionSetup
        /// </summary>
        [DataMember(Name = "connectionSetup", EmitDefaultValue = false)]
        public ConnectionSetup ConnectionSetup { get; set; }

        /// <summary>
        /// Defines certain data about user project.
        /// </summary>
        /// <value>Defines certain data about user project.</value>
        [DataMember(Name = "projectData", EmitDefaultValue = false)]
        public Object ProjectData { get; set; }

        /// <summary>
        /// List of the Check members
        /// </summary>
        /// <value>List of the Check members</value>
        [DataMember(Name = "checkMember", EmitDefaultValue = true)]
        public List<CheckMember> CheckMember { get; set; }

        /// <summary>
        /// List of the concrete check section
        /// </summary>
        /// <value>List of the concrete check section</value>
        [DataMember(Name = "concreteCheckSection", EmitDefaultValue = true)]
        public List<CheckSection> ConcreteCheckSection { get; set; }

        /// <summary>
        /// Gets or Sets ConcreteSetup
        /// </summary>
        [DataMember(Name = "concreteSetup", EmitDefaultValue = false)]
        public ConcreteSetup ConcreteSetup { get; set; }

        /// <summary>
        /// Project data concrete
        /// </summary>
        /// <value>Project data concrete</value>
        [DataMember(Name = "projectDataConcrete", EmitDefaultValue = false)]
        public Object ProjectDataConcrete { get; set; }

        /// <summary>
        /// Gets or sets the rebars shapes
        /// </summary>
        /// <value>Gets or sets the rebars shapes</value>
        [DataMember(Name = "rebarShape", EmitDefaultValue = true)]
        public List<RebarShape> RebarShape { get; set; }

        /// <summary>
        /// Gets or sets the rebar General collection
        /// </summary>
        /// <value>Gets or sets the rebar General collection</value>
        [DataMember(Name = "rebarGeneral", EmitDefaultValue = true)]
        public List<RebarGeneral> RebarGeneral { get; set; }

        /// <summary>
        /// Gets or sets the rebar single collection
        /// </summary>
        /// <value>Gets or sets the rebar single collection</value>
        [DataMember(Name = "rebarSingle", EmitDefaultValue = true)]
        public List<RebarSingle> RebarSingle { get; set; }

        /// <summary>
        /// Gets or sets the rebar group (stirrups) collection
        /// </summary>
        /// <value>Gets or sets the rebar group (stirrups) collection</value>
        [DataMember(Name = "rebarStirrups", EmitDefaultValue = true)]
        public List<RebarStirrups> RebarStirrups { get; set; }

        /// <summary>
        /// Gets or Sets Taper
        /// </summary>
        [DataMember(Name = "taper", EmitDefaultValue = true)]
        public List<Taper> Taper { get; set; }

        /// <summary>
        /// Gets or Sets Span
        /// </summary>
        [DataMember(Name = "span", EmitDefaultValue = true)]
        public List<Span> Span { get; set; }

        /// <summary>
        /// List of Solid Blocks 3D
        /// </summary>
        /// <value>List of Solid Blocks 3D</value>
        [DataMember(Name = "solidBlocks3D", EmitDefaultValue = true)]
        public List<SolidBlock3D> SolidBlocks3D { get; set; }

        /// <summary>
        /// List of Surface Supports 3D
        /// </summary>
        /// <value>List of Surface Supports 3D</value>
        [DataMember(Name = "surfaceSupports3D", EmitDefaultValue = true)]
        public List<SurfaceSupport3D> SurfaceSupports3D { get; set; }

        /// <summary>
        /// List of Base Plates 3D
        /// </summary>
        /// <value>List of Base Plates 3D</value>
        [DataMember(Name = "basePlates3D", EmitDefaultValue = true)]
        public List<BasePlate3D> BasePlates3D { get; set; }

        /// <summary>
        /// List of Anchors 3D
        /// </summary>
        /// <value>List of Anchors 3D</value>
        [DataMember(Name = "anchors3D", EmitDefaultValue = true)]
        public List<Anchor3D> Anchors3D { get; set; }

        /// <summary>
        /// List of Load cases
        /// </summary>
        /// <value>List of Load cases</value>
        [DataMember(Name = "detailLoadCase", EmitDefaultValue = true)]
        public List<DetailLoadCase> DetailLoadCase { get; set; }

        /// <summary>
        /// List of Combinations
        /// </summary>
        /// <value>List of Combinations</value>
        [DataMember(Name = "detailCombination", EmitDefaultValue = true)]
        public List<DetailCombination> DetailCombination { get; set; }

        /// <summary>
        /// Returns the string presentation of the object
        /// </summary>
        /// <returns>String presentation of the object</returns>
        public override string ToString()
        {
            StringBuilder sb = new StringBuilder();
            sb.Append("class OpenModel {\n");
            sb.Append("  VarVersion: ").Append(VarVersion).Append("\n");
            sb.Append("  OriginSettings: ").Append(OriginSettings).Append("\n");
            sb.Append("  Point3D: ").Append(Point3D).Append("\n");
            sb.Append("  LineSegment3D: ").Append(LineSegment3D).Append("\n");
            sb.Append("  ArcSegment3D: ").Append(ArcSegment3D).Append("\n");
            sb.Append("  PolyLine3D: ").Append(PolyLine3D).Append("\n");
            sb.Append("  Region3D: ").Append(Region3D).Append("\n");
            sb.Append("  MatConcrete: ").Append(MatConcrete).Append("\n");
            sb.Append("  MatReinforcement: ").Append(MatReinforcement).Append("\n");
            sb.Append("  MatSteel: ").Append(MatSteel).Append("\n");
            sb.Append("  MatPrestressSteel: ").Append(MatPrestressSteel).Append("\n");
            sb.Append("  MatWelding: ").Append(MatWelding).Append("\n");
            sb.Append("  CrossSection: ").Append(CrossSection).Append("\n");
            sb.Append("  ReinforcedCrossSection: ").Append(ReinforcedCrossSection).Append("\n");
            sb.Append("  HingeElement1D: ").Append(HingeElement1D).Append("\n");
            sb.Append("  Opening: ").Append(Opening).Append("\n");
            sb.Append("  DappedEnd: ").Append(DappedEnd).Append("\n");
            sb.Append("  PatchDevice: ").Append(PatchDevice).Append("\n");
            sb.Append("  Element1D: ").Append(Element1D).Append("\n");
            sb.Append("  Beam: ").Append(Beam).Append("\n");
            sb.Append("  Member1D: ").Append(Member1D).Append("\n");
            sb.Append("  Element2D: ").Append(Element2D).Append("\n");
            sb.Append("  Wall: ").Append(Wall).Append("\n");
            sb.Append("  Member2D: ").Append(Member2D).Append("\n");
            sb.Append("  RigidLink: ").Append(RigidLink).Append("\n");
            sb.Append("  PointOnLine3D: ").Append(PointOnLine3D).Append("\n");
            sb.Append("  PointSupportNode: ").Append(PointSupportNode).Append("\n");
            sb.Append("  LineSupportSegment: ").Append(LineSupportSegment).Append("\n");
            sb.Append("  LoadsInPoint: ").Append(LoadsInPoint).Append("\n");
            sb.Append("  LoadsOnLine: ").Append(LoadsOnLine).Append("\n");
            sb.Append("  StrainLoadsOnLine: ").Append(StrainLoadsOnLine).Append("\n");
            sb.Append("  PointLoadsOnLine: ").Append(PointLoadsOnLine).Append("\n");
            sb.Append("  LoadsOnSurface: ").Append(LoadsOnSurface).Append("\n");
            sb.Append("  Settlements: ").Append(Settlements).Append("\n");
            sb.Append("  TemperatureLoadsOnLine: ").Append(TemperatureLoadsOnLine).Append("\n");
            sb.Append("  LoadGroup: ").Append(LoadGroup).Append("\n");
            sb.Append("  LoadCase: ").Append(LoadCase).Append("\n");
            sb.Append("  CombiInput: ").Append(CombiInput).Append("\n");
            sb.Append("  Attribute: ").Append(Attribute).Append("\n");
            sb.Append("  ConnectionPoint: ").Append(ConnectionPoint).Append("\n");
            sb.Append("  Connections: ").Append(Connections).Append("\n");
            sb.Append("  Reinforcement: ").Append(Reinforcement).Append("\n");
            sb.Append("  IsdModel: ").Append(IsdModel).Append("\n");
            sb.Append("  InitialImperfectionOfPoint: ").Append(InitialImperfectionOfPoint).Append("\n");
            sb.Append("  Tendon: ").Append(Tendon).Append("\n");
            sb.Append("  ResultClass: ").Append(ResultClass).Append("\n");
            sb.Append("  DesignMember: ").Append(DesignMember).Append("\n");
            sb.Append("  SubStructure: ").Append(SubStructure).Append("\n");
            sb.Append("  ConnectionSetup: ").Append(ConnectionSetup).Append("\n");
            sb.Append("  ProjectData: ").Append(ProjectData).Append("\n");
            sb.Append("  CheckMember: ").Append(CheckMember).Append("\n");
            sb.Append("  ConcreteCheckSection: ").Append(ConcreteCheckSection).Append("\n");
            sb.Append("  ConcreteSetup: ").Append(ConcreteSetup).Append("\n");
            sb.Append("  ProjectDataConcrete: ").Append(ProjectDataConcrete).Append("\n");
            sb.Append("  RebarShape: ").Append(RebarShape).Append("\n");
            sb.Append("  RebarGeneral: ").Append(RebarGeneral).Append("\n");
            sb.Append("  RebarSingle: ").Append(RebarSingle).Append("\n");
            sb.Append("  RebarStirrups: ").Append(RebarStirrups).Append("\n");
            sb.Append("  Taper: ").Append(Taper).Append("\n");
            sb.Append("  Span: ").Append(Span).Append("\n");
            sb.Append("  SolidBlocks3D: ").Append(SolidBlocks3D).Append("\n");
            sb.Append("  SurfaceSupports3D: ").Append(SurfaceSupports3D).Append("\n");
            sb.Append("  BasePlates3D: ").Append(BasePlates3D).Append("\n");
            sb.Append("  Anchors3D: ").Append(Anchors3D).Append("\n");
            sb.Append("  DetailLoadCase: ").Append(DetailLoadCase).Append("\n");
            sb.Append("  DetailCombination: ").Append(DetailCombination).Append("\n");
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
