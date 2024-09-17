export * from './calculationApi';
import { CalculationApi } from './calculationApi';
export * from './clientApi';
import { ClientApi } from './clientApi';
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
export * from './operationApi';
import { OperationApi } from './operationApi';
export * from './parameterApi';
import { ParameterApi } from './parameterApi';
export * from './presentationApi';
import { PresentationApi } from './presentationApi';
export * from './projectApi';
import { ProjectApi } from './projectApi';
export * from './reportApi';
import { ReportApi } from './reportApi';
export * from './templateApi';
import { TemplateApi } from './templateApi';
import * as http from 'http';

export class HttpError extends Error {
    constructor (public response: http.IncomingMessage, public body: any, public statusCode?: number) {
        super('HTTP request failed');
        this.name = 'HttpError';
    }
}

export { RequestFile } from '../model/models';

export const APIS = [CalculationApi, ClientApi, ConnectionApi, ExportApi, LoadEffectApi, MaterialApi, MemberApi, OperationApi, ParameterApi, PresentationApi, ProjectApi, ReportApi, TemplateApi];
