/*
 * Connection Rest API 1.0
 *
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 1.0
 * Generated by: https://github.com/openapitools/openapi-generator.git
 */

using System;
using System.IO;
using System.Collections.Generic;
using System.Collections.ObjectModel;
using System.Linq;
using System.Reflection;
using RestSharp;
using Xunit;

using connection_restapi_client_poc.Client;
using connection_restapi_client_poc.Api;
// uncomment below to import models
//using connection_restapi_client_poc.Model;

namespace connection_restapi_client_poc.Test.Api
{
    /// <summary>
    ///  Class for testing ReportApi
    /// </summary>
    /// <remarks>
    /// This file is automatically generated by OpenAPI Generator (https://openapi-generator.tech).
    /// Please update the test case below to test the API endpoint.
    /// </remarks>
    public class ReportApiTests : IDisposable
    {
        private ReportApi instance;

        public ReportApiTests()
        {
            instance = new ReportApi();
        }

        public void Dispose()
        {
            // Cleanup when everything is done.
        }

        /// <summary>
        /// Test an instance of ReportApi
        /// </summary>
        [Fact]
        public void InstanceTest()
        {
            // TODO uncomment below to test 'IsType' ReportApi
            //Assert.IsType<ReportApi>(instance);
        }

        /// <summary>
        /// Test Api1ProjectsProjectIdReportsConnectionIdPdfGet
        /// </summary>
        [Fact]
        public void Api1ProjectsProjectIdReportsConnectionIdPdfGetTest()
        {
            // TODO uncomment below to test the method and replace null with proper value
            //Guid projectId = null;
            //int connectionId = null;
            //Object? body = null;
            //var response = instance.Api1ProjectsProjectIdReportsConnectionIdPdfGet(projectId, connectionId, body);
            //Assert.IsType<Stream>(response);
        }

        /// <summary>
        /// Test Api1ProjectsProjectIdReportsConnectionIdWordGet
        /// </summary>
        [Fact]
        public void Api1ProjectsProjectIdReportsConnectionIdWordGetTest()
        {
            // TODO uncomment below to test the method and replace null with proper value
            //Guid projectId = null;
            //int connectionId = null;
            //Object? body = null;
            //var response = instance.Api1ProjectsProjectIdReportsConnectionIdWordGet(projectId, connectionId, body);
            //Assert.IsType<Stream>(response);
        }
    }
}
