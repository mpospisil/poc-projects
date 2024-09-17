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
* Message numbers
*/
export enum MessageNumber {
    Unspecified = <any> 'unspecified',
    Information = <any> 'information',
    Warning = <any> 'warning',
    WarnNoPropertyInData = <any> 'warnNoPropertyInData',
    WarnValueOutOfRange = <any> 'warnValueOutOfRange',
    WarnCurveCount = <any> 'warnCurveCount',
    WarnReinforcementBarsCollision = <any> 'warnReinforcementBarsCollision',
    Error = <any> 'error',
    ErrNoOpenObject = <any> 'errNoOpenObject',
    ErrDataObjectNotCreated = <any> 'errDataObjectNotCreated',
    ErrNoObjectInOpenModel = <any> 'errNoObjectInOpenModel',
    ErrNoReferenceObjectInOpenModel = <any> 'errNoReferenceObjectInOpenModel',
    ErrNoEquivalentObjectInDataModel = <any> 'errNoEquivalentObjectInDataModel',
    ErrNoCrossSectionParameter = <any> 'errNoCrossSectionParameter',
    ErrBoltsTooClose = <any> 'errBoltsTooClose',
    ErrBoltsTooCloseEdge = <any> 'errBoltsTooCloseEdge',
    ErrContactsAngle = <any> 'errContactsAngle',
    ErrIncorrentMaterialE = <any> 'errIncorrentMaterialE',
    ErrIncorrectMaterialEgp = <any> 'errIncorrectMaterialEGP',
    ErrPreloadedBoltGrade = <any> 'errPreloadedBoltGrade',
    ErrValueOutOfRange = <any> 'errValueOutOfRange',
    ErrCurveZeroPoint = <any> 'errCurveZeroPoint',
    ErrCurveFunction = <any> 'errCurveFunction',
    ErrCurveDecreaseFunction = <any> 'errCurveDecreaseFunction',
    ErrCurveDerivation = <any> 'errCurveDerivation',
    ErrCurveNotSet = <any> 'errCurveNotSet',
    ErrValidPolyline = <any> 'errValidPolyline',
    ErrWarningLoad = <any> 'errWarningLoad',
    ErrTimeout = <any> 'errTimeout',
    ErrNoInLibrary = <any> 'errNoInLibrary',
    ErrBadWeldMaterialProperty = <any> 'errBadWeldMaterialProperty',
    ErrOperation = <any> 'errOperation',
    Reserved = <any> 'reserved'
}
