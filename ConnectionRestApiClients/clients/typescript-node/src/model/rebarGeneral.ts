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
* Represents a single main rebar in 3D space.  Holds data from generated rebar or rebar imported from Tekla.  the rebarShape is in global coordinates and it is not possible to prject it along Member1D, Polyline, ... (referenceLine)
*/
export class RebarGeneral {
    /**
    * Element Id
    */
    'id'?: number;

    static discriminator: string | undefined = undefined;

    static attributeTypeMap: Array<{name: string, baseName: string, type: string}> = [
        {
            "name": "id",
            "baseName": "id",
            "type": "number"
        }    ];

    static getAttributeTypeMap() {
        return RebarGeneral.attributeTypeMap;
    }
}
