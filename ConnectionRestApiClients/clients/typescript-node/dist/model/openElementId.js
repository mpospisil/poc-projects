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
exports.OpenElementId = void 0;
/**
* Open element base class  POS - class can not be abstract -it causes problems with serialization
*/
class OpenElementId {
    static getAttributeTypeMap() {
        return OpenElementId.attributeTypeMap;
    }
}
exports.OpenElementId = OpenElementId;
OpenElementId.discriminator = undefined;
OpenElementId.attributeTypeMap = [
    {
        "name": "id",
        "baseName": "id",
        "type": "number"
    }
];
