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
exports.RebarSingle = void 0;
/**
* Represents a single main rebar in 3D space.
*/
class RebarSingle {
    static getAttributeTypeMap() {
        return RebarSingle.attributeTypeMap;
    }
}
exports.RebarSingle = RebarSingle;
RebarSingle.discriminator = undefined;
RebarSingle.attributeTypeMap = [
    {
        "name": "id",
        "baseName": "id",
        "type": "number"
    }
];
