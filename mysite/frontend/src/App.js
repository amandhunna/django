import logo from './logo.svg';
import { useState } from "react";
import './App.css';

function App() {
  const [ count, setCount ] = useState(0)
  return (
    <div className="App">
      <header className="App-header">
      <p>{count}</p>
        <img src={logo} className="App-logo" alt="logo" />
 
       
        <button onClick={() => setCount(prev => prev + 1)}>Inc count</button>
      </header>
    </div>
  );
}

export default App;
