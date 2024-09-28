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
* Data of concrete block
*/
export class ConcreteBlock {
    /**
    * Lenght of ConcreteBlock
    */
    'lenght'?: number;
    /**
    * Width of ConcreteBlock
    */
    'width'?: number;
    /**
    * Height of ConcreteBlock
    */
    'height'?: number;
    /**
    * Material of ConcreteBlock
    */
    'material'?: string | null;

    static discriminator: string | undefined = undefined;

    static attributeTypeMap: Array<{name: string, baseName: string, type: string}> = [
        {
            "name": "lenght",
            "baseName": "lenght",
            "type": "number"
        },
        {
            "name": "width",
            "baseName": "width",
            "type": "number"
        },
        {
            "name": "height",
            "baseName": "height",
            "type": "number"
        },
        {
            "name": "material",
            "baseName": "material",
            "type": "string"
        }    ];

    static getAttributeTypeMap() {
        return ConcreteBlock.attributeTypeMap;
    }
}
