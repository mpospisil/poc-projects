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
import { FatigueTypeOfPrestressingSteel } from './fatigueTypeOfPrestressingSteel';
import { Point2D } from './point2D';
import { ReferenceElement } from './referenceElement';
import { TendonBarType } from './tendonBarType';
import { TendonDuct } from './tendonDuct';

/**
* Tendon bar
*/
export class TendonBar {
    /**
    * Tendon Id
    */
    'id'?: number;
    'tendonType'?: TendonBarType;
    'point'?: Point2D;
    'material'?: ReferenceElement;
    /**
    * order of tendon prestessing
    */
    'prestressingOrder'?: number;
    /**
    * number of ropes in tendon
    */
    'numStrandsInTendon'?: number;
    'prestressReinforcementType'?: FatigueTypeOfPrestressingSteel;
    /**
    * Phase
    */
    'phase'?: number;
    'tendonDuct'?: TendonDuct;

    static discriminator: string | undefined = undefined;

    static attributeTypeMap: Array<{name: string, baseName: string, type: string}> = [
        {
            "name": "id",
            "baseName": "id",
            "type": "number"
        },
        {
            "name": "tendonType",
            "baseName": "tendonType",
            "type": "TendonBarType"
        },
        {
            "name": "point",
            "baseName": "point",
            "type": "Point2D"
        },
        {
            "name": "material",
            "baseName": "material",
            "type": "ReferenceElement"
        },
        {
            "name": "prestressingOrder",
            "baseName": "prestressingOrder",
            "type": "number"
        },
        {
            "name": "numStrandsInTendon",
            "baseName": "numStrandsInTendon",
            "type": "number"
        },
        {
            "name": "prestressReinforcementType",
            "baseName": "prestressReinforcementType",
            "type": "FatigueTypeOfPrestressingSteel"
        },
        {
            "name": "phase",
            "baseName": "phase",
            "type": "number"
        },
        {
            "name": "tendonDuct",
            "baseName": "tendonDuct",
            "type": "TendonDuct"
        }    ];

    static getAttributeTypeMap() {
        return TendonBar.attributeTypeMap;
    }
}

export namespace TendonBar {
}