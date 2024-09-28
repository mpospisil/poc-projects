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
import { ConConnection } from './conConnection';
import { ConProjectData } from './conProjectData';

export class ConProject {
    'projectId'?: string;
    'projectInfo'?: ConProjectData;
    'connections'?: Array<ConConnection> | null;

    static discriminator: string | undefined = undefined;

    static attributeTypeMap: Array<{name: string, baseName: string, type: string}> = [
        {
            "name": "projectId",
            "baseName": "projectId",
            "type": "string"
        },
        {
            "name": "projectInfo",
            "baseName": "projectInfo",
            "type": "ConProjectData"
        },
        {
            "name": "connections",
            "baseName": "connections",
            "type": "Array<ConConnection>"
        }    ];

    static getAttributeTypeMap() {
        return ConProject.attributeTypeMap;
    }
}
