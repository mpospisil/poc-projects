import React from 'react';
import logo from './logo.svg';
import './App.css';
import { useDispatch, useSelector } from 'react-redux';
import ConnectionPresenter from './components/ConnectionPresenter';


function App() {
  const dispatch = useDispatch();


  return (
  <div>
      <ConnectionPresenter />
    </div>
  );
}

export default App;
