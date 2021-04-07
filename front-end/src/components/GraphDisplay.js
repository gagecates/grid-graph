import React from 'react';

class GraphDisplay extends React.Component {
    state = { 
        buss: '',
        level: ''
    };

    onBussChange = event => {
        this.setState({ buss: event.target.value });
      };
    
    onLevelChange = event => {
        this.setState({ level: event.target.value });
    };

    onFormSubmit = event => {
        event.preventDefault();
        this.state.buss < 10001 ? alert('Please enter a buss number from 10001 - 80100') : console.log('ok')
        this.props.onFormSubmit(this.state.buss, this.state.level);
    };

    render() {
        return (
            <div className='overview'>
                <p>To see a focused view on a particular portion of the grid, choose a starting buss and depth level.</p>
                <form onSubmit={this.onFormSubmit} className="form">
                    <div className='user-input'>
                        <div className="field">
                            <label>Starting Buss</label>
                            <input
                                type="number"
                                value={this.state.buss}
                                placeholder="10001-80100"
                                onChange={this.onBussChange}
                            />
                        </div>
                        <div className="field">
                            <label>Level</label>
                            <input
                                type="number"
                                value={this.state.level}
                                onChange={this.onLevelChange}
                            />
                        </div>
                    </div>
                    <button type='submit' class="button button1">Fetch Graph</button>
                </form>

                
                
            </div>
        );
    }
}

export default GraphDisplay;
