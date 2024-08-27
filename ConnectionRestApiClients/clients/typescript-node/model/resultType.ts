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
* Type of results
*/
export enum ResultType {
    InternalForces = <any> 'internalForces',
    Deformation = <any> 'deformation',
    CrossSectionNla = <any> 'crossSectionNLA',
    CrossSectionTa = <any> 'crossSectionTA',
    InteractionDiagram = <any> 'interactionDiagram',
    CrossSectionMesh = <any> 'crossSectionMesh'
}
