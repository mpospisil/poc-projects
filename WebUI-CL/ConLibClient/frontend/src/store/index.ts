import { configureStore } from '@reduxjs/toolkit';
import fileUploaderReducer from './fileUploaderSlice';
import { FileUploaderState } from './fileUploaderSlice';
import { ProjectState}  from './conProjectSlice';
import { PresenterState } from './presenterSlice';
import presenterReducer from './presenterSlice';
import projectReducer from './conProjectSlice';

// Define your initial state interface
export interface AppState {
    fileUploader: FileUploaderState;
    project: ProjectState;
    presenter: PresenterState;
  }

// Define your initial state
const initialState: AppState = {
    fileUploader: {
        isLoading: false,
        error: null,
      },
      project : {
        clientId: null,
        projectId: null,
        projectData: null,
      },
      presenter : {
        sceneData: null,
      }
  }

// Define your reducer function
// Create the rootReducer
const rootReducer = {
    fileUploader: fileUploaderReducer, // Add this line to include the fileUploaderReducer
    project: projectReducer,
    presenter: presenterReducer
  };
  

// Create the Redux store
const store = configureStore({
  reducer: rootReducer,
  preloadedState: initialState, // Provide the initial state to the store
});

export default store;
