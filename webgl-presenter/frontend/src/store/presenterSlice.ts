import { createSlice, PayloadAction } from '@reduxjs/toolkit';
import { PresenterData } from '../models/presenterData';
import { Scene } from "@ideastatica/scene/build/Types";

export  interface PresenterState {
    sceneData: Scene | null;
}

const initialState: PresenterState = {
    sceneData: null,
};

const presenterSlice = createSlice({
    name: 'presenter',
    initialState,
    reducers: {
        setSceneData: (state, action: PayloadAction<PresenterData | null>) => {
        state.sceneData = action?.payload?.sceneData!;
       }
    },
  });

  export const {
    setSceneData,
  } = presenterSlice.actions;
  
  export default presenterSlice.reducer;