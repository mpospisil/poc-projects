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
exports.CheckResPlate = void 0;
/**
* Check value for Plate
*/
class CheckResPlate {
    static getAttributeTypeMap() {
        return CheckResPlate.attributeTypeMap;
    }
}
exports.CheckResPlate = CheckResPlate;
CheckResPlate.discriminator = undefined;
CheckResPlate.attributeTypeMap = [
    {
        "name": "name",
        "baseName": "name",
        "type": "string"
    },
    {
        "name": "checkStatus",
        "baseName": "checkStatus",
        "type": "boolean"
    },
    {
        "name": "loadCaseId",
        "baseName": "loadCaseId",
        "type": "number"
    },
    {
        "name": "maxStrain",
        "baseName": "maxStrain",
        "type": "number"
    },
    {
        "name": "maxStress",
        "baseName": "maxStress",
        "type": "number"
    },
    {
        "name": "items",
        "baseName": "items",
        "type": "Array<number>"
    }
];
