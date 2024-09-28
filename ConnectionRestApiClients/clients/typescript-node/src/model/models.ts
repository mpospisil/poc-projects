import localVarRequest from 'request';

export * from './anchor3D';
export * from './anchorGrid';
export * from './anchorType';
export * from './arcSegment3D';
export * from './basePlate3D';
export * from './baseTemplateConversion';
export * from './beam';
export * from './beamData';
export * from './bendData';
export * from './boltGrid';
export * from './boltShearType';
export * from './bucklingRes';
export * from './checkMember';
export * from './checkResAnchor';
export * from './checkResBolt';
export * from './checkResConcreteBlock';
export * from './checkResPlate';
export * from './checkResSummary';
export * from './checkResWeld';
export * from './checkSection';
export * from './combiInput';
export * from './conAnalysisTypeEnum';
export * from './conCalculationParameter';
export * from './conConnection';
export * from './conLoadEffect';
export * from './conLoadEffectMemberLoad';
export * from './conLoadEffectPositionEnum';
export * from './conLoadEffectSectionLoad';
export * from './conLoadSettings';
export * from './conMember';
export * from './conMprlCrossSection';
export * from './conMprlElement';
export * from './conOperation';
export * from './conProductionCost';
export * from './conProject';
export * from './conProjectData';
export * from './conResultSummary';
export * from './conTemplateApplyParam';
export * from './conTemplateMappingGetParam';
export * from './concreteBlock';
export * from './concreteBlockData';
export * from './concreteSetup';
export * from './coneBreakoutCheckType';
export * from './connectionCheckRes';
export * from './connectionData';
export * from './connectionPoint';
export * from './connectionSetup';
export * from './crossSection';
export * from './crtCompCheckIS';
export * from './cutBeamByBeamData';
export * from './cutData';
export * from './cutMethod';
export * from './cutOrientation';
export * from './cutPart';
export * from './dappedEnd';
export * from './designMember';
export * from './detailCombination';
export * from './detailLoadCase';
export * from './distanceComparison';
export * from './drawData';
export * from './ePurpose';
export * from './element1D';
export * from './element2D';
export * from './fatigueTypeOfPrestressingSteel';
export * from './foldedPlateData';
export * from './hingeElement1D';
export * from './iGroup';
export * from './iSDModel';
export * from './ideaParameter';
export * from './ideaParameterUpdate';
export * from './initialImperfectionOfPoint';
export * from './line';
export * from './lineSegment3D';
export * from './lineSupportSegment';
export * from './loadCase';
export * from './loadEffectData';
export * from './loadGroup';
export * from './loadInPoint';
export * from './loadOnLine';
export * from './loadOnSurface';
export * from './loading';
export * from './loadingType';
export * from './matConcrete';
export * from './matPrestressSteel';
export * from './matReinforcement';
export * from './matSteel';
export * from './matWelding';
export * from './materialDuct';
export * from './member';
export * from './member1D';
export * from './member2D';
export * from './memberType';
export * from './memoryStream';
export * from './messageNumber';
export * from './openElementId';
export * from './openMessage';
export * from './openMessages';
export * from './openModel';
export * from './openModelContainer';
export * from './openModelResult';
export * from './openProjectRequest';
export * from './opening';
export * from './parameterData';
export * from './patchDevice';
export * from './plateData';
export * from './point2D';
export * from './point3D';
export * from './pointLoadOnLine';
export * from './pointOnLine3D';
export * from './pointSupportNode';
export * from './polyLine2D';
export * from './polyLine3D';
export * from './polygon2D';
export * from './rebarGeneral';
export * from './rebarShape';
export * from './rebarSingle';
export * from './rebarStirrups';
export * from './referenceElement';
export * from './region2D';
export * from './region3D';
export * from './reinfBarSurface';
export * from './reinforcedBar';
export * from './reinforcedCrossSection';
export * from './reinforcement';
export * from './resultClass';
export * from './resultLocalSystemType';
export * from './resultOnMember';
export * from './resultOnMembers';
export * from './resultType';
export * from './rigidLink';
export * from './segment2D';
export * from './selected';
export * from './selectedType';
export * from './settlement';
export * from './solidBlock3D';
export * from './span';
export * from './stirrup';
export * from './strainLoadOnLine';
export * from './subStructure';
export * from './surfaceSupport3D';
export * from './taper';
export * from './temperatureCurve2D';
export * from './temperatureLoadOnLine';
export * from './templateConversions';
export * from './tendon';
export * from './tendonBar';
export * from './tendonBarType';
export * from './tendonDuct';
export * from './text';
export * from './textPosition';
export * from './thermalConductivityState';
export * from './thermalExpansionState';
export * from './thermalSpecificHeatState';
export * from './thermalStrainState';
export * from './thermalStressStrainState';
export * from './validationType';
export * from './vector3D';
export * from './wall';
export * from './weldData';
export * from './weldEvaluation';
export * from './weldType';

import * as fs from 'fs';

export interface RequestDetailedFile {
    value: Buffer;
    options?: {
        filename?: string;
        contentType?: string;
    }
}

export type RequestFile = string | Buffer | fs.ReadStream | RequestDetailedFile;


import { Anchor3D } from './anchor3D';
import { AnchorGrid } from './anchorGrid';
import { AnchorType } from './anchorType';
import { ArcSegment3D } from './arcSegment3D';
import { BasePlate3D } from './basePlate3D';
import { BaseTemplateConversion } from './baseTemplateConversion';
import { Beam } from './beam';
import { BeamData } from './beamData';
import { BendData } from './bendData';
import { BoltGrid } from './boltGrid';
import { BoltShearType } from './boltShearType';
import { BucklingRes } from './bucklingRes';
import { CheckMember } from './checkMember';
import { CheckResAnchor } from './checkResAnchor';
import { CheckResBolt } from './checkResBolt';
import { CheckResConcreteBlock } from './checkResConcreteBlock';
import { CheckResPlate } from './checkResPlate';
import { CheckResSummary } from './checkResSummary';
import { CheckResWeld } from './checkResWeld';
import { CheckSection } from './checkSection';
import { CombiInput } from './combiInput';
import { ConAnalysisTypeEnum } from './conAnalysisTypeEnum';
import { ConCalculationParameter } from './conCalculationParameter';
import { ConConnection } from './conConnection';
import { ConLoadEffect } from './conLoadEffect';
import { ConLoadEffectMemberLoad } from './conLoadEffectMemberLoad';
import { ConLoadEffectPositionEnum } from './conLoadEffectPositionEnum';
import { ConLoadEffectSectionLoad } from './conLoadEffectSectionLoad';
import { ConLoadSettings } from './conLoadSettings';
import { ConMember } from './conMember';
import { ConMprlCrossSection } from './conMprlCrossSection';
import { ConMprlElement } from './conMprlElement';
import { ConOperation } from './conOperation';
import { ConProductionCost } from './conProductionCost';
import { ConProject } from './conProject';
import { ConProjectData } from './conProjectData';
import { ConResultSummary } from './conResultSummary';
import { ConTemplateApplyParam } from './conTemplateApplyParam';
import { ConTemplateMappingGetParam } from './conTemplateMappingGetParam';
import { ConcreteBlock } from './concreteBlock';
import { ConcreteBlockData } from './concreteBlockData';
import { ConcreteSetup } from './concreteSetup';
import { ConeBreakoutCheckType } from './coneBreakoutCheckType';
import { ConnectionCheckRes } from './connectionCheckRes';
import { ConnectionData } from './connectionData';
import { ConnectionPoint } from './connectionPoint';
import { ConnectionSetup } from './connectionSetup';
import { CrossSection } from './crossSection';
import { CrtCompCheckIS } from './crtCompCheckIS';
import { CutBeamByBeamData } from './cutBeamByBeamData';
import { CutData } from './cutData';
import { CutMethod } from './cutMethod';
import { CutOrientation } from './cutOrientation';
import { CutPart } from './cutPart';
import { DappedEnd } from './dappedEnd';
import { DesignMember } from './designMember';
import { DetailCombination } from './detailCombination';
import { DetailLoadCase } from './detailLoadCase';
import { DistanceComparison } from './distanceComparison';
import { DrawData } from './drawData';
import { EPurpose } from './ePurpose';
import { Element1D } from './element1D';
import { Element2D } from './element2D';
import { FatigueTypeOfPrestressingSteel } from './fatigueTypeOfPrestressingSteel';
import { FoldedPlateData } from './foldedPlateData';
import { HingeElement1D } from './hingeElement1D';
import { IGroup } from './iGroup';
import { ISDModel } from './iSDModel';
import { IdeaParameter } from './ideaParameter';
import { IdeaParameterUpdate } from './ideaParameterUpdate';
import { InitialImperfectionOfPoint } from './initialImperfectionOfPoint';
import { Line } from './line';
import { LineSegment3D } from './lineSegment3D';
import { LineSupportSegment } from './lineSupportSegment';
import { LoadCase } from './loadCase';
import { LoadEffectData } from './loadEffectData';
import { LoadGroup } from './loadGroup';
import { LoadInPoint } from './loadInPoint';
import { LoadOnLine } from './loadOnLine';
import { LoadOnSurface } from './loadOnSurface';
import { Loading } from './loading';
import { LoadingType } from './loadingType';
import { MatConcrete } from './matConcrete';
import { MatPrestressSteel } from './matPrestressSteel';
import { MatReinforcement } from './matReinforcement';
import { MatSteel } from './matSteel';
import { MatWelding } from './matWelding';
import { MaterialDuct } from './materialDuct';
import { Member } from './member';
import { Member1D } from './member1D';
import { Member2D } from './member2D';
import { MemberType } from './memberType';
import { MemoryStream } from './memoryStream';
import { MessageNumber } from './messageNumber';
import { OpenElementId } from './openElementId';
import { OpenMessage } from './openMessage';
import { OpenMessages } from './openMessages';
import { OpenModel } from './openModel';
import { OpenModelContainer } from './openModelContainer';
import { OpenModelResult } from './openModelResult';
import { OpenProjectRequest } from './openProjectRequest';
import { Opening } from './opening';
import { ParameterData } from './parameterData';
import { PatchDevice } from './patchDevice';
import { PlateData } from './plateData';
import { Point2D } from './point2D';
import { Point3D } from './point3D';
import { PointLoadOnLine } from './pointLoadOnLine';
import { PointOnLine3D } from './pointOnLine3D';
import { PointSupportNode } from './pointSupportNode';
import { PolyLine2D } from './polyLine2D';
import { PolyLine3D } from './polyLine3D';
import { Polygon2D } from './polygon2D';
import { RebarGeneral } from './rebarGeneral';
import { RebarShape } from './rebarShape';
import { RebarSingle } from './rebarSingle';
import { RebarStirrups } from './rebarStirrups';
import { ReferenceElement } from './referenceElement';
import { Region2D } from './region2D';
import { Region3D } from './region3D';
import { ReinfBarSurface } from './reinfBarSurface';
import { ReinforcedBar } from './reinforcedBar';
import { ReinforcedCrossSection } from './reinforcedCrossSection';
import { Reinforcement } from './reinforcement';
import { ResultClass } from './resultClass';
import { ResultLocalSystemType } from './resultLocalSystemType';
import { ResultOnMember } from './resultOnMember';
import { ResultOnMembers } from './resultOnMembers';
import { ResultType } from './resultType';
import { RigidLink } from './rigidLink';
import { Segment2D } from './segment2D';
import { Selected } from './selected';
import { SelectedType } from './selectedType';
import { Settlement } from './settlement';
import { SolidBlock3D } from './solidBlock3D';
import { Span } from './span';
import { Stirrup } from './stirrup';
import { StrainLoadOnLine } from './strainLoadOnLine';
import { SubStructure } from './subStructure';
import { SurfaceSupport3D } from './surfaceSupport3D';
import { Taper } from './taper';
import { TemperatureCurve2D } from './temperatureCurve2D';
import { TemperatureLoadOnLine } from './temperatureLoadOnLine';
import { TemplateConversions } from './templateConversions';
import { Tendon } from './tendon';
import { TendonBar } from './tendonBar';
import { TendonBarType } from './tendonBarType';
import { TendonDuct } from './tendonDuct';
import { Text } from './text';
import { TextPosition } from './textPosition';
import { ThermalConductivityState } from './thermalConductivityState';
import { ThermalExpansionState } from './thermalExpansionState';
import { ThermalSpecificHeatState } from './thermalSpecificHeatState';
import { ThermalStrainState } from './thermalStrainState';
import { ThermalStressStrainState } from './thermalStressStrainState';
import { ValidationType } from './validationType';
import { Vector3D } from './vector3D';
import { Wall } from './wall';
import { WeldData } from './weldData';
import { WeldEvaluation } from './weldEvaluation';
import { WeldType } from './weldType';

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

let enumsMap: {[index: string]: any} = {
        "AnchorType": AnchorType,
        "BoltShearType": BoltShearType,
        "ConAnalysisTypeEnum": ConAnalysisTypeEnum,
        "ConLoadEffectPositionEnum": ConLoadEffectPositionEnum,
        "ConeBreakoutCheckType": ConeBreakoutCheckType,
        "CrtCompCheckIS": CrtCompCheckIS,
        "CutMethod": CutMethod,
        "CutOrientation": CutOrientation,
        "CutPart": CutPart,
        "DistanceComparison": DistanceComparison,
        "EPurpose": EPurpose,
        "FatigueTypeOfPrestressingSteel": FatigueTypeOfPrestressingSteel,
        "LoadingType": LoadingType,
        "MaterialDuct": MaterialDuct,
        "MemberType": MemberType,
        "MessageNumber": MessageNumber,
        "ReinfBarSurface": ReinfBarSurface,
        "ResultLocalSystemType": ResultLocalSystemType,
        "ResultType": ResultType,
        "TendonBarType": TendonBarType,
        "ThermalConductivityState": ThermalConductivityState,
        "ThermalExpansionState": ThermalExpansionState,
        "ThermalSpecificHeatState": ThermalSpecificHeatState,
        "ThermalStrainState": ThermalStrainState,
        "ThermalStressStrainState": ThermalStressStrainState,
        "ValidationType": ValidationType,
        "WeldEvaluation": WeldEvaluation,
        "WeldType": WeldType,
}

let typeMap: {[index: string]: any} = {
    "Anchor3D": Anchor3D,
    "AnchorGrid": AnchorGrid,
    "ArcSegment3D": ArcSegment3D,
    "BasePlate3D": BasePlate3D,
    "BaseTemplateConversion": BaseTemplateConversion,
    "Beam": Beam,
    "BeamData": BeamData,
    "BendData": BendData,
    "BoltGrid": BoltGrid,
    "BucklingRes": BucklingRes,
    "CheckMember": CheckMember,
    "CheckResAnchor": CheckResAnchor,
    "CheckResBolt": CheckResBolt,
    "CheckResConcreteBlock": CheckResConcreteBlock,
    "CheckResPlate": CheckResPlate,
    "CheckResSummary": CheckResSummary,
    "CheckResWeld": CheckResWeld,
    "CheckSection": CheckSection,
    "CombiInput": CombiInput,
    "ConCalculationParameter": ConCalculationParameter,
    "ConConnection": ConConnection,
    "ConLoadEffect": ConLoadEffect,
    "ConLoadEffectMemberLoad": ConLoadEffectMemberLoad,
    "ConLoadEffectSectionLoad": ConLoadEffectSectionLoad,
    "ConLoadSettings": ConLoadSettings,
    "ConMember": ConMember,
    "ConMprlCrossSection": ConMprlCrossSection,
    "ConMprlElement": ConMprlElement,
    "ConOperation": ConOperation,
    "ConProductionCost": ConProductionCost,
    "ConProject": ConProject,
    "ConProjectData": ConProjectData,
    "ConResultSummary": ConResultSummary,
    "ConTemplateApplyParam": ConTemplateApplyParam,
    "ConTemplateMappingGetParam": ConTemplateMappingGetParam,
    "ConcreteBlock": ConcreteBlock,
    "ConcreteBlockData": ConcreteBlockData,
    "ConcreteSetup": ConcreteSetup,
    "ConnectionCheckRes": ConnectionCheckRes,
    "ConnectionData": ConnectionData,
    "ConnectionPoint": ConnectionPoint,
    "ConnectionSetup": ConnectionSetup,
    "CrossSection": CrossSection,
    "CutBeamByBeamData": CutBeamByBeamData,
    "CutData": CutData,
    "DappedEnd": DappedEnd,
    "DesignMember": DesignMember,
    "DetailCombination": DetailCombination,
    "DetailLoadCase": DetailLoadCase,
    "DrawData": DrawData,
    "Element1D": Element1D,
    "Element2D": Element2D,
    "FoldedPlateData": FoldedPlateData,
    "HingeElement1D": HingeElement1D,
    "IGroup": IGroup,
    "ISDModel": ISDModel,
    "IdeaParameter": IdeaParameter,
    "IdeaParameterUpdate": IdeaParameterUpdate,
    "InitialImperfectionOfPoint": InitialImperfectionOfPoint,
    "Line": Line,
    "LineSegment3D": LineSegment3D,
    "LineSupportSegment": LineSupportSegment,
    "LoadCase": LoadCase,
    "LoadEffectData": LoadEffectData,
    "LoadGroup": LoadGroup,
    "LoadInPoint": LoadInPoint,
    "LoadOnLine": LoadOnLine,
    "LoadOnSurface": LoadOnSurface,
    "Loading": Loading,
    "MatConcrete": MatConcrete,
    "MatPrestressSteel": MatPrestressSteel,
    "MatReinforcement": MatReinforcement,
    "MatSteel": MatSteel,
    "MatWelding": MatWelding,
    "Member": Member,
    "Member1D": Member1D,
    "Member2D": Member2D,
    "MemoryStream": MemoryStream,
    "OpenElementId": OpenElementId,
    "OpenMessage": OpenMessage,
    "OpenMessages": OpenMessages,
    "OpenModel": OpenModel,
    "OpenModelContainer": OpenModelContainer,
    "OpenModelResult": OpenModelResult,
    "OpenProjectRequest": OpenProjectRequest,
    "Opening": Opening,
    "ParameterData": ParameterData,
    "PatchDevice": PatchDevice,
    "PlateData": PlateData,
    "Point2D": Point2D,
    "Point3D": Point3D,
    "PointLoadOnLine": PointLoadOnLine,
    "PointOnLine3D": PointOnLine3D,
    "PointSupportNode": PointSupportNode,
    "PolyLine2D": PolyLine2D,
    "PolyLine3D": PolyLine3D,
    "Polygon2D": Polygon2D,
    "RebarGeneral": RebarGeneral,
    "RebarShape": RebarShape,
    "RebarSingle": RebarSingle,
    "RebarStirrups": RebarStirrups,
    "ReferenceElement": ReferenceElement,
    "Region2D": Region2D,
    "Region3D": Region3D,
    "ReinforcedBar": ReinforcedBar,
    "ReinforcedCrossSection": ReinforcedCrossSection,
    "Reinforcement": Reinforcement,
    "ResultClass": ResultClass,
    "ResultOnMember": ResultOnMember,
    "ResultOnMembers": ResultOnMembers,
    "RigidLink": RigidLink,
    "Segment2D": Segment2D,
    "Selected": Selected,
    "SelectedType": SelectedType,
    "Settlement": Settlement,
    "SolidBlock3D": SolidBlock3D,
    "Span": Span,
    "Stirrup": Stirrup,
    "StrainLoadOnLine": StrainLoadOnLine,
    "SubStructure": SubStructure,
    "SurfaceSupport3D": SurfaceSupport3D,
    "Taper": Taper,
    "TemperatureCurve2D": TemperatureCurve2D,
    "TemperatureLoadOnLine": TemperatureLoadOnLine,
    "TemplateConversions": TemplateConversions,
    "Tendon": Tendon,
    "TendonBar": TendonBar,
    "TendonDuct": TendonDuct,
    "Text": Text,
    "TextPosition": TextPosition,
    "Vector3D": Vector3D,
    "Wall": Wall,
    "WeldData": WeldData,
}

export class ObjectSerializer {
    public static findCorrectType(data: any, expectedType: string) {
        if (data == undefined) {
            return expectedType;
        } else if (primitives.indexOf(expectedType.toLowerCase()) !== -1) {
            return expectedType;
        } else if (expectedType === "Date") {
            return expectedType;
        } else {
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
            } else {
                if (data[discriminatorProperty]) {
                    var discriminatorType = data[discriminatorProperty];
                    if(typeMap[discriminatorType]){
                        return discriminatorType; // use the type given in the discriminator
                    } else {
                        return expectedType; // discriminator did not map to a type
                    }
                } else {
                    return expectedType; // discriminator was not present (or an empty string)
                }
            }
        }
    }

    public static serialize(data: any, type: string) {
        if (data == undefined) {
            return data;
        } else if (primitives.indexOf(type.toLowerCase()) !== -1) {
            return data;
        } else if (type.lastIndexOf("Array<", 0) === 0) { // string.startsWith pre es6
            let subType: string = type.replace("Array<", ""); // Array<Type> => Type>
            subType = subType.substring(0, subType.length - 1); // Type> => Type
            let transformedData: any[] = [];
            for (let index = 0; index < data.length; index++) {
                let datum = data[index];
                transformedData.push(ObjectSerializer.serialize(datum, subType));
            }
            return transformedData;
        } else if (type === "Date") {
            return data.toISOString();
        } else {
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
            let instance: {[index: string]: any} = {};
            for (let index = 0; index < attributeTypes.length; index++) {
                let attributeType = attributeTypes[index];
                instance[attributeType.baseName] = ObjectSerializer.serialize(data[attributeType.name], attributeType.type);
            }
            return instance;
        }
    }

    public static deserialize(data: any, type: string) {
        // polymorphism may change the actual type.
        type = ObjectSerializer.findCorrectType(data, type);
        if (data == undefined) {
            return data;
        } else if (primitives.indexOf(type.toLowerCase()) !== -1) {
            return data;
        } else if (type.lastIndexOf("Array<", 0) === 0) { // string.startsWith pre es6
            let subType: string = type.replace("Array<", ""); // Array<Type> => Type>
            subType = subType.substring(0, subType.length - 1); // Type> => Type
            let transformedData: any[] = [];
            for (let index = 0; index < data.length; index++) {
                let datum = data[index];
                transformedData.push(ObjectSerializer.deserialize(datum, subType));
            }
            return transformedData;
        } else if (type === "Date") {
            return new Date(data);
        } else {
            if (enumsMap[type]) {// is Enum
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

export interface Authentication {
    /**
    * Apply authentication settings to header and query params.
    */
    applyToRequest(requestOptions: localVarRequest.Options): Promise<void> | void;
}

export class HttpBasicAuth implements Authentication {
    public username: string = '';
    public password: string = '';

    applyToRequest(requestOptions: localVarRequest.Options): void {
        requestOptions.auth = {
            username: this.username, password: this.password
        }
    }
}

export class HttpBearerAuth implements Authentication {
    public accessToken: string | (() => string) = '';

    applyToRequest(requestOptions: localVarRequest.Options): void {
        if (requestOptions && requestOptions.headers) {
            const accessToken = typeof this.accessToken === 'function'
                            ? this.accessToken()
                            : this.accessToken;
            requestOptions.headers["Authorization"] = "Bearer " + accessToken;
        }
    }
}

export class ApiKeyAuth implements Authentication {
    public apiKey: string = '';

    constructor(private location: string, private paramName: string) {
    }

    applyToRequest(requestOptions: localVarRequest.Options): void {
        if (this.location == "query") {
            (<any>requestOptions.qs)[this.paramName] = this.apiKey;
        } else if (this.location == "header" && requestOptions && requestOptions.headers) {
            requestOptions.headers[this.paramName] = this.apiKey;
        } else if (this.location == 'cookie' && requestOptions && requestOptions.headers) {
            if (requestOptions.headers['Cookie']) {
                requestOptions.headers['Cookie'] += '; ' + this.paramName + '=' + encodeURIComponent(this.apiKey);
            }
            else {
                requestOptions.headers['Cookie'] = this.paramName + '=' + encodeURIComponent(this.apiKey);
            }
        }
    }
}

export class OAuth implements Authentication {
    public accessToken: string = '';

    applyToRequest(requestOptions: localVarRequest.Options): void {
        if (requestOptions && requestOptions.headers) {
            requestOptions.headers["Authorization"] = "Bearer " + this.accessToken;
        }
    }
}

export class VoidAuth implements Authentication {
    public username: string = '';
    public password: string = '';

    applyToRequest(_: localVarRequest.Options): void {
        // Do nothing
    }
}

export type Interceptor = (requestOptions: localVarRequest.Options) => (Promise<void> | void);
