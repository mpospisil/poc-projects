import React from "react";
import { useSelector } from "react-redux";
import ProjectInfo from "./ProjectInfo";
import ConnectionList from "./ConnectionList";
import { ConProject } from 'connection-restapi-client-poc';


const ProjectContent: React.FC = () => {
  let projectData: ConProject | null = useSelector(
    (state: any) => state.project.projectData
  );

  if (projectData == null) {
    return (
      <div>
        <h1>Not loaded</h1>
      </div>
    );
  } else {
    return (
      <div>
        <ProjectInfo />
        <div>
          <label>Connections :</label>
        </div>
        <ConnectionList />
      </div>
    );
  }
};

export default ProjectContent;
