"use strict";
var __createBinding = (this && this.__createBinding) || (Object.create ? (function(o, m, k, k2) {
    if (k2 === undefined) k2 = k;
    var desc = Object.getOwnPropertyDescriptor(m, k);
    if (!desc || ("get" in desc ? !m.__esModule : desc.writable || desc.configurable)) {
      desc = { enumerable: true, get: function() { return m[k]; } };
    }
    Object.defineProperty(o, k2, desc);
}) : (function(o, m, k, k2) {
    if (k2 === undefined) k2 = k;
    o[k2] = m[k];
}));
var __exportStar = (this && this.__exportStar) || function(m, exports) {
    for (var p in m) if (p !== "default" && !Object.prototype.hasOwnProperty.call(exports, p)) __createBinding(exports, m, p);
};
Object.defineProperty(exports, "__esModule", { value: true });
exports.APIS = exports.HttpError = void 0;
__exportStar(require("./calculationApi"), exports);
const calculationApi_1 = require("./calculationApi");
__exportStar(require("./connectionApi"), exports);
const connectionApi_1 = require("./connectionApi");
__exportStar(require("./exportApi"), exports);
const exportApi_1 = require("./exportApi");
__exportStar(require("./loadEffectApi"), exports);
const loadEffectApi_1 = require("./loadEffectApi");
__exportStar(require("./materialApi"), exports);
const materialApi_1 = require("./materialApi");
__exportStar(require("./memberApi"), exports);
const memberApi_1 = require("./memberApi");
__exportStar(require("./parameterApi"), exports);
const parameterApi_1 = require("./parameterApi");
__exportStar(require("./presentationApi"), exports);
const presentationApi_1 = require("./presentationApi");
__exportStar(require("./projectApi"), exports);
const projectApi_1 = require("./projectApi");
__exportStar(require("./reportApi"), exports);
const reportApi_1 = require("./reportApi");
__exportStar(require("./templateApi"), exports);
const templateApi_1 = require("./templateApi");
__exportStar(require("./versionApi"), exports);
const versionApi_1 = require("./versionApi");
class HttpError extends Error {
    constructor(response, body, statusCode) {
        super('HTTP request failed');
        this.response = response;
        this.body = body;
        this.statusCode = statusCode;
        this.name = 'HttpError';
    }
}
exports.HttpError = HttpError;
exports.APIS = [calculationApi_1.CalculationApi, connectionApi_1.ConnectionApi, exportApi_1.ExportApi, loadEffectApi_1.LoadEffectApi, materialApi_1.MaterialApi, memberApi_1.MemberApi, parameterApi_1.ParameterApi, presentationApi_1.PresentationApi, projectApi_1.ProjectApi, reportApi_1.ReportApi, templateApi_1.TemplateApi, versionApi_1.VersionApi];
