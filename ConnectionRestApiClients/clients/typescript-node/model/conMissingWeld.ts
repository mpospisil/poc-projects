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

export class ConMissingWeld {
    'edgePlate'?: string | null;
    'surfacePlate'?: string | null;
    'edgeIndex'?: number;
    'surfaceIndex'?: number;
    'weldSize'?: number;
    'weldTypeCode'?: string | null;
    'weldMaterialName'?: string | null;
    'isHollowOrUncoiledSection'?: boolean;

    static discriminator: string | undefined = undefined;

    static attributeTypeMap: Array<{name: string, baseName: string, type: string}> = [
        {
            "name": "edgePlate",
            "baseName": "edgePlate",
            "type": "string"
        },
        {
            "name": "surfacePlate",
            "baseName": "surfacePlate",
            "type": "string"
        },
        {
            "name": "edgeIndex",
            "baseName": "edgeIndex",
            "type": "number"
        },
        {
            "name": "surfaceIndex",
            "baseName": "surfaceIndex",
            "type": "number"
        },
        {
            "name": "weldSize",
            "baseName": "weldSize",
            "type": "number"
        },
        {
            "name": "weldTypeCode",
            "baseName": "weldTypeCode",
            "type": "string"
        },
        {
            "name": "weldMaterialName",
            "baseName": "weldMaterialName",
            "type": "string"
        },
        {
            "name": "isHollowOrUncoiledSection",
            "baseName": "isHollow_OrUncoiledSection",
            "type": "boolean"
        }    ];

    static getAttributeTypeMap() {
        return ConMissingWeld.attributeTypeMap;
    }
}

