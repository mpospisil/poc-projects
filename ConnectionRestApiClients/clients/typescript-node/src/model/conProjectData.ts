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

export class ConProjectData {
    'name'?: string | null;
    'description'?: string | null;
    'projectNumber'?: string | null;
    'author'?: string | null;
    'designCode'?: string | null;
    'date'?: Date;

    static discriminator: string | undefined = undefined;

    static attributeTypeMap: Array<{name: string, baseName: string, type: string}> = [
        {
            "name": "name",
            "baseName": "name",
            "type": "string"
        },
        {
            "name": "description",
            "baseName": "description",
            "type": "string"
        },
        {
            "name": "projectNumber",
            "baseName": "projectNumber",
            "type": "string"
        },
        {
            "name": "author",
            "baseName": "author",
            "type": "string"
        },
        {
            "name": "designCode",
            "baseName": "designCode",
            "type": "string"
        },
        {
            "name": "date",
            "baseName": "date",
            "type": "Date"
        }    ];

    static getAttributeTypeMap() {
        return ConProjectData.attributeTypeMap;
    }
}

