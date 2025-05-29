import localVarRequest from 'request';

export * from './anchorGrid';
export * from './anchorType';
export * from './baseTemplateConversion';
export * from './beamData';
export * from './bendData';
export * from './boltGrid';
export * from './boltShearType';
export * from './bucklingRes';
export * from './checkResAnchor';
export * from './checkResBolt';
export * from './checkResConcreteBlock';
export * from './checkResPlate';
export * from './checkResSummary';
export * from './checkResWeld';
export * from './conAnalysisTypeEnum';
export * from './conCalculationParameter';
export * from './conConnection';
export * from './conConversionSettings';
export * from './conLoadEffect';
export * from './conLoadEffectMemberLoad';
export * from './conLoadEffectPositionEnum';
export * from './conLoadEffectSectionLoad';
export * from './conLoadSettings';
export * from './conMember';
export * from './conMprlCrossSection';
export * from './conMprlElement';
export * from './conOperation';
export * from './conOperationCommonProperties';
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
export * from './connectionSetup';
export * from './conversionMapping';
export * from './countryCode';
export * from './crtCompCheckIS';
export * from './cutBeamByBeamData';
export * from './cutData';
export * from './cutMethod';
export * from './cutOrientation';
export * from './cutPart';
export * from './distanceComparison';
export * from './drawData';
export * from './foldedPlateData';
export * from './iGroup';
export * from './ideaParameter';
export * from './ideaParameterUpdate';
export * from './ideaParameterValidation';
export * from './line';
export * from './messageNumber';
export * from './openElementId';
export * from './openMessage';
export * from './openMessages';
export * from './pinGrid';
export * from './plateData';
export * from './point2D';
export * from './point3D';
export * from './polyLine2D';
export * from './referenceElement';
export * from './region2D';
export * from './segment2D';
export * from './selected';
export * from './selectedType';
export * from './templateConversions';
export * from './text';
export * from './textPosition';
export * from './vector3D';
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


import { AnchorGrid } from './anchorGrid';
import { AnchorType } from './anchorType';
import { BaseTemplateConversion } from './baseTemplateConversion';
import { BeamData } from './beamData';
import { BendData } from './bendData';
import { BoltGrid } from './boltGrid';
import { BoltShearType } from './boltShearType';
import { BucklingRes } from './bucklingRes';
import { CheckResAnchor } from './checkResAnchor';
import { CheckResBolt } from './checkResBolt';
import { CheckResConcreteBlock } from './checkResConcreteBlock';
import { CheckResPlate } from './checkResPlate';
import { CheckResSummary } from './checkResSummary';
import { CheckResWeld } from './checkResWeld';
import { ConAnalysisTypeEnum } from './conAnalysisTypeEnum';
import { ConCalculationParameter } from './conCalculationParameter';
import { ConConnection } from './conConnection';
import { ConConversionSettings } from './conConversionSettings';
import { ConLoadEffect } from './conLoadEffect';
import { ConLoadEffectMemberLoad } from './conLoadEffectMemberLoad';
import { ConLoadEffectPositionEnum } from './conLoadEffectPositionEnum';
import { ConLoadEffectSectionLoad } from './conLoadEffectSectionLoad';
import { ConLoadSettings } from './conLoadSettings';
import { ConMember } from './conMember';
import { ConMprlCrossSection } from './conMprlCrossSection';
import { ConMprlElement } from './conMprlElement';
import { ConOperation } from './conOperation';
import { ConOperationCommonProperties } from './conOperationCommonProperties';
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
import { ConnectionSetup } from './connectionSetup';
import { ConversionMapping } from './conversionMapping';
import { CountryCode } from './countryCode';
import { CrtCompCheckIS } from './crtCompCheckIS';
import { CutBeamByBeamData } from './cutBeamByBeamData';
import { CutData } from './cutData';
import { CutMethod } from './cutMethod';
import { CutOrientation } from './cutOrientation';
import { CutPart } from './cutPart';
import { DistanceComparison } from './distanceComparison';
import { DrawData } from './drawData';
import { FoldedPlateData } from './foldedPlateData';
import { IGroup } from './iGroup';
import { IdeaParameter } from './ideaParameter';
import { IdeaParameterUpdate } from './ideaParameterUpdate';
import { IdeaParameterValidation } from './ideaParameterValidation';
import { Line } from './line';
import { MessageNumber } from './messageNumber';
import { OpenElementId } from './openElementId';
import { OpenMessage } from './openMessage';
import { OpenMessages } from './openMessages';
import { PinGrid } from './pinGrid';
import { PlateData } from './plateData';
import { Point2D } from './point2D';
import { Point3D } from './point3D';
import { PolyLine2D } from './polyLine2D';
import { ReferenceElement } from './referenceElement';
import { Region2D } from './region2D';
import { Segment2D } from './segment2D';
import { Selected } from './selected';
import { SelectedType } from './selectedType';
import { TemplateConversions } from './templateConversions';
import { Text } from './text';
import { TextPosition } from './textPosition';
import { Vector3D } from './vector3D';
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
        "CountryCode": CountryCode,
        "CrtCompCheckIS": CrtCompCheckIS,
        "CutMethod": CutMethod,
        "CutOrientation": CutOrientation,
        "CutPart": CutPart,
        "DistanceComparison": DistanceComparison,
        "MessageNumber": MessageNumber,
        "WeldEvaluation": WeldEvaluation,
        "WeldType": WeldType,
}

let typeMap: {[index: string]: any} = {
    "AnchorGrid": AnchorGrid,
    "BaseTemplateConversion": BaseTemplateConversion,
    "BeamData": BeamData,
    "BendData": BendData,
    "BoltGrid": BoltGrid,
    "BucklingRes": BucklingRes,
    "CheckResAnchor": CheckResAnchor,
    "CheckResBolt": CheckResBolt,
    "CheckResConcreteBlock": CheckResConcreteBlock,
    "CheckResPlate": CheckResPlate,
    "CheckResSummary": CheckResSummary,
    "CheckResWeld": CheckResWeld,
    "ConCalculationParameter": ConCalculationParameter,
    "ConConnection": ConConnection,
    "ConConversionSettings": ConConversionSettings,
    "ConLoadEffect": ConLoadEffect,
    "ConLoadEffectMemberLoad": ConLoadEffectMemberLoad,
    "ConLoadEffectSectionLoad": ConLoadEffectSectionLoad,
    "ConLoadSettings": ConLoadSettings,
    "ConMember": ConMember,
    "ConMprlCrossSection": ConMprlCrossSection,
    "ConMprlElement": ConMprlElement,
    "ConOperation": ConOperation,
    "ConOperationCommonProperties": ConOperationCommonProperties,
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
    "ConnectionSetup": ConnectionSetup,
    "ConversionMapping": ConversionMapping,
    "CutBeamByBeamData": CutBeamByBeamData,
    "CutData": CutData,
    "DrawData": DrawData,
    "FoldedPlateData": FoldedPlateData,
    "IGroup": IGroup,
    "IdeaParameter": IdeaParameter,
    "IdeaParameterUpdate": IdeaParameterUpdate,
    "IdeaParameterValidation": IdeaParameterValidation,
    "Line": Line,
    "OpenElementId": OpenElementId,
    "OpenMessage": OpenMessage,
    "OpenMessages": OpenMessages,
    "PinGrid": PinGrid,
    "PlateData": PlateData,
    "Point2D": Point2D,
    "Point3D": Point3D,
    "PolyLine2D": PolyLine2D,
    "ReferenceElement": ReferenceElement,
    "Region2D": Region2D,
    "Segment2D": Segment2D,
    "Selected": Selected,
    "SelectedType": SelectedType,
    "TemplateConversions": TemplateConversions,
    "Text": Text,
    "TextPosition": TextPosition,
    "Vector3D": Vector3D,
    "WeldData": WeldData,
}

// Check if a string starts with another string without using es6 features
function startsWith(str: string, match: string): boolean {
    return str.substring(0, match.length) === match;
}

// Check if a string ends with another string without using es6 features
function endsWith(str: string, match: string): boolean {
    return str.length >= match.length && str.substring(str.length - match.length) === match;
}

const nullableSuffix = " | null";
const optionalSuffix = " | undefined";
const arrayPrefix = "Array<";
const arraySuffix = ">";
const mapPrefix = "{ [key: string]: ";
const mapSuffix = "; }";

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

    public static serialize(data: any, type: string): any {
        if (data == undefined) {
            return data;
        } else if (primitives.indexOf(type.toLowerCase()) !== -1) {
            return data;
        } else if (endsWith(type, nullableSuffix)) {
            let subType: string = type.slice(0, -nullableSuffix.length); // Type | null => Type
            return ObjectSerializer.serialize(data, subType);
        } else if (endsWith(type, optionalSuffix)) {
            let subType: string = type.slice(0, -optionalSuffix.length); // Type | undefined => Type
            return ObjectSerializer.serialize(data, subType);
        } else if (startsWith(type, arrayPrefix)) {
            let subType: string = type.slice(arrayPrefix.length, -arraySuffix.length); // Array<Type> => Type
            let transformedData: any[] = [];
            for (let index = 0; index < data.length; index++) {
                let datum = data[index];
                transformedData.push(ObjectSerializer.serialize(datum, subType));
            }
            return transformedData;
        } else if (startsWith(type, mapPrefix)) {
            let subType: string = type.slice(mapPrefix.length, -mapSuffix.length); // { [key: string]: Type; } => Type
            let transformedData: { [key: string]: any } = {};
            for (let key in data) {
                transformedData[key] = ObjectSerializer.serialize(
                    data[key],
                    subType,
                );
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

    public static deserialize(data: any, type: string): any {
        // polymorphism may change the actual type.
        type = ObjectSerializer.findCorrectType(data, type);
        if (data == undefined) {
            return data;
        } else if (primitives.indexOf(type.toLowerCase()) !== -1) {
            return data;
        } else if (endsWith(type, nullableSuffix)) {
            let subType: string = type.slice(0, -nullableSuffix.length); // Type | null => Type
            return ObjectSerializer.deserialize(data, subType);
        } else if (endsWith(type, optionalSuffix)) {
            let subType: string = type.slice(0, -optionalSuffix.length); // Type | undefined => Type
            return ObjectSerializer.deserialize(data, subType);
        } else if (startsWith(type, arrayPrefix)) {
            let subType: string = type.slice(arrayPrefix.length, -arraySuffix.length); // Array<Type> => Type
            let transformedData: any[] = [];
            for (let index = 0; index < data.length; index++) {
                let datum = data[index];
                transformedData.push(ObjectSerializer.deserialize(datum, subType));
            }
            return transformedData;
        } else if (startsWith(type, mapPrefix)) {
            let subType: string = type.slice(mapPrefix.length, -mapSuffix.length); // { [key: string]: Type; } => Type
            let transformedData: { [key: string]: any } = {};
            for (let key in data) {
                transformedData[key] = ObjectSerializer.deserialize(
                    data[key],
                    subType,
                );
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
