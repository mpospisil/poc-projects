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
exports.Point2D = void 0;
/**
* Represents an x- and y-coordinate pair in two-dimensional space.
*/
class Point2D {
    static getAttributeTypeMap() {
        return Point2D.attributeTypeMap;
    }
}
exports.Point2D = Point2D;
Point2D.discriminator = undefined;
Point2D.attributeTypeMap = [
    {
        "name": "x",
        "baseName": "x",
        "type": "number"
    },
    {
        "name": "y",
        "baseName": "y",
        "type": "number"
    }
];
