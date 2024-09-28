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
* Results of the buckling analysis
*/
export class BucklingRes {
    'loadCaseId'?: number;
    /**
    * Shape lc calculated by solver
    */
    'shape'?: number;
    /**
    * Buckling factor
    */
    'factor'?: number;

    static discriminator: string | undefined = undefined;

    static attributeTypeMap: Array<{name: string, baseName: string, type: string}> = [
        {
            "name": "loadCaseId",
            "baseName": "loadCaseId",
            "type": "number"
        },
        {
            "name": "shape",
            "baseName": "shape",
            "type": "number"
        },
        {
            "name": "factor",
            "baseName": "factor",
            "type": "number"
        }    ];

    static getAttributeTypeMap() {
        return BucklingRes.attributeTypeMap;
    }
}
