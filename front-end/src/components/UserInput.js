import React from 'react';

class UserInput extends React.Component {
    state = { 
        buss: null,
        level: null,
        bussValid: false,
        levelValid: false,
        formValid: false
    };

    onBussChange = event => {
        this.setState({ buss: event.target.value });
      };
    
    onLevelChange = event => {
        this.setState({ level: event.target.value });
    };

    onFormSubmit = event => {
        event.preventDefault();
        this.state.buss < 10001 || this.state.buss > 80100 ? alert('Please enter a bus number from 10001 - 80100') : console.log('ok')
        this.state.level == 0 || this.state.level === null ? alert('Please enter a level above 0') : console.log('ok')
        this.props.onFormSubmit(this.state.buss, this.state.level);
    };

    render() {
        return (
            <div className='overview'>
                <p>To see a focused view on a particular portion of the grid, choose a starting buss and depth level.</p>
                <form onSubmit={this.onFormSubmit} className="form">
                    <div className='user-input'>
                        <div className="field">
                            <label>Starting Bus</label>
                            <input
                                type="number"
                                value={this.state.buss}
                                placeholder="10001-80100"
                                onChange={this.onBussChange}
                                required
                            />
                        </div>
                        <div className="field">
                            <label>Level</label>
                            <input
                                type="number"
                                value={this.state.level}
                                onChange={this.onLevelChange}
                                required
                            />
                        </div>
                    </div>
                    <button type='submit' className="button button1">Fetch Graph</button>
                </form>
            </div>

            
        );
    }
}


export default UserInput;
