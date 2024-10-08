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
import { ConLoadEffectMemberLoad } from './conLoadEffectMemberLoad';

export class ConLoadEffect {
    'isPercentage'?: boolean;
    'memberLoadings'?: Array<ConLoadEffectMemberLoad> | null;
    'id'?: number;
    'name'?: string | null;
    'active'?: boolean;

    static discriminator: string | undefined = undefined;

    static attributeTypeMap: Array<{name: string, baseName: string, type: string}> = [
        {
            "name": "isPercentage",
            "baseName": "isPercentage",
            "type": "boolean"
        },
        {
            "name": "memberLoadings",
            "baseName": "memberLoadings",
            "type": "Array<ConLoadEffectMemberLoad>"
        },
        {
            "name": "id",
            "baseName": "id",
            "type": "number"
        },
        {
            "name": "name",
            "baseName": "name",
            "type": "string"
        },
        {
            "name": "active",
            "baseName": "active",
            "type": "boolean"
        }    ];

    static getAttributeTypeMap() {
        return ConLoadEffect.attributeTypeMap;
    }
}

