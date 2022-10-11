import './App.css';
import axios from 'axios'


function App() {
  
  const handleClick = () => {
    axios.get('/api/commands')
    .then( response => console.log("Hello World"))
  }

    return (
      <div>

        <div className='button__container'>
          <button className='button' onClick={handleClick}>
          Click Me</button>
        </div>
      </div>
    )
}

export default App;
