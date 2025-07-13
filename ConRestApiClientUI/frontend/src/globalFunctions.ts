import store from './store'; // Import the Redux store
import { PresenterData } from './models/presenterData';
import { Scene } from "@ideastatica/scene/build/Types";

import {
  setSceneData,
} from './store/presenterSlice';

declare global {
    interface Window {
        scene3dPresenterApi: {
            PresentFunction: (data: string) => Promise<string>;
        };

    }
}

export const PresentFunction = async (data: string): Promise<string> => {
       const obj = JSON.parse(data);
      const scene : Scene = obj;

      const presenterData : PresenterData = {
        sceneData : scene,
      };

      store.dispatch(setSceneData(presenterData))


    return "OK";
};

// Make your TypeScript function globally accessible on a dedicated object
// This is crucial for C# to find and call it via ExecuteScriptAsync
window.scene3dPresenterApi = {
    PresentFunction: PresentFunction
};

