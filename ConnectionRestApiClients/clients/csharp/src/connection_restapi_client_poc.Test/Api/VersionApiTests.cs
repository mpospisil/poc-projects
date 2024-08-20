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

namespace connection_restapi_client_poc.Test.Api
{
    /// <summary>
    ///  Class for testing VersionApi
    /// </summary>
    /// <remarks>
    /// This file is automatically generated by OpenAPI Generator (https://openapi-generator.tech).
    /// Please update the test case below to test the API endpoint.
    /// </remarks>
    public class VersionApiTests : IDisposable
    {
        private VersionApi instance;

        public VersionApiTests()
        {
            instance = new VersionApi();
        }

        public void Dispose()
        {
            // Cleanup when everything is done.
        }

        /// <summary>
        /// Test an instance of VersionApi
        /// </summary>
        [Fact]
        public void InstanceTest()
        {
            // TODO uncomment below to test 'IsType' VersionApi
            //Assert.IsType<VersionApi>(instance);
        }

        /// <summary>
        /// Test GetVersion
        /// </summary>
        [Fact]
        public void GetVersionTest()
        {
            // TODO uncomment below to test the method and replace null with proper value
            //var response = instance.GetVersion();
            //Assert.IsType<string>(response);
        }
    }
}
