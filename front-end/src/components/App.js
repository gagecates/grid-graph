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
    const { data } = await axios.post('https://grid-view-gmc.herokuapp.com/graph', {target: target, levels: levels})
    
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
        <div className='navbar'>
          <ul>
            <a href='https://github.com/gagecates/grid-graph'><li>GitHub Repo</li></a>
          </ul>
        </div>
        <div className='image-bg-fluid-height fadeImage'>
          <h4 className='header-pic-title'>Hire Gage Cates</h4>
          <p className='header-pic-title title-small'>2021</p>
        </div>
        <div className='header'>
          <h3>Introductory Project for Frontend Engineer</h3>
        </div>
        <div className='main-content'>
          <UserInput onFormSubmit={this.onFormSubmit}/>
          {this.state.showGraph && <GraphDisplay graph={this.state.graph}/>}
        </div>
        <div className='hire-me'>
          <div>Hire Gage Cates<br/>2021</div>
        </div>
      </div>
    );
  }
}

export default App;
