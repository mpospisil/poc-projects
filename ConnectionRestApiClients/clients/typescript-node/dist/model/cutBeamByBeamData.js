"use strict";
/**
 * Connection Rest API 1.0
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 1.0
 *
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */
Object.defineProperty(exports, "__esModule", { value: true });
exports.CutBeamByBeamData = void 0;
/**
* Provides data of the cut objec by object
*/
class CutBeamByBeamData {
    static getAttributeTypeMap() {
        return CutBeamByBeamData.attributeTypeMap;
    }
}
exports.CutBeamByBeamData = CutBeamByBeamData;
CutBeamByBeamData.discriminator = undefined;
CutBeamByBeamData.attributeTypeMap = [
    {
        "name": "name",
        "baseName": "name",
        "type": "string"
    },
    {
        "name": "modifiedObject",
        "baseName": "modifiedObject",
        "type": "ReferenceElement"
    },
    {
        "name": "cuttingObject",
        "baseName": "cuttingObject",
        "type": "ReferenceElement"
    },
    {
        "name": "isWeld",
        "baseName": "isWeld",
        "type": "boolean"
    },
    {
        "name": "weldThickness",
        "baseName": "weldThickness",
        "type": "number"
    },
    {
        "name": "weldType",
        "baseName": "weldType",
        "type": "WeldType"
    },
    {
        "name": "offset",
        "baseName": "offset",
        "type": "number"
    },
    {
        "name": "method",
        "baseName": "method",
        "type": "CutMethod"
    },
    {
        "name": "orientation",
        "baseName": "orientation",
        "type": "CutOrientation"
    },
    {
        "name": "planeOnCuttingObject",
        "baseName": "planeOnCuttingObject",
        "type": "DistanceComparison"
    },
    {
        "name": "cutPart",
        "baseName": "cutPart",
        "type": "CutPart"
    },
    {
        "name": "extendBeforeCut",
        "baseName": "extendBeforeCut",
        "type": "boolean"
    }
];
