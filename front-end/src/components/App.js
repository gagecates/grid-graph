import React from 'react';
import UserInput from './UserInput';
import GraphDisplay from './GraphDisplay';
import './page.css';
import axios from 'axios';

class App extends React.Component {
  state = { 
    graph: null,
    showGraph: false
  };

  onFormSubmit = async (target, levels) => {

    this.setState({graph: null});
    this.setState({showGraph: true})

    const { data } = await axios.post('https://git.heroku.com/grid-view-gmc.git/graph', {target: target, levels: levels})
    if (data.image === null){
      alert(data.message)
      this.setState({showGraph: false})
    }else{
      this.setState({graph: data.image});
    }

  };

  render() {
    return (
      <div>
      <div className='header'>
        <h3>Introductory Project for Frontend Engineer</h3>
      </div>
      <div className='main-content'>
        <UserInput onFormSubmit={this.onFormSubmit}/>
        { this.state.showGraph && <GraphDisplay graph={this.state.graph}/>}
      </div>
    </div>
    );
  }
}

export default App;
