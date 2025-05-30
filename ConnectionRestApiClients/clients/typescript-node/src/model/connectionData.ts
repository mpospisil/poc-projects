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
import { AnchorGrid } from './anchorGrid';
import { BeamData } from './beamData';
import { BoltGrid } from './boltGrid';
import { ConcreteBlockData } from './concreteBlockData';
import { CutBeamByBeamData } from './cutBeamByBeamData';
import { FoldedPlateData } from './foldedPlateData';
import { PinGrid } from './pinGrid';
import { PlateData } from './plateData';
import { ReferenceElement } from './referenceElement';
import { WeldData } from './weldData';

/**
* Provides data of the connection
*/
export class ConnectionData {
    'connectionPoint'?: ReferenceElement;
    /**
    * Connected beams
    */
    'beams'?: Array<BeamData> | null;
    /**
    * Plates of the connection
    */
    'plates'?: Array<PlateData> | null;
    /**
    * Folded plate of the connection
    */
    'foldedPlates'?: Array<FoldedPlateData> | null;
    /**
    * Bolt grids which belongs to the connection
    */
    'boltGrids'?: Array<BoltGrid> | null;
    /**
    * Anchor grids which belongs to the connection
    */
    'anchorGrids'?: Array<AnchorGrid> | null;
    /**
    * Pin grids which belongs to the connection
    */
    'pinGrids'?: Array<PinGrid> | null;
    /**
    * Welds of the connection
    */
    'welds'?: Array<WeldData> | null;
    /**
    * ConcreteBlocksof the connection
    */
    'concreteBlocks'?: Array<ConcreteBlockData> | null;
    /**
    * cut beam by beams
    */
    'cutBeamByBeams'?: Array<CutBeamByBeamData> | null;

    static discriminator: string | undefined = undefined;

    static attributeTypeMap: Array<{name: string, baseName: string, type: string}> = [
        {
            "name": "connectionPoint",
            "baseName": "connectionPoint",
            "type": "ReferenceElement"
        },
        {
            "name": "beams",
            "baseName": "beams",
            "type": "Array<BeamData>"
        },
        {
            "name": "plates",
            "baseName": "plates",
            "type": "Array<PlateData>"
        },
        {
            "name": "foldedPlates",
            "baseName": "foldedPlates",
            "type": "Array<FoldedPlateData>"
        },
        {
            "name": "boltGrids",
            "baseName": "boltGrids",
            "type": "Array<BoltGrid>"
        },
        {
            "name": "anchorGrids",
            "baseName": "anchorGrids",
            "type": "Array<AnchorGrid>"
        },
        {
            "name": "pinGrids",
            "baseName": "pinGrids",
            "type": "Array<PinGrid>"
        },
        {
            "name": "welds",
            "baseName": "welds",
            "type": "Array<WeldData>"
        },
        {
            "name": "concreteBlocks",
            "baseName": "concreteBlocks",
            "type": "Array<ConcreteBlockData>"
        },
        {
            "name": "cutBeamByBeams",
            "baseName": "cutBeamByBeams",
            "type": "Array<CutBeamByBeamData>"
        }    ];

    static getAttributeTypeMap() {
        return ConnectionData.attributeTypeMap;
    }
}

