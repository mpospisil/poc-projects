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
import { ConcreteSetup } from './concreteSetup';
import { ConeBreakoutCheckType } from './coneBreakoutCheckType';
import { CrtCompCheckIS } from './crtCompCheckIS';
import { WeldEvaluation } from './weldEvaluation';

/**
* ConnectionSetup
*/
export class ConnectionSetup {
    /**
    * ISteelSetup
    */
    'steelSetup'?: object;
    'concreteSetup'?: ConcreteSetup;
    /**
    * Stop analysis when the limit strain is reached.
    */
    'stopAtLimitStrain'?: boolean;
    'weldEvaluationData'?: WeldEvaluation;
    /**
    * Perform check of bolt positions
    */
    'checkDetailing'?: boolean;
    'applyConeBreakoutCheck'?: ConeBreakoutCheckType;
    /**
    * Pretension force fpc = k * fub * As
    */
    'pretensionForceFpc'?: number;
    /**
    * Partial safety factor of instalation safety
    */
    'gammaInst'?: number;
    /**
    * Partial safety factor of concrete
    */
    'gammaC'?: number;
    /**
    * Preloaded bolts safety factor
    */
    'gammaM3'?: number;
    /**
    * Length of anchor to define the anchor stiffness in analysis model, as a multiple of anchor diameter (E A /n * [d])
    */
    'anchorLengthForStiffness'?: number;
    /**
    * Joint coefficient βj - Used for Fjd calculation
    */
    'jointBetaFactor'?: number;
    /**
    * Effective area is taken from intersection of stress area and area of joined items according to EN1993-1-8 art. 6.2.5
    */
    'effectiveAreaStressCoeff'?: number;
    /**
    * Effective area stress coefficient - Concrete loaded area: Stress cut-off is set for AISC
    */
    'effectiveAreaStressCoeffAISC'?: number;
    /**
    * Coefficient of friction between base plate and concrete block
    */
    'frictionCoefficient'?: number;
    /**
    * Limit of plastic strain used in 2D plate element check
    */
    'limitPlasticStrain'?: number;
    /**
    * Limit deformation on closed sections
    */
    'limitDeformation'?: number;
    /**
    * Limit deformation on closed sections check or not
    */
    'limitDeformationCheck'?: boolean;
    /**
    * Analysis with GNL
    */
    'analysisGNL'?: boolean;
    /**
    * Analysis with All GNL
    */
    'analysisAllGNL'?: boolean;
    /**
    * Warning plastic strain
    */
    'warnPlasticStrain'?: number;
    /**
    * Warning check level
    */
    'warnCheckLevel'?: number;
    /**
    * Optimal check level
    */
    'optimalCheckLevel'?: number;
    /**
    * Limit distance between bolts as a multiple of bolt diameter
    */
    'distanceBetweenBolts'?: number;
    /**
    * Anchor pitch
    */
    'distanceDiameterBetweenBP'?: number;
    /**
    * Limit distance between bolt and plate edge as a multiple of bolt diameter
    */
    'distanceBetweenBoltsEdge'?: number;
    /**
    * Load distribution angle of concrete block in calculation of factor Kj
    */
    'bearingAngle'?: number;
    /**
    * Decreasing Ftrd of anchors. Worse quality influence
    */
    'decreasingFtrd'?: number;
    /**
    * Consider the frame system as braced for stiffness calculation. Braced system reduces horizontal displacements.
    */
    'bracedSystem'?: boolean;
    /**
    * Apply bearing check including αb
    */
    'bearingCheck'?: boolean;
    /**
    * Apply βp influence in bolt shear resistance. ΕΝ 1993-1-8 chapter 3.6.1 (12)
    */
    'applyBetapInfluence'?: boolean;
    /**
    * A multiple of cross-section height to determine the default length of member
    */
    'memberLengthRatio'?: number;
    /**
    * Number of straight lines to substitute circle of circular tube in analysis model
    */
    'divisionOfSurfaceOfCHS'?: number;
    /**
    * Number of straight lines to substitute corner arc of rectangular tubes in analysis model
    */
    'divisionOfArcsOfRHS'?: number;
    /**
    * Ratio of length of decisive plate edge and Elements on edge count determines the average size of mesh element
    */
    'numElement'?: number;
    /**
    * More iterations helps to find better solutions in contact elements but increases calculation time
    */
    'numberIterations'?: number;
    /**
    * Number of iteration steps to evaluate analysis divergence
    */
    'mdiv'?: number;
    /**
    * Minimal size of generated finite mesh element
    */
    'minSize'?: number;
    /**
    * Maximal size of generated finite mesh element
    */
    'maxSize'?: number;
    /**
    * Number of mesh elements in RHS height
    */
    'numElementRhs'?: number;
    /**
    * Number of mesh elements on plates
    */
    'numElementPlate'?: number;
    /**
    * True if rigid base plate is considered
    */
    'rigidBP'?: boolean;
    /**
    * Long-term effect on fcd
    */
    'alphaCC'?: number;
    /**
    * True if cracked concrete is considered
    */
    'crackedConcrete'?: boolean;
    /**
    * True if developed fillers is considered
    */
    'developedFillers'?: boolean;
    /**
    * True if bolt hole deformation is considered
    */
    'deformationBoltHole'?: boolean;
    /**
    * ExtensionLengthRationOpenSections
    */
    'extensionLengthRationOpenSections'?: number;
    /**
    * ExtensionLengthRationCloseSections
    */
    'extensionLengthRationCloseSections'?: number;
    /**
    * FactorPreloadBolt
    */
    'factorPreloadBolt'?: number;
    /**
    * BaseMetalCapacity
    */
    'baseMetalCapacity'?: boolean;
    /**
    * ApplyBearingCheck
    */
    'applyBearingCheck'?: boolean;
    /**
    * Friction factor of slip-resistant joint
    */
    'frictionCoefficientPbolt'?: number;
    'crtCompCheckIS'?: CrtCompCheckIS;
    /**
    * Max value of bolt grip
    */
    'boltMaxGripLengthCoeff'?: number;
    /**
    * Fatigue section Offset = FatigueSectionOffset x Legsize
    */
    'fatigueSectionOffset'?: number;
    /**
    * Condensed element length factor (CEF). Condensed beam legth = maxCssSize * CEF
    */
    'condensedElementLengthFactor'?: number;
    /**
    * Partial safety factor for Horizontal tying
    */
    'gammaMu'?: number;
    /**
    * Limit plastic strain for high strength steel
    */
    'hssLimitPlasticStrain'?: number;

    static discriminator: string | undefined = undefined;

    static attributeTypeMap: Array<{name: string, baseName: string, type: string}> = [
        {
            "name": "steelSetup",
            "baseName": "steelSetup",
            "type": "object"
        },
        {
            "name": "concreteSetup",
            "baseName": "concreteSetup",
            "type": "ConcreteSetup"
        },
        {
            "name": "stopAtLimitStrain",
            "baseName": "stopAtLimitStrain",
            "type": "boolean"
        },
        {
            "name": "weldEvaluationData",
            "baseName": "weldEvaluationData",
            "type": "WeldEvaluation"
        },
        {
            "name": "checkDetailing",
            "baseName": "checkDetailing",
            "type": "boolean"
        },
        {
            "name": "applyConeBreakoutCheck",
            "baseName": "applyConeBreakoutCheck",
            "type": "ConeBreakoutCheckType"
        },
        {
            "name": "pretensionForceFpc",
            "baseName": "pretensionForceFpc",
            "type": "number"
        },
        {
            "name": "gammaInst",
            "baseName": "gammaInst",
            "type": "number"
        },
        {
            "name": "gammaC",
            "baseName": "gammaC",
            "type": "number"
        },
        {
            "name": "gammaM3",
            "baseName": "gammaM3",
            "type": "number"
        },
        {
            "name": "anchorLengthForStiffness",
            "baseName": "anchorLengthForStiffness",
            "type": "number"
        },
        {
            "name": "jointBetaFactor",
            "baseName": "jointBetaFactor",
            "type": "number"
        },
        {
            "name": "effectiveAreaStressCoeff",
            "baseName": "effectiveAreaStressCoeff",
            "type": "number"
        },
        {
            "name": "effectiveAreaStressCoeffAISC",
            "baseName": "effectiveAreaStressCoeffAISC",
            "type": "number"
        },
        {
            "name": "frictionCoefficient",
            "baseName": "frictionCoefficient",
            "type": "number"
        },
        {
            "name": "limitPlasticStrain",
            "baseName": "limitPlasticStrain",
            "type": "number"
        },
        {
            "name": "limitDeformation",
            "baseName": "limitDeformation",
            "type": "number"
        },
        {
            "name": "limitDeformationCheck",
            "baseName": "limitDeformationCheck",
            "type": "boolean"
        },
        {
            "name": "analysisGNL",
            "baseName": "analysisGNL",
            "type": "boolean"
        },
        {
            "name": "analysisAllGNL",
            "baseName": "analysisAllGNL",
            "type": "boolean"
        },
        {
            "name": "warnPlasticStrain",
            "baseName": "warnPlasticStrain",
            "type": "number"
        },
        {
            "name": "warnCheckLevel",
            "baseName": "warnCheckLevel",
            "type": "number"
        },
        {
            "name": "optimalCheckLevel",
            "baseName": "optimalCheckLevel",
            "type": "number"
        },
        {
            "name": "distanceBetweenBolts",
            "baseName": "distanceBetweenBolts",
            "type": "number"
        },
        {
            "name": "distanceDiameterBetweenBP",
            "baseName": "distanceDiameterBetweenBP",
            "type": "number"
        },
        {
            "name": "distanceBetweenBoltsEdge",
            "baseName": "distanceBetweenBoltsEdge",
            "type": "number"
        },
        {
            "name": "bearingAngle",
            "baseName": "bearingAngle",
            "type": "number"
        },
        {
            "name": "decreasingFtrd",
            "baseName": "decreasingFtrd",
            "type": "number"
        },
        {
            "name": "bracedSystem",
            "baseName": "bracedSystem",
            "type": "boolean"
        },
        {
            "name": "bearingCheck",
            "baseName": "bearingCheck",
            "type": "boolean"
        },
        {
            "name": "applyBetapInfluence",
            "baseName": "applyBetapInfluence",
            "type": "boolean"
        },
        {
            "name": "memberLengthRatio",
            "baseName": "memberLengthRatio",
            "type": "number"
        },
        {
            "name": "divisionOfSurfaceOfCHS",
            "baseName": "divisionOfSurfaceOfCHS",
            "type": "number"
        },
        {
            "name": "divisionOfArcsOfRHS",
            "baseName": "divisionOfArcsOfRHS",
            "type": "number"
        },
        {
            "name": "numElement",
            "baseName": "numElement",
            "type": "number"
        },
        {
            "name": "numberIterations",
            "baseName": "numberIterations",
            "type": "number"
        },
        {
            "name": "mdiv",
            "baseName": "mdiv",
            "type": "number"
        },
        {
            "name": "minSize",
            "baseName": "minSize",
            "type": "number"
        },
        {
            "name": "maxSize",
            "baseName": "maxSize",
            "type": "number"
        },
        {
            "name": "numElementRhs",
            "baseName": "numElementRhs",
            "type": "number"
        },
        {
            "name": "numElementPlate",
            "baseName": "numElementPlate",
            "type": "number"
        },
        {
            "name": "rigidBP",
            "baseName": "rigidBP",
            "type": "boolean"
        },
        {
            "name": "alphaCC",
            "baseName": "alphaCC",
            "type": "number"
        },
        {
            "name": "crackedConcrete",
            "baseName": "crackedConcrete",
            "type": "boolean"
        },
        {
            "name": "developedFillers",
            "baseName": "developedFillers",
            "type": "boolean"
        },
        {
            "name": "deformationBoltHole",
            "baseName": "deformationBoltHole",
            "type": "boolean"
        },
        {
            "name": "extensionLengthRationOpenSections",
            "baseName": "extensionLengthRationOpenSections",
            "type": "number"
        },
        {
            "name": "extensionLengthRationCloseSections",
            "baseName": "extensionLengthRationCloseSections",
            "type": "number"
        },
        {
            "name": "factorPreloadBolt",
            "baseName": "factorPreloadBolt",
            "type": "number"
        },
        {
            "name": "baseMetalCapacity",
            "baseName": "baseMetalCapacity",
            "type": "boolean"
        },
        {
            "name": "applyBearingCheck",
            "baseName": "applyBearingCheck",
            "type": "boolean"
        },
        {
            "name": "frictionCoefficientPbolt",
            "baseName": "frictionCoefficientPbolt",
            "type": "number"
        },
        {
            "name": "crtCompCheckIS",
            "baseName": "crtCompCheckIS",
            "type": "CrtCompCheckIS"
        },
        {
            "name": "boltMaxGripLengthCoeff",
            "baseName": "boltMaxGripLengthCoeff",
            "type": "number"
        },
        {
            "name": "fatigueSectionOffset",
            "baseName": "fatigueSectionOffset",
            "type": "number"
        },
        {
            "name": "condensedElementLengthFactor",
            "baseName": "condensedElementLengthFactor",
            "type": "number"
        },
        {
            "name": "gammaMu",
            "baseName": "gammaMu",
            "type": "number"
        },
        {
            "name": "hssLimitPlasticStrain",
            "baseName": "hssLimitPlasticStrain",
            "type": "number"
        }    ];

    static getAttributeTypeMap() {
        return ConnectionSetup.attributeTypeMap;
    }
}

export namespace ConnectionSetup {
}
