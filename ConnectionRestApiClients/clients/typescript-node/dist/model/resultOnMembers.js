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
exports.ResultOnMembers = void 0;
/**
* Result of the member
*/
class ResultOnMembers {
    static getAttributeTypeMap() {
        return ResultOnMembers.attributeTypeMap;
    }
}
exports.ResultOnMembers = ResultOnMembers;
ResultOnMembers.discriminator = undefined;
ResultOnMembers.attributeTypeMap = [
    {
        "name": "loading",
        "baseName": "loading",
        "type": "Loading"
    },
    {
        "name": "members",
        "baseName": "members",
        "type": "Array<ResultOnMember>"
    }
];
