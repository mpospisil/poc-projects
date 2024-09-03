import { createSlice, PayloadAction } from '@reduxjs/toolkit';
import { OpenProjectResult} from '../models/conProjectInfo';
import { ConProject } from 'connection-restapi-client-poc';

export  interface ProjectState {
    clientId: string | null;
    projectId: string | null;
    projectData: ConProject | null;
}

const initialState: ProjectState = {
    clientId: null,
    projectId : null,
    projectData : null,
  };

const conProjectSlice = createSlice({
    name: 'conProject',
    initialState,
    reducers: {
      open: (state, action: PayloadAction<OpenProjectResult | null>) => {
        state.clientId = action?.payload?.openClientId!;
        state.projectId = action?.payload?.openProjectId!;
        state.projectData = action?.payload?.projectInfo!;
       },
       close: (state, action: PayloadAction<OpenProjectResult | null>) => {
        state.clientId = null;
        state.projectId = null;
        state.projectData = null;
       }
    },
  });

  export const {
    open,
    close,
  } = conProjectSlice.actions;
  
  export default conProjectSlice.reducer;