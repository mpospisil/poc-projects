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

/**
* enum of weld types
*/
export enum WeldType {
    NotSpecified = <any> 'notSpecified',
    Fillet = <any> 'fillet',
    DoubleFillet = <any> 'doubleFillet',
    Bevel = <any> 'bevel',
    Pjp = <any> 'pjp',
    PjpRear = <any> 'pjpRear',
    LengthAtHaunch = <any> 'lengthAtHaunch',
    FilletRear = <any> 'filletRear',
    Contact = <any> 'contact',
    Intermittent = <any> 'intermittent'
}
