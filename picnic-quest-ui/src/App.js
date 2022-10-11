import './App.css';
import axios from 'axios'


function App() {
  
  const handleClick = () => {
    axios.get('http://picnic-quest.vercel.app/')
    .then( response => console.log("Hello World"))
  }

    return (
      <div>
        <meta http-equiv="Content-Security-Policy" content="upgrade-insecure-requests"/> 
        <div className='button__container'>
          <button className='button' onClick={handleClick}>
          Click Me</button>
        </div>
      </div>
    )
}

export default App;
