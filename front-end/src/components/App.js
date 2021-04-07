import React from 'react';
import GraphDisplay from './GraphDisplay';
import flask from '../api/flask';
import './page.css';

class App extends React.Component {
  state = { graph: '' };

  onFormSubmit = async (term) => {
    const response = await flask.get('/search', {
      params: {
        
      },
    });

    this.setState({graph: response.data});
  };

  render() {
    return (
      <div>
      <div className='header'>
        <h3>Introductory Project for Frontend Engineer</h3>
      </div>
      <div className='main-content'>
        <GraphDisplay onFormSubmit={this.onFormSubmit}/>
      </div>
    </div>
    );
  }
}

export default App;
