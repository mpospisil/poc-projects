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
export declare class IdeaParameter {
    'key'?: string | null;
    'expression'?: string | null;
    'value'?: any | null;
    'unit'?: string | null;
    'parameterType'?: string | null;
    'validationExpression'?: string | null;
    'description'?: string | null;
    'validationStatus'?: string | null;
    'isVisible'?: boolean | null;
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
