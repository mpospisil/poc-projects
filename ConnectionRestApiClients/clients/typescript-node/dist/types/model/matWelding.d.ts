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
import { Polygon2D } from './polygon2D';
import { TemperatureCurve2D } from './temperatureCurve2D';
import { ThermalConductivityState } from './thermalConductivityState';
import { ThermalExpansionState } from './thermalExpansionState';
import { ThermalSpecificHeatState } from './thermalSpecificHeatState';
import { ThermalStrainState } from './thermalStrainState';
import { ThermalStressStrainState } from './thermalStressStrainState';
/**
* Welding material base class
*/
export declare class MatWelding {
    /**
    * Name of material
    */
    'name'?: string | null;
    /**
    * Load from library - try override properties from library find material by name
    */
    'loadFromLibrary'?: boolean;
    /**
    * Young\'s modulus
    */
    'e'?: number;
    /**
    * Shear modulus
    */
    'g'?: number;
    /**
    * Poisson\'s ratio
    */
    'poisson'?: number;
    /**
    * Unit weight
    */
    'unitMass'?: number;
    /**
    * Specific heat capacity
    */
    'specificHeat'?: number;
    /**
    * Thermal expansion
    */
    'thermalExpansion'?: number;
    /**
    * Thermal conductivity
    */
    'thermalConductivity'?: number;
    /**
    * True if material is default material from the code
    */
    'isDefaultMaterial'?: boolean;
    /**
    * Order of this material in the code
    */
    'orderInCode'?: number;
    'stateOfThermalExpansion'?: ThermalExpansionState;
    'stateOfThermalConductivity'?: ThermalConductivityState;
    'stateOfThermalSpecificHeat'?: ThermalSpecificHeatState;
    'stateOfThermalStressStrain'?: ThermalStressStrainState;
    'stateOfThermalStrain'?: ThermalStrainState;
    'userThermalSpecificHeatCurvature'?: Polygon2D;
    'userThermalConductivityCurvature'?: Polygon2D;
    'userThermalExpansionCurvature'?: Polygon2D;
    'userThermalStrainCurvature'?: Polygon2D;
    /**
    * User-defined curvature for thermal stress,strain { Temperature = Θ[K], {x = ε[-], y = σ[Pa]}}
    */
    'userThermalStressStrainCurvature'?: Array<TemperatureCurve2D> | null;
    /**
    * Element Id
    */
    'id'?: number;
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
export declare namespace MatWelding {
}
