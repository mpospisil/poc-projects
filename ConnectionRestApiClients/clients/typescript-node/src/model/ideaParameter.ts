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
import { IdeaParameterValidation } from './ideaParameterValidation';

export class IdeaParameter {
    'key'?: string | null;
    'expression'?: string | null;
    'value'?: any | null;
    'unit'?: string | null;
    'parameterType'?: string | null;
    'validationExpression'?: string | null;
    'description'?: string | null;
    'validationStatus'?: string | null;
    'isVisible'?: boolean | null;
    'lowerBound'?: string | null;
    'upperBound'?: string | null;
    'parameterValidation'?: IdeaParameterValidation;

    static discriminator: string | undefined = undefined;

    static attributeTypeMap: Array<{name: string, baseName: string, type: string}> = [
        {
            "name": "key",
            "baseName": "key",
            "type": "string"
        },
        {
            "name": "expression",
            "baseName": "expression",
            "type": "string"
        },
        {
            "name": "value",
            "baseName": "value",
            "type": "any"
        },
        {
            "name": "unit",
            "baseName": "unit",
            "type": "string"
        },
        {
            "name": "parameterType",
            "baseName": "parameterType",
            "type": "string"
        },
        {
            "name": "validationExpression",
            "baseName": "validationExpression",
            "type": "string"
        },
        {
            "name": "description",
            "baseName": "description",
            "type": "string"
        },
        {
            "name": "validationStatus",
            "baseName": "validationStatus",
            "type": "string"
        },
        {
            "name": "isVisible",
            "baseName": "isVisible",
            "type": "boolean"
        },
        {
            "name": "lowerBound",
            "baseName": "lowerBound",
            "type": "string"
        },
        {
            "name": "upperBound",
            "baseName": "upperBound",
            "type": "string"
        },
        {
            "name": "parameterValidation",
            "baseName": "parameterValidation",
            "type": "IdeaParameterValidation"
        }    ];

    static getAttributeTypeMap() {
        return IdeaParameter.attributeTypeMap;
    }
}

