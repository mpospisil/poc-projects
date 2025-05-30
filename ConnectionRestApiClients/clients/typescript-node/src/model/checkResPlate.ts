/**
 * Connection Rest API 1.0
 * IDEA StatiCa Connection API, used for the automated design and calculation of steel connections.
 *
 * The version of the OpenAPI document: 1.0
 * Contact: info@ideastatica.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

import { RequestFile } from './models';

/**
* Check value for Plate
*/
export class CheckResPlate {
    /**
    * Name of Plate
    */
    'name'?: string | null;
    /**
    * Status of the Check
    */
    'checkStatus'?: boolean;
    /**
    * Id of Load Case
    */
    'loadCaseId'?: number;
    /**
    * Max Strain
    */
    'maxStrain'?: number;
    /**
    * Max Stress
    */
    'maxStress'?: number;
    /**
    * In case of presentation of groups plates (uncoiled beams)
    */
    'items'?: Array<number> | null;

    static discriminator: string | undefined = undefined;

    static attributeTypeMap: Array<{name: string, baseName: string, type: string}> = [
        {
            "name": "name",
            "baseName": "name",
            "type": "string"
        },
        {
            "name": "checkStatus",
            "baseName": "checkStatus",
            "type": "boolean"
        },
        {
            "name": "loadCaseId",
            "baseName": "loadCaseId",
            "type": "number"
        },
        {
            "name": "maxStrain",
            "baseName": "maxStrain",
            "type": "number"
        },
        {
            "name": "maxStress",
            "baseName": "maxStress",
            "type": "number"
        },
        {
            "name": "items",
            "baseName": "items",
            "type": "Array<number>"
        }    ];

    static getAttributeTypeMap() {
        return CheckResPlate.attributeTypeMap;
    }
}

