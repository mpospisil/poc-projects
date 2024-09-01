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
import { Point2D } from './point2D';
import { Point3D } from './point3D';
import { Region2D } from './region2D';
import { Vector3D } from './vector3D';
/**
* Provides data of the single plate
*/
export declare class PlateData {
    /**
    * Name of the plate
    */
    'name'?: string | null;
    /**
    * Thickness of the plate
    */
    'thickness'?: number;
    /**
    * Name of the material
    */
    'material'?: string | null;
    /**
    * Outline points
    */
    'outlinePoints'?: Array<Point2D> | null;
    'origin'?: Point3D;
    'axisX'?: Vector3D;
    'axisY'?: Vector3D;
    'axisZ'?: Vector3D;
    /**
    * Geometry of the plate in svg format. In next version will be mark as OBSOLETE! New use property Geometry
    */
    'region'?: string | null;
    'geometry'?: Region2D;
    /**
    * Get or set the identification in the original model  In the case of the imported connection from another application
    */
    'originalModelId'?: string | null;
    /**
    * Is negative object
    */
    'isNegativeObject'?: boolean;
    /**
    * Element Id
    */
    'id'?: number;
    static discriminator: string | undefined;
    static attributeTypeMap: Array<{
        name: string;
        baseName: string;
        type: string;
    }>;
    static getAttributeTypeMap(): {
        name: string;
        baseName: string;
        type: string;
    }[];
}
