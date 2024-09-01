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
exports.ConConnection = void 0;
class ConConnection {
    static getAttributeTypeMap() {
        return ConConnection.attributeTypeMap;
    }
}
exports.ConConnection = ConConnection;
ConConnection.discriminator = undefined;
ConConnection.attributeTypeMap = [
    {
        "name": "id",
        "baseName": "id",
        "type": "number"
    },
    {
        "name": "identifier",
        "baseName": "identifier",
        "type": "string"
    },
    {
        "name": "name",
        "baseName": "name",
        "type": "string"
    },
    {
        "name": "description",
        "baseName": "description",
        "type": "string"
    },
    {
        "name": "analysisType",
        "baseName": "analysisType",
        "type": "ConAnalysisTypeEnum"
    },
    {
        "name": "loadOptions",
        "baseName": "loadOptions",
        "type": "ConLoadingOptions"
    },
    {
        "name": "bearingMemberId",
        "baseName": "bearingMemberId",
        "type": "number"
    },
    {
        "name": "isCalculated",
        "baseName": "isCalculated",
        "type": "boolean"
    }
];
