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
exports.ConLoadingOptions = void 0;
class ConLoadingOptions {
    static getAttributeTypeMap() {
        return ConLoadingOptions.attributeTypeMap;
    }
}
exports.ConLoadingOptions = ConLoadingOptions;
ConLoadingOptions.discriminator = undefined;
ConLoadingOptions.attributeTypeMap = [
    {
        "name": "loadsInEquilibrium",
        "baseName": "loadsInEquilibrium",
        "type": "boolean"
    },
    {
        "name": "loadsInPercentage",
        "baseName": "loadsInPercentage",
        "type": "boolean"
    }
];
