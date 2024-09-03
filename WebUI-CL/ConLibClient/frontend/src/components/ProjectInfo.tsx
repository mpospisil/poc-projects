import React from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { OpenProjectResult } from '../models/conProjectInfo';
import { ConProject } from 'connection-restapi-client-poc';
import {
    close,
  } from '../store/conProjectSlice';

const ProjectInfo: React.FC = () => {
    let projectId : ConProject | null= useSelector((state: any) => state.project.projectId); 

    let clientId: string | null  = useSelector(
        (state: any) => state.project.clientId
    );

    const dispatch = useDispatch();

    const closeProjectHandler = (conId : number) => (event : any) => {
        const reqHeaders = new Headers();
        reqHeaders.append('ClientId', clientId!);
    
        const options = {
          headers: reqHeaders,
          method: 'GET',
        };

        // Pass init as an "options" object with our headers.
        const closeUrl = `/api/1/projects/${projectId}/close`;
        const req = new Request(closeUrl, options);  // URL is the URL of the image.  flowers.jpg is a placeholder.      

        const response2 = fetch(req)
        .then(response => response.json())
        .then(data => {
          // Handle the response from the backend
          const conData : ConProject = data;
          
          const closeProjRes : OpenProjectResult = {
            openClientId : null,
            openProjectId : null,
            projectInfo : null
          };

          dispatch(close(closeProjRes));
          console.log(data);
        })
        .catch(error => {
          // Handle any errors that occur during the request
          //dispatch(uploadFileFailure(error.message));
          console.error(error);
        });

    };

    let projectData : ConProject | null= useSelector((state: any) => state.project.projectData); 

        if(projectData == null)
        {
            return (<div></div>);
        }
        return (
            <div className="ProjectInfo">
                <div className="ProjectInfoRow">
                    <label>Project name :</label>
                    <label>{projectData.projectInfo?.name}</label>
                </div>
                <div className="ProjectInfoRow">
                    <label>Design code :</label>
                    <label>{projectData.projectInfo?.designCode}</label> 
                </div>
                <div className="ProjectInfoRow">
                    <button onClick={closeProjectHandler(1)}>Close</button>
                </div>                                  
            </div>
    );   
}

export default ProjectInfo;