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

export class ConLoadEffectSectionLoad {
    'n'?: number;
    'vy'?: number;
    'vz'?: number;
    'mx'?: number;
    'my'?: number;
    'mz'?: number;

    static discriminator: string | undefined = undefined;

    static attributeTypeMap: Array<{name: string, baseName: string, type: string}> = [
        {
            "name": "n",
            "baseName": "n",
            "type": "number"
        },
        {
            "name": "vy",
            "baseName": "vy",
            "type": "number"
        },
        {
            "name": "vz",
            "baseName": "vz",
            "type": "number"
        },
        {
            "name": "mx",
            "baseName": "mx",
            "type": "number"
        },
        {
            "name": "my",
            "baseName": "my",
            "type": "number"
        },
        {
            "name": "mz",
            "baseName": "mz",
            "type": "number"
        }    ];

    static getAttributeTypeMap() {
        return ConLoadEffectSectionLoad.attributeTypeMap;
    }
}
