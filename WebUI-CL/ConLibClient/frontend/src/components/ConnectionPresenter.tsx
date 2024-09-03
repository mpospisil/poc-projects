import React from "react";
import { useSelector, useDispatch } from "react-redux";
import { PresenterState } from '../store/presenterSlice';
import {SceneRenderer} from '@martin.pospisil/react-components/dist/components';

const ConnectionPresenter: React.FC = () => {
  let presenterState: PresenterState | null = useSelector(
    (state: any) => state.presenter
  );

  if (presenterState == null) {
    return (
      <div>
        <h1>Not loaded</h1>
      </div>
    );
  } else {
    return (
      <div >
        <SceneRenderer
            scene={presenterState.sceneData!}
        />
      </div>
    );
  }
};

export default ConnectionPresenter;