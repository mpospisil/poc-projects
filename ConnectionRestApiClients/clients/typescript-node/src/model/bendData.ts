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
import { Vector3D } from './vector3D';

/**
* Provides data of bend
*/
export class BendData {
    /**
    * First plate
    */
    'plate1Id'?: number;
    /**
    * Second plate
    */
    'plate2Id'?: number;
    /**
    * Radius of bend
    */
    'radius'?: number;
    'point1OfSideBoundary1'?: Point3D;
    'point2OfSideBoundary1'?: Point3D;
    'endFaceNormal1'?: Vector3D;
    'point1OfSideBoundary2'?: Point3D;
    'point2OfSideBoundary2'?: Point3D;

    static discriminator: string | undefined = undefined;

    static attributeTypeMap: Array<{name: string, baseName: string, type: string}> = [
        {
            "name": "plate1Id",
            "baseName": "plate1Id",
            "type": "number"
        },
        {
            "name": "plate2Id",
            "baseName": "plate2Id",
            "type": "number"
        },
        {
            "name": "radius",
            "baseName": "radius",
            "type": "number"
        },
        {
            "name": "point1OfSideBoundary1",
            "baseName": "point1OfSideBoundary1",
            "type": "Point3D"
        },
        {
            "name": "point2OfSideBoundary1",
            "baseName": "point2OfSideBoundary1",
            "type": "Point3D"
        },
        {
            "name": "endFaceNormal1",
            "baseName": "endFaceNormal1",
            "type": "Vector3D"
        },
        {
            "name": "point1OfSideBoundary2",
            "baseName": "point1OfSideBoundary2",
            "type": "Point3D"
        },
        {
            "name": "point2OfSideBoundary2",
            "baseName": "point2OfSideBoundary2",
            "type": "Point3D"
        }    ];

    static getAttributeTypeMap() {
        return BendData.attributeTypeMap;
    }
}

