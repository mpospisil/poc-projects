export * from './calculationApi';
import { CalculationApi } from './calculationApi';
export * from './connectionApi';
import { ConnectionApi } from './connectionApi';
export * from './exportApi';
import { ExportApi } from './exportApi';
export * from './loadEffectApi';
import { LoadEffectApi } from './loadEffectApi';
export * from './materialApi';
import { MaterialApi } from './materialApi';
export * from './memberApi';
import { MemberApi } from './memberApi';
export * from './parameterApi';
import { ParameterApi } from './parameterApi';
export * from './projectApi';
import { ProjectApi } from './projectApi';
export * from './reportApi';
import { ReportApi } from './reportApi';
export * from './templateApi';
import { TemplateApi } from './templateApi';
export * from './versionApi';
import { VersionApi } from './versionApi';
import * as http from 'http';

export class HttpError extends Error {
    constructor (public response: http.IncomingMessage, public body: any, public statusCode?: number) {
        super('HTTP request failed');
        this.name = 'HttpError';
    }
}

export { RequestFile } from '../model/models';

export const APIS = [CalculationApi, ConnectionApi, ExportApi, LoadEffectApi, MaterialApi, MemberApi, ParameterApi, ProjectApi, ReportApi, TemplateApi, VersionApi];
