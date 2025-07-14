import store from './store'; // Import the Redux store
import { PresenterData } from './models/presenterData';
import { Scene } from "@ideastatica/scene/build/Types";
import html2canvas from 'html2canvas';

import {
  setSceneData,
} from './store/presenterSlice';

declare global {
    interface Window {
        scene3dPresenterApi: {
            PresentFunction: (data: string) => Promise<string>;
            CaptureDivAsImage: (divId: string) => Promise<string | null>;
        };
    }
}

export const PresentFunction = async (data: string): Promise<string> => {
      if(data === undefined || data === null || data === "") {
        store.dispatch(setSceneData(null));
      }
      else {
        const obj = JSON.parse(data);
        const scene : Scene = obj;

        const presenterData : PresenterData = {
          sceneData : scene,
        };

        store.dispatch(setSceneData(presenterData));
    }

    return "OK";
};

export const CaptureDivAsImage = async (divId: string): Promise<string | null> => {
    const divElement = document.getElementById(divId) as HTMLElement | null;

    if (!divElement) {
        console.error('Div not found:', divId);
        return null;
    }

    // html2canvas returns a Promise that resolves with an HTMLCanvasElement
    try {
        const canvas: HTMLCanvasElement = await html2canvas(divElement);
        // toDataURL returns a string representing the image
        const imageBase64: string = canvas.toDataURL('image/png'); // or 'image/jpeg'
        return imageBase64;
    } catch (error) {
        console.error('Error capturing div with html2canvas:', error);
        return null;
    }
}

// Make your TypeScript function globally accessible on a dedicated object
// This is crucial for C# to find and call it via ExecuteScriptAsync
window.scene3dPresenterApi = {
    PresentFunction: PresentFunction,
    CaptureDivAsImage: CaptureDivAsImage
};

