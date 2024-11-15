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
import { CutOrientation } from './cutOrientation';
import { Point3D } from './point3D';
import { Vector3D } from './vector3D';

/**
* Provides data of the cut beam
*/
export class CutData {
    'planePoint'?: Point3D;
    'normalVector'?: Vector3D;
    'direction'?: CutOrientation;
    /**
    * Offset - shift of cut
    */
    'offset'?: number;

    static discriminator: string | undefined = undefined;

    static attributeTypeMap: Array<{name: string, baseName: string, type: string}> = [
        {
            "name": "planePoint",
            "baseName": "planePoint",
            "type": "Point3D"
        },
        {
            "name": "normalVector",
            "baseName": "normalVector",
            "type": "Vector3D"
        },
        {
            "name": "direction",
            "baseName": "direction",
            "type": "CutOrientation"
        },
        {
            "name": "offset",
            "baseName": "offset",
            "type": "number"
        }    ];

    static getAttributeTypeMap() {
        return CutData.attributeTypeMap;
    }
}

export namespace CutData {
}
