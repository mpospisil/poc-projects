import React from "react";
import { useSelector, useDispatch } from "react-redux";
import { ConProject, ConCalculationParameter, ConAnalysisTypeEnum} from 'connection-restapi-client-poc';
import { Scene } from "@ideastatica/scene/build/Types";
import { PresenterData } from '../models/presenterData';
import {
  setSceneData,
} from '../store/presenterSlice';

const ConnectionList: React.FC = () => {
  const projectData: ConProject | null = useSelector(
    (state: any) => state.project.projectData
  );

  const projectId: string | null  = useSelector(
    (state: any) => state.project.projectId
  );

  let clientId: string | null  = useSelector(
    (state: any) => state.project.clientId
  );

  const dispatch = useDispatch();

  const showHandler = (conId : number) => (event : any) => {
    if(projectId == null)
      {
        return;
      }

    const url = `http://localhost:5000/api/1/projects/${projectId}/connections/${conId}/presentation`;
    const reqHeaders = new Headers();
    reqHeaders.append('ClientId', clientId!);
    reqHeaders.append('Content-Type', 'application/json');

    const options = {
      headers: reqHeaders,
      method: 'GET',
    };
    const req = new Request(url, options); 

    fetch(req)
      .then(response => response.json())
      .then(data => {
        // Handle the response from the backend
        const sceneData : Scene = data;
        const presenterData : PresenterData = {
          sceneData : sceneData,
        };

        dispatch(setSceneData(presenterData));
        console.log(sceneData);
      })
      .catch(error => {
        // Handle any errors that occur during the request

        console.error(error);
      });
  }

  const calculateHandler = (conId : number) => (event : any) => {
    console.log('Button clicked with ID:', conId);

    if(projectId == null)
    {
      return;
    }

    const calcParam : any = {
      analysisType : " stress_Strain",
      connectionIds : [conId],
    };

    const reqHeaders = new Headers();
    reqHeaders.append('ClientId', clientId!);
    reqHeaders.append('Content-Type', 'application/json');

    const options = {
      headers: reqHeaders,
      method: 'POST',
      body: JSON.stringify(calcParam),
    };

    const url = `http://localhost:5000/api/1/projects/${projectId}/calculate`;
    const req = new Request(url, options); 

    fetch(req)
      .then(response => response.json())
      .then(data => {
        // Handle the response from the backend


        console.log(data);
      })
      .catch(error => {
        // Handle any errors that occur during the request

        console.error(error);
      });
  };


  if (projectData == null || projectData.connections == null) {
    return <div></div>;
  } else {
    return (
      <div className="ConnectionList">
        {projectData.connections.map((con, i) => (
          <li key={con.id} className="ConnectionListItem">
            {con.name}
            <button className="calc-con-button" onClick={calculateHandler(con.id!)}>Calculate</button>
            <button className="calc-con-button" onClick={showHandler(con.id!)}>Show</button>
          </li>
        ))}
      </div>
    );
  }
};

export default ConnectionList;
