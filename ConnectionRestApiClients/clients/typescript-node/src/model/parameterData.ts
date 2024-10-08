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
import { ValidationType } from './validationType';

export class ParameterData {
    'id'?: number;
    'identifier'?: string | null;
    'description'?: string | null;
    'parameterType'?: string | null;
    'value'?: any | null;
    'defaultValue'?: any | null;
    'evaluatedValue'?: any | null;
    'evaluatedDefaultValue'?: any | null;
    'validationValue'?: string | null;
    'evaluatedValidationValue'?: string | null;
    'validationType'?: ValidationType;
    'userUnitId'?: number;
    'isVisibleForSimpleConnection'?: boolean;

    static discriminator: string | undefined = undefined;

    static attributeTypeMap: Array<{name: string, baseName: string, type: string}> = [
        {
            "name": "id",
            "baseName": "id",
            "type": "number"
        },
        {
            "name": "identifier",
            "baseName": "identifier",
            "type": "string"
        },
        {
            "name": "description",
            "baseName": "description",
            "type": "string"
        },
        {
            "name": "parameterType",
            "baseName": "parameterType",
            "type": "string"
        },
        {
            "name": "value",
            "baseName": "value",
            "type": "any"
        },
        {
            "name": "defaultValue",
            "baseName": "defaultValue",
            "type": "any"
        },
        {
            "name": "evaluatedValue",
            "baseName": "evaluatedValue",
            "type": "any"
        },
        {
            "name": "evaluatedDefaultValue",
            "baseName": "evaluatedDefaultValue",
            "type": "any"
        },
        {
            "name": "validationValue",
            "baseName": "validationValue",
            "type": "string"
        },
        {
            "name": "evaluatedValidationValue",
            "baseName": "evaluatedValidationValue",
            "type": "string"
        },
        {
            "name": "validationType",
            "baseName": "validationType",
            "type": "ValidationType"
        },
        {
            "name": "userUnitId",
            "baseName": "userUnitId",
            "type": "number"
        },
        {
            "name": "isVisibleForSimpleConnection",
            "baseName": "isVisibleForSimpleConnection",
            "type": "boolean"
        }    ];

    static getAttributeTypeMap() {
        return ParameterData.attributeTypeMap;
    }
}

export namespace ParameterData {
}
