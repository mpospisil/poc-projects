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
import { BaseTemplateConversion } from './baseTemplateConversion';

export class TemplateConversions {
    'conversions'?: Array<BaseTemplateConversion> | null;
    'countryCode'?: string | null;

    static discriminator: string | undefined = undefined;

    static attributeTypeMap: Array<{name: string, baseName: string, type: string}> = [
        {
            "name": "conversions",
            "baseName": "conversions",
            "type": "Array<BaseTemplateConversion>"
        },
        {
            "name": "countryCode",
            "baseName": "countryCode",
            "type": "string"
        }    ];

    static getAttributeTypeMap() {
        return TemplateConversions.attributeTypeMap;
    }
}

