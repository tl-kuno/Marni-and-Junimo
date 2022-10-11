import './App.css';
import axios from 'axios'


class App extends Component {
  constructor() {
    super()
    this.state = {
       command: ''
    }

    this.handleClick = this.handleClick.bind(this)
  }

  handleClick () {
    axios.get('http://picnic-quest.vercel.app/')
    .then( response => console.log("Hello World"))
  }

  render () {
    return (
      <div className='button__container'>
        <button className='button' onClick={this.handleClick}>
        Click Me</button>
      </div>
    )
  }
}

export default App;
