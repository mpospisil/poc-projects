import React from 'react';
import { useDispatch, useSelector } from 'react-redux';
import FileUploader from './components/FileUploader';
import ProjectContent from './components/ProjectContent';
import ConnectionPresenter from './components/ConnectionPresenter';

function App() {
  const dispatch = useDispatch();

  return (
    <div>
      <FileUploader /> {/* Add this line to include the FileUploader component */}
      <ProjectContent />
      <ConnectionPresenter />
    </div>
  );
}

export default App;