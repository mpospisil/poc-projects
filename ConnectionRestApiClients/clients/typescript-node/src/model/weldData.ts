/**
 * Connection Rest API 1.0
 * API for designing steel connections
 *
 * The version of the OpenAPI document: 1.0
 * Contact: info@ideastatica.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

import { RequestFile } from './models';
import { Point3D } from './point3D';
import { ReferenceElement } from './referenceElement';
import { WeldType } from './weldType';

/**
* Provides data of the single weld
*/
export class WeldData {
    /**
    * Id of the weld
    */
    'id'?: number;
    /**
    * Name of the weld
    */
    'name'?: string | null;
    /**
    * Thickness of the weld
    */
    'thickness'?: number;
    /**
    * Name of the material
    */
    'material'?: string | null;
    'weldMaterial'?: ReferenceElement;
    'weldType'?: WeldType;
    /**
    * Id of the weld
    */
    'connectedPartIds'?: Array<string> | null;
    'start'?: Point3D;
    'end'?: Point3D;

    static discriminator: string | undefined = undefined;

    static attributeTypeMap: Array<{name: string, baseName: string, type: string}> = [
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
            "name": "thickness",
            "baseName": "thickness",
            "type": "number"
        },
        {
            "name": "material",
            "baseName": "material",
            "type": "string"
        },
        {
            "name": "weldMaterial",
            "baseName": "weldMaterial",
            "type": "ReferenceElement"
        },
        {
            "name": "weldType",
            "baseName": "weldType",
            "type": "WeldType"
        },
        {
            "name": "connectedPartIds",
            "baseName": "connectedPartIds",
            "type": "Array<string>"
        },
        {
            "name": "start",
            "baseName": "start",
            "type": "Point3D"
        },
        {
            "name": "end",
            "baseName": "end",
            "type": "Point3D"
        }    ];

    static getAttributeTypeMap() {
        return WeldData.attributeTypeMap;
    }
}

export namespace WeldData {
}
