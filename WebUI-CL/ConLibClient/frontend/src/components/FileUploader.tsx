import React, { ChangeEvent } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import {
  uploadFileSuccess,
  uploadFileFailure,
} from '../store/fileUploaderSlice';
import {
  open,
} from '../store/conProjectSlice';
import { OpenProjectResult } from '../models/conProjectInfo';
import { ConProject } from 'connection-restapi-client-poc';

const FileUploader: React.FC = () => {
  let selectedFile:Blob|null = null;
  const isLoading = useSelector((state: any) => state.fileUploader.isLoading);
  const error = useSelector((state: any) => state.fileUploader.error);
  
  const dispatch = useDispatch();

  const handleFileChange = (event: ChangeEvent<HTMLInputElement>) => {
    selectedFile = event.target.files?.[0] || null;
  };

  const handleUpload = () => {
      if(selectedFile === undefined)
      {
        return;
      }

      const formData = new FormData();
      formData.append('ideaConFile', selectedFile as Blob, 'connection.ideacon');

      // Send the formData to the backend using an API call (e.g., fetch or axios)
      // Replace 'http://example.com/upload' with the appropriate backend endpoint
      fetch('/api/1/connect-client', {
        method: 'GET',
      })
        .then(response => {
          if(!response.ok) {
            throw new Error('Network response was not ok');
          }

          return response.text();
        }).then(clientId => {
          const reqHeaders = new Headers();
          reqHeaders.append('ClientId', clientId);

          const options = {
            headers: reqHeaders,
            method: 'POST',
            body: formData,
          };

          // Pass init as an "options" object with our headers.
          const req = new Request('/api/1/projects/upload-ideacon', options);  // URL is the URL of the image.  flowers.jpg is a placeholder.      

          // Send the formData to the backend using an API call (e.g., fetch or axios)
          // Replace 'http://example.com/upload' with the appropriate backend endpoint
          const response2 = fetch(req)
          .then(response => response.json())
          .then(data => {
            // Handle the response from the backend
            const conData : ConProject = data;
            
            const openProjRes : OpenProjectResult = {
              openClientId : clientId,
              openProjectId : conData.projectId!,
              projectInfo : conData
            };
            //const openProjRes : OpenProjectResult = data;
            dispatch(uploadFileSuccess());
            dispatch(open(openProjRes));
            console.log(data);
          })
          .catch(error => {
            // Handle any errors that occur during the request
            dispatch(uploadFileFailure(error.message));
            console.error(error);
          });
        });
  };

  return (
    <div>
      <input type="file" onChange={handleFileChange}/>
      <button onClick={handleUpload} disabled={isLoading}>
        {isLoading ? 'Uploading...' : 'Upload'}
      </button>
      {error && <p>Error: {error}</p>}
    </div>
  );
};

export default FileUploader;
