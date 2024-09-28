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

import { RequestFile } from './models';

/**
* Cross-section
*/
export class CrossSection {
    /**
    * Name of cross-section
    */
    'name'?: string | null;
    /**
    * Rotation of Cross - Section
    */
    'crossSectionRotation'?: number;
    /**
    * Specifies that the cross-section is in its principal axis.
    */
    'isInPrincipal'?: boolean;
    /**
    * Element Id
    */
    'id'?: number;

    static discriminator: string | undefined = undefined;

    static attributeTypeMap: Array<{name: string, baseName: string, type: string}> = [
        {
            "name": "name",
            "baseName": "name",
            "type": "string"
        },
        {
            "name": "crossSectionRotation",
            "baseName": "crossSectionRotation",
            "type": "number"
        },
        {
            "name": "isInPrincipal",
            "baseName": "isInPrincipal",
            "type": "boolean"
        },
        {
            "name": "id",
            "baseName": "id",
            "type": "number"
        }    ];

    static getAttributeTypeMap() {
        return CrossSection.attributeTypeMap;
    }
}
