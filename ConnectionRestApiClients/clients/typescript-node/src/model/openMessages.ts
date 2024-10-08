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
import { OpenMessage } from './openMessage';

/**
* Open messages collection
*/
export class OpenMessages {
    /**
    * List of messages
    */
    'messages'?: Array<OpenMessage> | null;

    static discriminator: string | undefined = undefined;

    static attributeTypeMap: Array<{name: string, baseName: string, type: string}> = [
        {
            "name": "messages",
            "baseName": "messages",
            "type": "Array<OpenMessage>"
        }    ];

    static getAttributeTypeMap() {
        return OpenMessages.attributeTypeMap;
    }
}

