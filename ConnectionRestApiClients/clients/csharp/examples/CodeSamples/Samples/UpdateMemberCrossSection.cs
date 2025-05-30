﻿using IdeaRS.OpenModel.Material;
using IdeaStatiCa.ConnectionApi;
using IdeaStatiCa.ConnectionApi.Model;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using static System.Collections.Specialized.BitVector32;

namespace CodeSamples
{
    public partial class ClientExamples
    {
        public static async Task UpdateMemberCrossSection(ConnectionApiClient conClient)
        {
            string filePath = "Inputs/simple cleat connection - sections.ideaCon";
            ConProject conProject = await conClient.Project.OpenProjectAsync(filePath);

            //Get projectId Guid
            Guid projectId = conProject.ProjectId;

            //Get First Connection
            var connections = await conClient.Connection.GetAllConnectionsDataAsync(projectId);
            int connectionId = connections[0].Id;

            //Create map of CrossSections and Materials.
            Dictionary<string, int> CrossSectionMap = new Dictionary<string, int>();

            //Get the cross-sections in the project.
            List<IdeaRS.OpenModel.CrossSection.CrossSection> crossSections = (await conClient.Material.GetCrossSectionsAsync(projectId)).Cast<IdeaRS.OpenModel.CrossSection.CrossSection>().ToList();
            crossSections.ForEach(x => CrossSectionMap.Add(x.Name, x.Id));

            Console.WriteLine("List of avaliable cross-sections in the project:");
            foreach (var css in crossSections)
            {
                Console.WriteLine($"({css.Id}) {css.Name}");
            }

            //Get Member Information.
            List<ConMember> members = await conClient.Member.GetAllMemberDataAsync(projectId, connectionId);

            foreach (var member in members)
            {
                Console.WriteLine($"{member.Name} ({member.Id}) has section size of {CrossSectionMap.FirstOrDefault(x => x.Value == member.Id).Key} {(member.IsBearing ? "and is the Bearing Member" : "")}");
            }

            bool found = false;
            int memberId = 0;
            while (!found)
            {
                Console.WriteLine("Select which member (by Id) to change cross-section:");
                string intput = Console.ReadLine();

                if (int.TryParse(intput, out memberId))
                {
                    if (members.Select(x => x.Id).Contains(memberId))
                    {
                        found = true;
                        break;
                    }
                }
                Console.WriteLine("Member not found provide valid Id");
            }

            bool foundCss = false;
            int cssId = 0;
            while (!foundCss)
            {
                Console.WriteLine($"Select which cross-section to apply to Member {memberId}");
                string intput = Console.ReadLine();
                if (int.TryParse(intput, out cssId))
                {
                    if (crossSections.Select(x => x.Id).Contains(cssId))
                    {
                        found = true;
                        break;
                    }
                }
                Console.WriteLine("Cross-section not found. Provide valid cross-section Id");
            }

            //Get the member with the provided MemberId.
            ConMember conMember = members.FirstOrDefault(x=> x.Id == memberId);
            conMember.CrossSectionId = cssId;

            //Update the member.
            var updatedMember = await conClient.Member.UpdateMemberAsync(projectId, connectionId, memberId, conMember);

            //Get Member Information again.
            members = await conClient.Member.GetAllMemberDataAsync(projectId, connectionId);

            foreach (var member in members)
            {
                Console.WriteLine($"{member.Name} ({member.Id}) has section size of {CrossSectionMap.FirstOrDefault(x => x.Value == member.CrossSectionId).Key} {(member.IsBearing ? "and is the Bearing Member" : "")}");
            }

            string exampleFolder = GetExampleFolderPathOnDesktop("UpdateMemberCrossSection");
            string fileName = "simple cleat - member update.ideaCon";
            string saveFilePath = Path.Combine(exampleFolder, fileName);

            //Save the applied template
            await conClient.Project.SaveProjectAsync(projectId, saveFilePath);
            Console.WriteLine("Project saved to: " + saveFilePath);

            await conClient.Project.CloseProjectAsync(projectId.ToString());
        }
    }
}
