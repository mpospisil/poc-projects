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
    ///  Class for testing OperationApi
    /// </summary>
    /// <remarks>
    /// This file is automatically generated by OpenAPI Generator (https://openapi-generator.tech).
    /// Please update the test case below to test the API endpoint.
    /// </remarks>
    public class OperationApiTests : IDisposable
    {
        private OperationApi instance;

        public OperationApiTests()
        {
            instance = new OperationApi();
        }

        public void Dispose()
        {
            // Cleanup when everything is done.
        }

        /// <summary>
        /// Test an instance of OperationApi
        /// </summary>
        [Fact]
        public void InstanceTest()
        {
            // TODO uncomment below to test 'IsType' OperationApi
            //Assert.IsType<OperationApi>(instance);
        }

        /// <summary>
        /// Test DeleteOperations
        /// </summary>
        [Fact]
        public void DeleteOperationsTest()
        {
            // TODO uncomment below to test the method and replace null with proper value
            //Guid projectId = null;
            //int connectionId = null;
            //instance.DeleteOperations(projectId, connectionId);
        }

        /// <summary>
        /// Test GetOperations
        /// </summary>
        [Fact]
        public void GetOperationsTest()
        {
            // TODO uncomment below to test the method and replace null with proper value
            //Guid projectId = null;
            //int connectionId = null;
            //var response = instance.GetOperations(projectId, connectionId);
            //Assert.IsType<List<ConOperation>>(response);
        }
    }
}