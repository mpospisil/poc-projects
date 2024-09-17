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
import { BucklingRes } from './bucklingRes';
import { CheckResAnchor } from './checkResAnchor';
import { CheckResBolt } from './checkResBolt';
import { CheckResConcreteBlock } from './checkResConcreteBlock';
import { CheckResPlate } from './checkResPlate';
import { CheckResSummary } from './checkResSummary';
import { CheckResWeld } from './checkResWeld';
import { OpenMessages } from './openMessages';

/**
* Results for connection in project
*/
export class ConnectionCheckRes {
    /**
    * List of CheckResSummary
    */
    'checkResSummary'?: Array<CheckResSummary> | null;
    /**
    * List of check results for plates
    */
    'checkResPlate'?: Array<CheckResPlate> | null;
    /**
    * List of check results for welds
    */
    'checkResWeld'?: Array<CheckResWeld> | null;
    /**
    * List of check results for bolts
    */
    'checkResBolt'?: Array<CheckResBolt> | null;
    /**
    * List of check results for anchors
    */
    'checkResAnchor'?: Array<CheckResAnchor> | null;
    /**
    * List of check results for concrete blocks
    */
    'checkResConcreteBlock'?: Array<CheckResConcreteBlock> | null;
    /**
    * List of results of buckling analysis
    */
    'bucklingResults'?: Array<BucklingRes> | null;
    /**
    * Name of connection
    */
    'name'?: string | null;
    /**
    * Guid of connection
    */
    'connectionID'?: string;
    /**
    * Integer Id of connection
    */
    'id'?: number;
    'messages'?: OpenMessages;

    static discriminator: string | undefined = undefined;

    static attributeTypeMap: Array<{name: string, baseName: string, type: string}> = [
        {
            "name": "checkResSummary",
            "baseName": "checkResSummary",
            "type": "Array<CheckResSummary>"
        },
        {
            "name": "checkResPlate",
            "baseName": "checkResPlate",
            "type": "Array<CheckResPlate>"
        },
        {
            "name": "checkResWeld",
            "baseName": "checkResWeld",
            "type": "Array<CheckResWeld>"
        },
        {
            "name": "checkResBolt",
            "baseName": "checkResBolt",
            "type": "Array<CheckResBolt>"
        },
        {
            "name": "checkResAnchor",
            "baseName": "checkResAnchor",
            "type": "Array<CheckResAnchor>"
        },
        {
            "name": "checkResConcreteBlock",
            "baseName": "checkResConcreteBlock",
            "type": "Array<CheckResConcreteBlock>"
        },
        {
            "name": "bucklingResults",
            "baseName": "bucklingResults",
            "type": "Array<BucklingRes>"
        },
        {
            "name": "name",
            "baseName": "name",
            "type": "string"
        },
        {
            "name": "connectionID",
            "baseName": "connectionID",
            "type": "string"
        },
        {
            "name": "id",
            "baseName": "id",
            "type": "number"
        },
        {
            "name": "messages",
            "baseName": "messages",
            "type": "OpenMessages"
        }    ];

    static getAttributeTypeMap() {
        return ConnectionCheckRes.attributeTypeMap;
    }
}

