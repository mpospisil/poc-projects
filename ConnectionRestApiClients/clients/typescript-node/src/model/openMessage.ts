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
import { MessageNumber } from './messageNumber';

/**
* Open message base class
*/
export class OpenMessage {
    'number'?: MessageNumber;
    /**
    * Description of message
    */
    'description'?: string | null;

    static discriminator: string | undefined = undefined;

    static attributeTypeMap: Array<{name: string, baseName: string, type: string}> = [
        {
            "name": "number",
            "baseName": "number",
            "type": "MessageNumber"
        },
        {
            "name": "description",
            "baseName": "description",
            "type": "string"
        }    ];

    static getAttributeTypeMap() {
        return OpenMessage.attributeTypeMap;
    }
}

export namespace OpenMessage {
}
