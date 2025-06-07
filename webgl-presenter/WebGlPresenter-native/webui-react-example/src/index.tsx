import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';
import { Provider } from 'react-redux';
import store from './store'; // Import the Redux store
import {myTypeScriptFunction} from './globalFunctions';

const root = ReactDOM.createRoot(
  document.getElementById('root') as HTMLElement
);

function onButtonClick() {
  console.log("Button clicked!");
  const result = myTypeScriptFunction("Button clicked! XXXXXX");
}


root.render(
  <div>
    <button id="global_button1" onClick={onButtonClick}>Global button</button>
    <Provider store={store}>
      <App />
    </Provider>
  </div>
);

// // You can also add some initial setup or a test button in your HTML
// document.addEventListener('DOMContentLoaded', () => {
//     const testButton = document.getElementById('global_button1');
//     if (testButton) {
//         testButton.addEventListener('click', async () => {
//             const result = await myTypeScriptFunction("Button clicked! XXXXXX");
//             console.log(`Result from button click: ${result}`);
//         });
//     }
// });

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
