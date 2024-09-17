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
import { IGroup } from './iGroup';

export class DrawData {
    'groups'?: Array<IGroup> | null;
    'vertices'?: Array<number> | null;
    'normals'?: Array<number> | null;

    static discriminator: string | undefined = undefined;

    static attributeTypeMap: Array<{name: string, baseName: string, type: string}> = [
        {
            "name": "groups",
            "baseName": "groups",
            "type": "Array<IGroup>"
        },
        {
            "name": "vertices",
            "baseName": "vertices",
            "type": "Array<number>"
        },
        {
            "name": "normals",
            "baseName": "normals",
            "type": "Array<number>"
        }    ];

    static getAttributeTypeMap() {
        return DrawData.attributeTypeMap;
    }
}

