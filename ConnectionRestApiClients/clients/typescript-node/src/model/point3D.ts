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
* Represents an x- , y- an z-coordinates in three-dimensional space.
*/
export class Point3D {
    /**
    * Gets or sets the X-coordinate value
    */
    'x'?: number;
    /**
    * Gets or sets the Y-coordinate value
    */
    'y'?: number;
    /**
    * Gets or sets the Z-coordinate value
    */
    'z'?: number;
    /**
    * Element Id
    */
    'id'?: number;

    static discriminator: string | undefined = undefined;

    static attributeTypeMap: Array<{name: string, baseName: string, type: string}> = [
        {
            "name": "x",
            "baseName": "x",
            "type": "number"
        },
        {
            "name": "y",
            "baseName": "y",
            "type": "number"
        },
        {
            "name": "z",
            "baseName": "z",
            "type": "number"
        },
        {
            "name": "id",
            "baseName": "id",
            "type": "number"
        }    ];

    static getAttributeTypeMap() {
        return Point3D.attributeTypeMap;
    }
}

