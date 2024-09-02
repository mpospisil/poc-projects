import { useEffect, useRef } from "react";
import { EntryPoint, threeEntryPoint } from "@ideastatica/scene";
import { Scene, Selected } from "@ideastatica/scene/build/Types";

import { ViewFrontIcon, ViewRightIcon, ViewTopIcon, ViewPerspectiveIcon } from "../assets/icons";

interface Props {
  scene?: Scene;
  selected?: Selected | null;
  detailPage?: boolean;
  showMemberLabels?: boolean;
}

interface DispatchProps {
  onSelectItem?: (selected?: Selected) => void;
}

const addMPrefixToTexts = (scene: Scene, showMemberLabels: boolean | undefined): Scene => {
  return {
    ...scene,
    groups: scene.groups.map((x) => {
      return {
        ...x,
        text: showMemberLabels
          ? x.text.map((y) => {
              return {
                ...y,
                value: `M${y.value}`,
              };
            })
          : [],
      };
    }),
  };
};

const SceneRenderer = ({
  scene,
  selected,
  detailPage,
  onSelectItem,
  showMemberLabels,
}: Props & DispatchProps) => {
  const entryPointRef = useRef<EntryPoint | undefined>(undefined);
  useEffect(() => {
    if (entryPointRef.current && scene && selected) {
      entryPointRef.current.modelChanged(
        addMPrefixToTexts(scene, showMemberLabels),
        selected,
        false,
      );
    } else if (entryPointRef.current && scene) {
      entryPointRef.current.modelChanged(addMPrefixToTexts(scene, showMemberLabels), null, false);
    }
  }, [scene, selected, showMemberLabels]);

  const initialize = (element: HTMLDivElement | null) => {
    if (element !== null && !element.hasChildNodes() && scene && selected && onSelectItem) {
      entryPointRef.current = threeEntryPoint(element, onSelectItem);
      entryPointRef.current.modelChanged(
        addMPrefixToTexts(scene, showMemberLabels),
        selected,
        true,
      );
    } else if (element !== null && !element.hasChildNodes() && scene) {
      entryPointRef.current = threeEntryPoint(element, (_) => {});
      entryPointRef.current.modelChanged(addMPrefixToTexts(scene, showMemberLabels), null, true);
    }
  };

  const setXView = () => entryPointRef.current?.setXView();

  const setYView = () => entryPointRef.current?.setYView();

  const setZView = () => entryPointRef.current?.setZView();

  const setAxoView = () => entryPointRef.current?.setAxoView();

  return (
    <div className={detailPage ? "canvas-renderer canvas-renderer-detail" : "canvas-renderer"}>
      {selected ? (
        <div className="utilities">
          <div className="navigation">
            <div className="navigation-button" onClick={setXView}>
              <ViewFrontIcon />
            </div>
            <div className="navigation-button" onClick={setYView}>
              <ViewRightIcon />
            </div>
            <div className="navigation-button" onClick={setZView}>
              <ViewTopIcon />
            </div>{" "}
            <div className="navigation-button" onClick={setAxoView}>
              <ViewPerspectiveIcon />
            </div>
          </div>
        </div>
      ) : (
        ""
      )}

      <div className="scene" ref={initialize} />
    </div>
  );
};

export default SceneRenderer;
