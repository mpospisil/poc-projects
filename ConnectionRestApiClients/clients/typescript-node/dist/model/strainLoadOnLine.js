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
exports.StrainLoadOnLine = void 0;
/**
* Linearly distributed generalized strain load along a line.  Strain load is in local coordinate system and there are no possible eccentricities.
*/
class StrainLoadOnLine {
    static getAttributeTypeMap() {
        return StrainLoadOnLine.attributeTypeMap;
    }
}
exports.StrainLoadOnLine = StrainLoadOnLine;
StrainLoadOnLine.discriminator = undefined;
StrainLoadOnLine.attributeTypeMap = [
    {
        "name": "id",
        "baseName": "id",
        "type": "number"
    }
];
