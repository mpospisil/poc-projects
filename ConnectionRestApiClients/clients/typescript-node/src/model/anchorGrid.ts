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
import { AnchorType } from './anchorType';
import { BoltShearType } from './boltShearType';
import { ConcreteBlock } from './concreteBlock';
import { Point3D } from './point3D';
import { Vector3D } from './vector3D';

/**
* Data of the anchor grid
*/
export class AnchorGrid {
    'concreteBlock'?: ConcreteBlock;
    'anchorType'?: AnchorType;
    /**
    * Washer Size used if AnchorType is washer
    */
    'washerSize'?: number;
    'boltAssemblyRef'?: string | null;
    /**
    * Unique Id of the bolt grid
    */
    'id'?: number;
    /**
    * Is Anchor
    */
    'isAnchor'?: boolean;
    /**
    * Anchor lenght
    */
    'anchorLen'?: number;
    /**
    * The diameter of the hole
    */
    'holeDiameter'?: number;
    /**
    * The diameter of bolt
    */
    'diameter'?: number;
    /**
    * The head diameter of bolt
    */
    'headDiameter'?: number;
    /**
    * The Diagonal Head Diameter of bolt
    */
    'diagonalHeadDiameter'?: number;
    /**
    * The Head Height of bolt
    */
    'headHeight'?: number;
    /**
    * The BoreHole of bolt
    */
    'boreHole'?: number;
    /**
    * The Tensile Stress Area of bolt
    */
    'tensileStressArea'?: number;
    /**
    * The Nut Thickness of bolt
    */
    'nutThickness'?: number;
    /**
    * The description of the bolt assembly
    */
    'boltAssemblyName'?: string | null;
    /**
    * The standard of the bolt assembly
    */
    'standard'?: string | null;
    /**
    * The material of the bolt assembly
    */
    'material'?: string | null;
    'origin'?: Point3D;
    'axisX'?: Vector3D;
    'axisY'?: Vector3D;
    'axisZ'?: Vector3D;
    /**
    * Positions of holes in the local coodinate system of the bolt grid
    */
    'positions'?: Array<Point3D> | null;
    /**
    * Identifiers of the connected plates
    */
    'connectedPlates'?: Array<number> | null;
    /**
    * Id of the weld
    */
    'connectedPartIds'?: Array<string> | null;
    /**
    * Indicates, whether a shear plane is in the thread of a bolt.
    */
    'shearInThread'?: boolean;
    'boltInteraction'?: BoltShearType;

    static discriminator: string | undefined = undefined;

    static attributeTypeMap: Array<{name: string, baseName: string, type: string}> = [
        {
            "name": "concreteBlock",
            "baseName": "concreteBlock",
            "type": "ConcreteBlock"
        },
        {
            "name": "anchorType",
            "baseName": "anchorType",
            "type": "AnchorType"
        },
        {
            "name": "washerSize",
            "baseName": "washerSize",
            "type": "number"
        },
        {
            "name": "boltAssemblyRef",
            "baseName": "boltAssemblyRef",
            "type": "string"
        },
        {
            "name": "id",
            "baseName": "id",
            "type": "number"
        },
        {
            "name": "isAnchor",
            "baseName": "isAnchor",
            "type": "boolean"
        },
        {
            "name": "anchorLen",
            "baseName": "anchorLen",
            "type": "number"
        },
        {
            "name": "holeDiameter",
            "baseName": "holeDiameter",
            "type": "number"
        },
        {
            "name": "diameter",
            "baseName": "diameter",
            "type": "number"
        },
        {
            "name": "headDiameter",
            "baseName": "headDiameter",
            "type": "number"
        },
        {
            "name": "diagonalHeadDiameter",
            "baseName": "diagonalHeadDiameter",
            "type": "number"
        },
        {
            "name": "headHeight",
            "baseName": "headHeight",
            "type": "number"
        },
        {
            "name": "boreHole",
            "baseName": "boreHole",
            "type": "number"
        },
        {
            "name": "tensileStressArea",
            "baseName": "tensileStressArea",
            "type": "number"
        },
        {
            "name": "nutThickness",
            "baseName": "nutThickness",
            "type": "number"
        },
        {
            "name": "boltAssemblyName",
            "baseName": "boltAssemblyName",
            "type": "string"
        },
        {
            "name": "standard",
            "baseName": "standard",
            "type": "string"
        },
        {
            "name": "material",
            "baseName": "material",
            "type": "string"
        },
        {
            "name": "origin",
            "baseName": "origin",
            "type": "Point3D"
        },
        {
            "name": "axisX",
            "baseName": "axisX",
            "type": "Vector3D"
        },
        {
            "name": "axisY",
            "baseName": "axisY",
            "type": "Vector3D"
        },
        {
            "name": "axisZ",
            "baseName": "axisZ",
            "type": "Vector3D"
        },
        {
            "name": "positions",
            "baseName": "positions",
            "type": "Array<Point3D>"
        },
        {
            "name": "connectedPlates",
            "baseName": "connectedPlates",
            "type": "Array<number>"
        },
        {
            "name": "connectedPartIds",
            "baseName": "connectedPartIds",
            "type": "Array<string>"
        },
        {
            "name": "shearInThread",
            "baseName": "shearInThread",
            "type": "boolean"
        },
        {
            "name": "boltInteraction",
            "baseName": "boltInteraction",
            "type": "BoltShearType"
        }    ];

    static getAttributeTypeMap() {
        return AnchorGrid.attributeTypeMap;
    }
}

export namespace AnchorGrid {
}
