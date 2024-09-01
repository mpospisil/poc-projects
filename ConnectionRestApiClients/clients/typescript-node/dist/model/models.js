"use strict";
var __createBinding = (this && this.__createBinding) || (Object.create ? (function(o, m, k, k2) {
    if (k2 === undefined) k2 = k;
    var desc = Object.getOwnPropertyDescriptor(m, k);
    if (!desc || ("get" in desc ? !m.__esModule : desc.writable || desc.configurable)) {
      desc = { enumerable: true, get: function() { return m[k]; } };
    }
    Object.defineProperty(o, k2, desc);
}) : (function(o, m, k, k2) {
    if (k2 === undefined) k2 = k;
    o[k2] = m[k];
}));
var __exportStar = (this && this.__exportStar) || function(m, exports) {
    for (var p in m) if (p !== "default" && !Object.prototype.hasOwnProperty.call(exports, p)) __createBinding(exports, m, p);
};
Object.defineProperty(exports, "__esModule", { value: true });
exports.VoidAuth = exports.OAuth = exports.ApiKeyAuth = exports.HttpBearerAuth = exports.HttpBasicAuth = exports.ObjectSerializer = void 0;
__exportStar(require("./anchor3D"), exports);
__exportStar(require("./anchorGrid"), exports);
__exportStar(require("./anchorType"), exports);
__exportStar(require("./arcSegment3D"), exports);
__exportStar(require("./basePlate3D"), exports);
__exportStar(require("./baseTemplateConversion"), exports);
__exportStar(require("./beam"), exports);
__exportStar(require("./beamData"), exports);
__exportStar(require("./bendData"), exports);
__exportStar(require("./boltGrid"), exports);
__exportStar(require("./boltShearType"), exports);
__exportStar(require("./bucklingRes"), exports);
__exportStar(require("./checkMember"), exports);
__exportStar(require("./checkResAnchor"), exports);
__exportStar(require("./checkResBolt"), exports);
__exportStar(require("./checkResConcreteBlock"), exports);
__exportStar(require("./checkResPlate"), exports);
__exportStar(require("./checkResSummary"), exports);
__exportStar(require("./checkResWeld"), exports);
__exportStar(require("./checkSection"), exports);
__exportStar(require("./combiInput"), exports);
__exportStar(require("./conAnalysisTypeEnum"), exports);
__exportStar(require("./conCalculationParameter"), exports);
__exportStar(require("./conConnection"), exports);
__exportStar(require("./conLoadEffect"), exports);
__exportStar(require("./conLoadEffectMemberLoad"), exports);
__exportStar(require("./conLoadEffectPositionEnum"), exports);
__exportStar(require("./conLoadEffectSectionLoad"), exports);
__exportStar(require("./conLoadingOptions"), exports);
__exportStar(require("./conMember"), exports);
__exportStar(require("./conMissingWeld"), exports);
__exportStar(require("./conMprlCrossSection"), exports);
__exportStar(require("./conMprlElement"), exports);
__exportStar(require("./conOperation"), exports);
__exportStar(require("./conProductionCost"), exports);
__exportStar(require("./conProject"), exports);
__exportStar(require("./conProjectData"), exports);
__exportStar(require("./conResultSummary"), exports);
__exportStar(require("./conTemplateApplyParam"), exports);
__exportStar(require("./conTemplateMappingGetParam"), exports);
__exportStar(require("./concreteBlock"), exports);
__exportStar(require("./concreteBlockData"), exports);
__exportStar(require("./concreteSetup"), exports);
__exportStar(require("./coneBreakoutCheckType"), exports);
__exportStar(require("./connectionCheckRes"), exports);
__exportStar(require("./connectionData"), exports);
__exportStar(require("./connectionPoint"), exports);
__exportStar(require("./connectionSetup"), exports);
__exportStar(require("./crossSection"), exports);
__exportStar(require("./crtCompCheckIS"), exports);
__exportStar(require("./cutBeamByBeamData"), exports);
__exportStar(require("./cutData"), exports);
__exportStar(require("./cutMethod"), exports);
__exportStar(require("./cutOrientation"), exports);
__exportStar(require("./cutPart"), exports);
__exportStar(require("./dappedEnd"), exports);
__exportStar(require("./designMember"), exports);
__exportStar(require("./detailCombination"), exports);
__exportStar(require("./detailLoadCase"), exports);
__exportStar(require("./distanceComparison"), exports);
__exportStar(require("./drawData"), exports);
__exportStar(require("./ePurpose"), exports);
__exportStar(require("./element1D"), exports);
__exportStar(require("./element2D"), exports);
__exportStar(require("./fatigueTypeOfPrestressingSteel"), exports);
__exportStar(require("./foldedPlateData"), exports);
__exportStar(require("./hingeElement1D"), exports);
__exportStar(require("./iGroup"), exports);
__exportStar(require("./iSDModel"), exports);
__exportStar(require("./ideaParameter"), exports);
__exportStar(require("./ideaParameterUpdate"), exports);
__exportStar(require("./initialImperfectionOfPoint"), exports);
__exportStar(require("./line"), exports);
__exportStar(require("./lineSegment3D"), exports);
__exportStar(require("./lineSupportSegment"), exports);
__exportStar(require("./loadCase"), exports);
__exportStar(require("./loadEffectData"), exports);
__exportStar(require("./loadGroup"), exports);
__exportStar(require("./loadInPoint"), exports);
__exportStar(require("./loadOnLine"), exports);
__exportStar(require("./loadOnSurface"), exports);
__exportStar(require("./loading"), exports);
__exportStar(require("./loadingType"), exports);
__exportStar(require("./matConcrete"), exports);
__exportStar(require("./matPrestressSteel"), exports);
__exportStar(require("./matReinforcement"), exports);
__exportStar(require("./matSteel"), exports);
__exportStar(require("./matWelding"), exports);
__exportStar(require("./materialDuct"), exports);
__exportStar(require("./member"), exports);
__exportStar(require("./member1D"), exports);
__exportStar(require("./member2D"), exports);
__exportStar(require("./memberType"), exports);
__exportStar(require("./memoryStream"), exports);
__exportStar(require("./messageNumber"), exports);
__exportStar(require("./okObjectResult"), exports);
__exportStar(require("./openElementId"), exports);
__exportStar(require("./openMessage"), exports);
__exportStar(require("./openMessages"), exports);
__exportStar(require("./openModel"), exports);
__exportStar(require("./openModelContainer"), exports);
__exportStar(require("./openModelResult"), exports);
__exportStar(require("./opening"), exports);
__exportStar(require("./parameterData"), exports);
__exportStar(require("./patchDevice"), exports);
__exportStar(require("./plateData"), exports);
__exportStar(require("./point2D"), exports);
__exportStar(require("./point3D"), exports);
__exportStar(require("./pointLoadOnLine"), exports);
__exportStar(require("./pointOnLine3D"), exports);
__exportStar(require("./pointSupportNode"), exports);
__exportStar(require("./polyLine2D"), exports);
__exportStar(require("./polyLine3D"), exports);
__exportStar(require("./polygon2D"), exports);
__exportStar(require("./rebarGeneral"), exports);
__exportStar(require("./rebarShape"), exports);
__exportStar(require("./rebarSingle"), exports);
__exportStar(require("./rebarStirrups"), exports);
__exportStar(require("./referenceElement"), exports);
__exportStar(require("./region2D"), exports);
__exportStar(require("./region3D"), exports);
__exportStar(require("./reinfBarSurface"), exports);
__exportStar(require("./reinforcedBar"), exports);
__exportStar(require("./reinforcedCrossSection"), exports);
__exportStar(require("./reinforcement"), exports);
__exportStar(require("./resultClass"), exports);
__exportStar(require("./resultLocalSystemType"), exports);
__exportStar(require("./resultOnMember"), exports);
__exportStar(require("./resultOnMembers"), exports);
__exportStar(require("./resultType"), exports);
__exportStar(require("./rigidLink"), exports);
__exportStar(require("./segment2D"), exports);
__exportStar(require("./selected"), exports);
__exportStar(require("./selectedType"), exports);
__exportStar(require("./settlement"), exports);
__exportStar(require("./solidBlock3D"), exports);
__exportStar(require("./span"), exports);
__exportStar(require("./stirrup"), exports);
__exportStar(require("./strainLoadOnLine"), exports);
__exportStar(require("./subStructure"), exports);
__exportStar(require("./surfaceSupport3D"), exports);
__exportStar(require("./taper"), exports);
__exportStar(require("./temperatureCurve2D"), exports);
__exportStar(require("./temperatureLoadOnLine"), exports);
__exportStar(require("./templateConversions"), exports);
__exportStar(require("./tendon"), exports);
__exportStar(require("./tendonBar"), exports);
__exportStar(require("./tendonBarType"), exports);
__exportStar(require("./tendonDuct"), exports);
__exportStar(require("./text"), exports);
__exportStar(require("./textPosition"), exports);
__exportStar(require("./thermalConductivityState"), exports);
__exportStar(require("./thermalExpansionState"), exports);
__exportStar(require("./thermalSpecificHeatState"), exports);
__exportStar(require("./thermalStrainState"), exports);
__exportStar(require("./thermalStressStrainState"), exports);
__exportStar(require("./uploadIdeaConRequest"), exports);
__exportStar(require("./validationType"), exports);
__exportStar(require("./vector3D"), exports);
__exportStar(require("./wall"), exports);
__exportStar(require("./weldData"), exports);
__exportStar(require("./weldEvaluation"), exports);
__exportStar(require("./weldType"), exports);
const anchor3D_1 = require("./anchor3D");
const anchorGrid_1 = require("./anchorGrid");
const anchorType_1 = require("./anchorType");
const arcSegment3D_1 = require("./arcSegment3D");
const basePlate3D_1 = require("./basePlate3D");
const baseTemplateConversion_1 = require("./baseTemplateConversion");
const beam_1 = require("./beam");
const beamData_1 = require("./beamData");
const bendData_1 = require("./bendData");
const boltGrid_1 = require("./boltGrid");
const boltShearType_1 = require("./boltShearType");
const bucklingRes_1 = require("./bucklingRes");
const checkMember_1 = require("./checkMember");
const checkResAnchor_1 = require("./checkResAnchor");
const checkResBolt_1 = require("./checkResBolt");
const checkResConcreteBlock_1 = require("./checkResConcreteBlock");
const checkResPlate_1 = require("./checkResPlate");
const checkResSummary_1 = require("./checkResSummary");
const checkResWeld_1 = require("./checkResWeld");
const checkSection_1 = require("./checkSection");
const combiInput_1 = require("./combiInput");
const conAnalysisTypeEnum_1 = require("./conAnalysisTypeEnum");
const conCalculationParameter_1 = require("./conCalculationParameter");
const conConnection_1 = require("./conConnection");
const conLoadEffect_1 = require("./conLoadEffect");
const conLoadEffectMemberLoad_1 = require("./conLoadEffectMemberLoad");
const conLoadEffectPositionEnum_1 = require("./conLoadEffectPositionEnum");
const conLoadEffectSectionLoad_1 = require("./conLoadEffectSectionLoad");
const conLoadingOptions_1 = require("./conLoadingOptions");
const conMember_1 = require("./conMember");
const conMissingWeld_1 = require("./conMissingWeld");
const conMprlCrossSection_1 = require("./conMprlCrossSection");
const conMprlElement_1 = require("./conMprlElement");
const conOperation_1 = require("./conOperation");
const conProductionCost_1 = require("./conProductionCost");
const conProject_1 = require("./conProject");
const conProjectData_1 = require("./conProjectData");
const conResultSummary_1 = require("./conResultSummary");
const conTemplateApplyParam_1 = require("./conTemplateApplyParam");
const conTemplateMappingGetParam_1 = require("./conTemplateMappingGetParam");
const concreteBlock_1 = require("./concreteBlock");
const concreteBlockData_1 = require("./concreteBlockData");
const concreteSetup_1 = require("./concreteSetup");
const coneBreakoutCheckType_1 = require("./coneBreakoutCheckType");
const connectionCheckRes_1 = require("./connectionCheckRes");
const connectionData_1 = require("./connectionData");
const connectionPoint_1 = require("./connectionPoint");
const connectionSetup_1 = require("./connectionSetup");
const crossSection_1 = require("./crossSection");
const crtCompCheckIS_1 = require("./crtCompCheckIS");
const cutBeamByBeamData_1 = require("./cutBeamByBeamData");
const cutData_1 = require("./cutData");
const cutMethod_1 = require("./cutMethod");
const cutOrientation_1 = require("./cutOrientation");
const cutPart_1 = require("./cutPart");
const dappedEnd_1 = require("./dappedEnd");
const designMember_1 = require("./designMember");
const detailCombination_1 = require("./detailCombination");
const detailLoadCase_1 = require("./detailLoadCase");
const distanceComparison_1 = require("./distanceComparison");
const drawData_1 = require("./drawData");
const ePurpose_1 = require("./ePurpose");
const element1D_1 = require("./element1D");
const element2D_1 = require("./element2D");
const fatigueTypeOfPrestressingSteel_1 = require("./fatigueTypeOfPrestressingSteel");
const foldedPlateData_1 = require("./foldedPlateData");
const hingeElement1D_1 = require("./hingeElement1D");
const iGroup_1 = require("./iGroup");
const iSDModel_1 = require("./iSDModel");
const ideaParameter_1 = require("./ideaParameter");
const ideaParameterUpdate_1 = require("./ideaParameterUpdate");
const initialImperfectionOfPoint_1 = require("./initialImperfectionOfPoint");
const line_1 = require("./line");
const lineSegment3D_1 = require("./lineSegment3D");
const lineSupportSegment_1 = require("./lineSupportSegment");
const loadCase_1 = require("./loadCase");
const loadEffectData_1 = require("./loadEffectData");
const loadGroup_1 = require("./loadGroup");
const loadInPoint_1 = require("./loadInPoint");
const loadOnLine_1 = require("./loadOnLine");
const loadOnSurface_1 = require("./loadOnSurface");
const loading_1 = require("./loading");
const loadingType_1 = require("./loadingType");
const matConcrete_1 = require("./matConcrete");
const matPrestressSteel_1 = require("./matPrestressSteel");
const matReinforcement_1 = require("./matReinforcement");
const matSteel_1 = require("./matSteel");
const matWelding_1 = require("./matWelding");
const materialDuct_1 = require("./materialDuct");
const member_1 = require("./member");
const member1D_1 = require("./member1D");
const member2D_1 = require("./member2D");
const memberType_1 = require("./memberType");
const memoryStream_1 = require("./memoryStream");
const messageNumber_1 = require("./messageNumber");
const okObjectResult_1 = require("./okObjectResult");
const openElementId_1 = require("./openElementId");
const openMessage_1 = require("./openMessage");
const openMessages_1 = require("./openMessages");
const openModel_1 = require("./openModel");
const openModelContainer_1 = require("./openModelContainer");
const openModelResult_1 = require("./openModelResult");
const opening_1 = require("./opening");
const parameterData_1 = require("./parameterData");
const patchDevice_1 = require("./patchDevice");
const plateData_1 = require("./plateData");
const point2D_1 = require("./point2D");
const point3D_1 = require("./point3D");
const pointLoadOnLine_1 = require("./pointLoadOnLine");
const pointOnLine3D_1 = require("./pointOnLine3D");
const pointSupportNode_1 = require("./pointSupportNode");
const polyLine2D_1 = require("./polyLine2D");
const polyLine3D_1 = require("./polyLine3D");
const polygon2D_1 = require("./polygon2D");
const rebarGeneral_1 = require("./rebarGeneral");
const rebarShape_1 = require("./rebarShape");
const rebarSingle_1 = require("./rebarSingle");
const rebarStirrups_1 = require("./rebarStirrups");
const referenceElement_1 = require("./referenceElement");
const region2D_1 = require("./region2D");
const region3D_1 = require("./region3D");
const reinfBarSurface_1 = require("./reinfBarSurface");
const reinforcedBar_1 = require("./reinforcedBar");
const reinforcedCrossSection_1 = require("./reinforcedCrossSection");
const reinforcement_1 = require("./reinforcement");
const resultClass_1 = require("./resultClass");
const resultLocalSystemType_1 = require("./resultLocalSystemType");
const resultOnMember_1 = require("./resultOnMember");
const resultOnMembers_1 = require("./resultOnMembers");
const resultType_1 = require("./resultType");
const rigidLink_1 = require("./rigidLink");
const segment2D_1 = require("./segment2D");
const selected_1 = require("./selected");
const selectedType_1 = require("./selectedType");
const settlement_1 = require("./settlement");
const solidBlock3D_1 = require("./solidBlock3D");
const span_1 = require("./span");
const stirrup_1 = require("./stirrup");
const strainLoadOnLine_1 = require("./strainLoadOnLine");
const subStructure_1 = require("./subStructure");
const surfaceSupport3D_1 = require("./surfaceSupport3D");
const taper_1 = require("./taper");
const temperatureCurve2D_1 = require("./temperatureCurve2D");
const temperatureLoadOnLine_1 = require("./temperatureLoadOnLine");
const templateConversions_1 = require("./templateConversions");
const tendon_1 = require("./tendon");
const tendonBar_1 = require("./tendonBar");
const tendonBarType_1 = require("./tendonBarType");
const tendonDuct_1 = require("./tendonDuct");
const text_1 = require("./text");
const textPosition_1 = require("./textPosition");
const thermalConductivityState_1 = require("./thermalConductivityState");
const thermalExpansionState_1 = require("./thermalExpansionState");
const thermalSpecificHeatState_1 = require("./thermalSpecificHeatState");
const thermalStrainState_1 = require("./thermalStrainState");
const thermalStressStrainState_1 = require("./thermalStressStrainState");
const uploadIdeaConRequest_1 = require("./uploadIdeaConRequest");
const validationType_1 = require("./validationType");
const vector3D_1 = require("./vector3D");
const wall_1 = require("./wall");
const weldData_1 = require("./weldData");
const weldEvaluation_1 = require("./weldEvaluation");
const weldType_1 = require("./weldType");
/* tslint:disable:no-unused-variable */
let primitives = [
    "string",
    "boolean",
    "double",
    "integer",
    "long",
    "float",
    "number",
    "any"
];
let enumsMap = {
    "AnchorType": anchorType_1.AnchorType,
    "BoltShearType": boltShearType_1.BoltShearType,
    "ConAnalysisTypeEnum": conAnalysisTypeEnum_1.ConAnalysisTypeEnum,
    "ConLoadEffectPositionEnum": conLoadEffectPositionEnum_1.ConLoadEffectPositionEnum,
    "ConeBreakoutCheckType": coneBreakoutCheckType_1.ConeBreakoutCheckType,
    "CrtCompCheckIS": crtCompCheckIS_1.CrtCompCheckIS,
    "CutMethod": cutMethod_1.CutMethod,
    "CutOrientation": cutOrientation_1.CutOrientation,
    "CutPart": cutPart_1.CutPart,
    "DistanceComparison": distanceComparison_1.DistanceComparison,
    "EPurpose": ePurpose_1.EPurpose,
    "FatigueTypeOfPrestressingSteel": fatigueTypeOfPrestressingSteel_1.FatigueTypeOfPrestressingSteel,
    "LoadingType": loadingType_1.LoadingType,
    "MaterialDuct": materialDuct_1.MaterialDuct,
    "MemberType": memberType_1.MemberType,
    "MessageNumber": messageNumber_1.MessageNumber,
    "ReinfBarSurface": reinfBarSurface_1.ReinfBarSurface,
    "ResultLocalSystemType": resultLocalSystemType_1.ResultLocalSystemType,
    "ResultType": resultType_1.ResultType,
    "TendonBarType": tendonBarType_1.TendonBarType,
    "ThermalConductivityState": thermalConductivityState_1.ThermalConductivityState,
    "ThermalExpansionState": thermalExpansionState_1.ThermalExpansionState,
    "ThermalSpecificHeatState": thermalSpecificHeatState_1.ThermalSpecificHeatState,
    "ThermalStrainState": thermalStrainState_1.ThermalStrainState,
    "ThermalStressStrainState": thermalStressStrainState_1.ThermalStressStrainState,
    "ValidationType": validationType_1.ValidationType,
    "WeldEvaluation": weldEvaluation_1.WeldEvaluation,
    "WeldType": weldType_1.WeldType,
};
let typeMap = {
    "Anchor3D": anchor3D_1.Anchor3D,
    "AnchorGrid": anchorGrid_1.AnchorGrid,
    "ArcSegment3D": arcSegment3D_1.ArcSegment3D,
    "BasePlate3D": basePlate3D_1.BasePlate3D,
    "BaseTemplateConversion": baseTemplateConversion_1.BaseTemplateConversion,
    "Beam": beam_1.Beam,
    "BeamData": beamData_1.BeamData,
    "BendData": bendData_1.BendData,
    "BoltGrid": boltGrid_1.BoltGrid,
    "BucklingRes": bucklingRes_1.BucklingRes,
    "CheckMember": checkMember_1.CheckMember,
    "CheckResAnchor": checkResAnchor_1.CheckResAnchor,
    "CheckResBolt": checkResBolt_1.CheckResBolt,
    "CheckResConcreteBlock": checkResConcreteBlock_1.CheckResConcreteBlock,
    "CheckResPlate": checkResPlate_1.CheckResPlate,
    "CheckResSummary": checkResSummary_1.CheckResSummary,
    "CheckResWeld": checkResWeld_1.CheckResWeld,
    "CheckSection": checkSection_1.CheckSection,
    "CombiInput": combiInput_1.CombiInput,
    "ConCalculationParameter": conCalculationParameter_1.ConCalculationParameter,
    "ConConnection": conConnection_1.ConConnection,
    "ConLoadEffect": conLoadEffect_1.ConLoadEffect,
    "ConLoadEffectMemberLoad": conLoadEffectMemberLoad_1.ConLoadEffectMemberLoad,
    "ConLoadEffectSectionLoad": conLoadEffectSectionLoad_1.ConLoadEffectSectionLoad,
    "ConLoadingOptions": conLoadingOptions_1.ConLoadingOptions,
    "ConMember": conMember_1.ConMember,
    "ConMissingWeld": conMissingWeld_1.ConMissingWeld,
    "ConMprlCrossSection": conMprlCrossSection_1.ConMprlCrossSection,
    "ConMprlElement": conMprlElement_1.ConMprlElement,
    "ConOperation": conOperation_1.ConOperation,
    "ConProductionCost": conProductionCost_1.ConProductionCost,
    "ConProject": conProject_1.ConProject,
    "ConProjectData": conProjectData_1.ConProjectData,
    "ConResultSummary": conResultSummary_1.ConResultSummary,
    "ConTemplateApplyParam": conTemplateApplyParam_1.ConTemplateApplyParam,
    "ConTemplateMappingGetParam": conTemplateMappingGetParam_1.ConTemplateMappingGetParam,
    "ConcreteBlock": concreteBlock_1.ConcreteBlock,
    "ConcreteBlockData": concreteBlockData_1.ConcreteBlockData,
    "ConcreteSetup": concreteSetup_1.ConcreteSetup,
    "ConnectionCheckRes": connectionCheckRes_1.ConnectionCheckRes,
    "ConnectionData": connectionData_1.ConnectionData,
    "ConnectionPoint": connectionPoint_1.ConnectionPoint,
    "ConnectionSetup": connectionSetup_1.ConnectionSetup,
    "CrossSection": crossSection_1.CrossSection,
    "CutBeamByBeamData": cutBeamByBeamData_1.CutBeamByBeamData,
    "CutData": cutData_1.CutData,
    "DappedEnd": dappedEnd_1.DappedEnd,
    "DesignMember": designMember_1.DesignMember,
    "DetailCombination": detailCombination_1.DetailCombination,
    "DetailLoadCase": detailLoadCase_1.DetailLoadCase,
    "DrawData": drawData_1.DrawData,
    "Element1D": element1D_1.Element1D,
    "Element2D": element2D_1.Element2D,
    "FoldedPlateData": foldedPlateData_1.FoldedPlateData,
    "HingeElement1D": hingeElement1D_1.HingeElement1D,
    "IGroup": iGroup_1.IGroup,
    "ISDModel": iSDModel_1.ISDModel,
    "IdeaParameter": ideaParameter_1.IdeaParameter,
    "IdeaParameterUpdate": ideaParameterUpdate_1.IdeaParameterUpdate,
    "InitialImperfectionOfPoint": initialImperfectionOfPoint_1.InitialImperfectionOfPoint,
    "Line": line_1.Line,
    "LineSegment3D": lineSegment3D_1.LineSegment3D,
    "LineSupportSegment": lineSupportSegment_1.LineSupportSegment,
    "LoadCase": loadCase_1.LoadCase,
    "LoadEffectData": loadEffectData_1.LoadEffectData,
    "LoadGroup": loadGroup_1.LoadGroup,
    "LoadInPoint": loadInPoint_1.LoadInPoint,
    "LoadOnLine": loadOnLine_1.LoadOnLine,
    "LoadOnSurface": loadOnSurface_1.LoadOnSurface,
    "Loading": loading_1.Loading,
    "MatConcrete": matConcrete_1.MatConcrete,
    "MatPrestressSteel": matPrestressSteel_1.MatPrestressSteel,
    "MatReinforcement": matReinforcement_1.MatReinforcement,
    "MatSteel": matSteel_1.MatSteel,
    "MatWelding": matWelding_1.MatWelding,
    "Member": member_1.Member,
    "Member1D": member1D_1.Member1D,
    "Member2D": member2D_1.Member2D,
    "MemoryStream": memoryStream_1.MemoryStream,
    "OkObjectResult": okObjectResult_1.OkObjectResult,
    "OpenElementId": openElementId_1.OpenElementId,
    "OpenMessage": openMessage_1.OpenMessage,
    "OpenMessages": openMessages_1.OpenMessages,
    "OpenModel": openModel_1.OpenModel,
    "OpenModelContainer": openModelContainer_1.OpenModelContainer,
    "OpenModelResult": openModelResult_1.OpenModelResult,
    "Opening": opening_1.Opening,
    "ParameterData": parameterData_1.ParameterData,
    "PatchDevice": patchDevice_1.PatchDevice,
    "PlateData": plateData_1.PlateData,
    "Point2D": point2D_1.Point2D,
    "Point3D": point3D_1.Point3D,
    "PointLoadOnLine": pointLoadOnLine_1.PointLoadOnLine,
    "PointOnLine3D": pointOnLine3D_1.PointOnLine3D,
    "PointSupportNode": pointSupportNode_1.PointSupportNode,
    "PolyLine2D": polyLine2D_1.PolyLine2D,
    "PolyLine3D": polyLine3D_1.PolyLine3D,
    "Polygon2D": polygon2D_1.Polygon2D,
    "RebarGeneral": rebarGeneral_1.RebarGeneral,
    "RebarShape": rebarShape_1.RebarShape,
    "RebarSingle": rebarSingle_1.RebarSingle,
    "RebarStirrups": rebarStirrups_1.RebarStirrups,
    "ReferenceElement": referenceElement_1.ReferenceElement,
    "Region2D": region2D_1.Region2D,
    "Region3D": region3D_1.Region3D,
    "ReinforcedBar": reinforcedBar_1.ReinforcedBar,
    "ReinforcedCrossSection": reinforcedCrossSection_1.ReinforcedCrossSection,
    "Reinforcement": reinforcement_1.Reinforcement,
    "ResultClass": resultClass_1.ResultClass,
    "ResultOnMember": resultOnMember_1.ResultOnMember,
    "ResultOnMembers": resultOnMembers_1.ResultOnMembers,
    "RigidLink": rigidLink_1.RigidLink,
    "Segment2D": segment2D_1.Segment2D,
    "Selected": selected_1.Selected,
    "SelectedType": selectedType_1.SelectedType,
    "Settlement": settlement_1.Settlement,
    "SolidBlock3D": solidBlock3D_1.SolidBlock3D,
    "Span": span_1.Span,
    "Stirrup": stirrup_1.Stirrup,
    "StrainLoadOnLine": strainLoadOnLine_1.StrainLoadOnLine,
    "SubStructure": subStructure_1.SubStructure,
    "SurfaceSupport3D": surfaceSupport3D_1.SurfaceSupport3D,
    "Taper": taper_1.Taper,
    "TemperatureCurve2D": temperatureCurve2D_1.TemperatureCurve2D,
    "TemperatureLoadOnLine": temperatureLoadOnLine_1.TemperatureLoadOnLine,
    "TemplateConversions": templateConversions_1.TemplateConversions,
    "Tendon": tendon_1.Tendon,
    "TendonBar": tendonBar_1.TendonBar,
    "TendonDuct": tendonDuct_1.TendonDuct,
    "Text": text_1.Text,
    "TextPosition": textPosition_1.TextPosition,
    "UploadIdeaConRequest": uploadIdeaConRequest_1.UploadIdeaConRequest,
    "Vector3D": vector3D_1.Vector3D,
    "Wall": wall_1.Wall,
    "WeldData": weldData_1.WeldData,
};
class ObjectSerializer {
    static findCorrectType(data, expectedType) {
        if (data == undefined) {
            return expectedType;
        }
        else if (primitives.indexOf(expectedType.toLowerCase()) !== -1) {
            return expectedType;
        }
        else if (expectedType === "Date") {
            return expectedType;
        }
        else {
            if (enumsMap[expectedType]) {
                return expectedType;
            }
            if (!typeMap[expectedType]) {
                return expectedType; // w/e we don't know the type
            }
            // Check the discriminator
            let discriminatorProperty = typeMap[expectedType].discriminator;
            if (discriminatorProperty == null) {
                return expectedType; // the type does not have a discriminator. use it.
            }
            else {
                if (data[discriminatorProperty]) {
                    var discriminatorType = data[discriminatorProperty];
                    if (typeMap[discriminatorType]) {
                        return discriminatorType; // use the type given in the discriminator
                    }
                    else {
                        return expectedType; // discriminator did not map to a type
                    }
                }
                else {
                    return expectedType; // discriminator was not present (or an empty string)
                }
            }
        }
    }
    static serialize(data, type) {
        if (data == undefined) {
            return data;
        }
        else if (primitives.indexOf(type.toLowerCase()) !== -1) {
            return data;
        }
        else if (type.lastIndexOf("Array<", 0) === 0) { // string.startsWith pre es6
            let subType = type.replace("Array<", ""); // Array<Type> => Type>
            subType = subType.substring(0, subType.length - 1); // Type> => Type
            let transformedData = [];
            for (let index = 0; index < data.length; index++) {
                let datum = data[index];
                transformedData.push(ObjectSerializer.serialize(datum, subType));
            }
            return transformedData;
        }
        else if (type === "Date") {
            return data.toISOString();
        }
        else {
            if (enumsMap[type]) {
                return data;
            }
            if (!typeMap[type]) { // in case we dont know the type
                return data;
            }
            // Get the actual type of this object
            type = this.findCorrectType(data, type);
            // get the map for the correct type.
            let attributeTypes = typeMap[type].getAttributeTypeMap();
            let instance = {};
            for (let index = 0; index < attributeTypes.length; index++) {
                let attributeType = attributeTypes[index];
                instance[attributeType.baseName] = ObjectSerializer.serialize(data[attributeType.name], attributeType.type);
            }
            return instance;
        }
    }
    static deserialize(data, type) {
        // polymorphism may change the actual type.
        type = ObjectSerializer.findCorrectType(data, type);
        if (data == undefined) {
            return data;
        }
        else if (primitives.indexOf(type.toLowerCase()) !== -1) {
            return data;
        }
        else if (type.lastIndexOf("Array<", 0) === 0) { // string.startsWith pre es6
            let subType = type.replace("Array<", ""); // Array<Type> => Type>
            subType = subType.substring(0, subType.length - 1); // Type> => Type
            let transformedData = [];
            for (let index = 0; index < data.length; index++) {
                let datum = data[index];
                transformedData.push(ObjectSerializer.deserialize(datum, subType));
            }
            return transformedData;
        }
        else if (type === "Date") {
            return new Date(data);
        }
        else {
            if (enumsMap[type]) { // is Enum
                return data;
            }
            if (!typeMap[type]) { // dont know the type
                return data;
            }
            let instance = new typeMap[type]();
            let attributeTypes = typeMap[type].getAttributeTypeMap();
            for (let index = 0; index < attributeTypes.length; index++) {
                let attributeType = attributeTypes[index];
                instance[attributeType.name] = ObjectSerializer.deserialize(data[attributeType.baseName], attributeType.type);
            }
            return instance;
        }
    }
}
exports.ObjectSerializer = ObjectSerializer;
class HttpBasicAuth {
    constructor() {
        this.username = '';
        this.password = '';
    }
    applyToRequest(requestOptions) {
        requestOptions.auth = {
            username: this.username, password: this.password
        };
    }
}
exports.HttpBasicAuth = HttpBasicAuth;
class HttpBearerAuth {
    constructor() {
        this.accessToken = '';
    }
    applyToRequest(requestOptions) {
        if (requestOptions && requestOptions.headers) {
            const accessToken = typeof this.accessToken === 'function'
                ? this.accessToken()
                : this.accessToken;
            requestOptions.headers["Authorization"] = "Bearer " + accessToken;
        }
    }
}
exports.HttpBearerAuth = HttpBearerAuth;
class ApiKeyAuth {
    constructor(location, paramName) {
        this.location = location;
        this.paramName = paramName;
        this.apiKey = '';
    }
    applyToRequest(requestOptions) {
        if (this.location == "query") {
            requestOptions.qs[this.paramName] = this.apiKey;
        }
        else if (this.location == "header" && requestOptions && requestOptions.headers) {
            requestOptions.headers[this.paramName] = this.apiKey;
        }
        else if (this.location == 'cookie' && requestOptions && requestOptions.headers) {
            if (requestOptions.headers['Cookie']) {
                requestOptions.headers['Cookie'] += '; ' + this.paramName + '=' + encodeURIComponent(this.apiKey);
            }
            else {
                requestOptions.headers['Cookie'] = this.paramName + '=' + encodeURIComponent(this.apiKey);
            }
        }
    }
}
exports.ApiKeyAuth = ApiKeyAuth;
class OAuth {
    constructor() {
        this.accessToken = '';
    }
    applyToRequest(requestOptions) {
        if (requestOptions && requestOptions.headers) {
            requestOptions.headers["Authorization"] = "Bearer " + this.accessToken;
        }
    }
}
exports.OAuth = OAuth;
class VoidAuth {
    constructor() {
        this.username = '';
        this.password = '';
    }
    applyToRequest(_) {
        // Do nothing
    }
}
exports.VoidAuth = VoidAuth;
