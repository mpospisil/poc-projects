import store from './store'; // Import the Redux store
import { PresenterData } from './models/presenterData';
import { Scene } from "@ideastatica/scene/build/Types";

import {
  setSceneData,
} from './store/presenterSlice';

declare global {
    interface Window {
        myExportedTypeScriptApi: {
            myTypeScriptFunction: (data: string) => Promise<string>;
        };
        // If you exposed C# directly to window.myCSharpAPI
        myCSharpAPI?: {
            SayHelloToCSharp: (name: string) => string;
            ReceiveMessageFromTypeScript: (message: string) => void;
        };
    }
}

export const myTypeScriptFunction = async (data: string): Promise<string> => {
    console.log(`TypeScript function received: ${data}`);
    // You can perform any logic here
    const response = `Processed by TypeScript: ${data.toUpperCase()}`;

    // Example: Calling a C# method from TypeScript
    if (window.myCSharpAPI) {
        const csharpResponse = await window.myCSharpAPI.SayHelloToCSharp("TypeScript");
        console.log(`C# responded: ${csharpResponse}`);
        window.myCSharpAPI.ReceiveMessageFromTypeScript("Message from TS to C#!");
    }

      const sceneJson = '{"groups":[{"type":"singleColor","color":[],"faces":[],"lines":[],"priority":1,"text":[]}],"vertices":[]}';

      const obj = JSON.parse(sceneJson);
      const scene : Scene = obj;

      const presenterData : PresenterData = {
        sceneData : scene,
      };

      store.dispatch(setSceneData(presenterData))


    return response;
};

// Make your TypeScript function globally accessible on a dedicated object
// This is crucial for C# to find and call it via ExecuteScriptAsync
window.myExportedTypeScriptApi = {
    myTypeScriptFunction: myTypeScriptFunction
};

