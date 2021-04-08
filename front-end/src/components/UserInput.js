import React from 'react';

class UserInput extends React.Component {
    state = { 
        errors: {},
        fields: {}
    };

    handleValidation(){
        let fields = this.state.fields;
        let errors = {};
        let formIsValid = true;

        //bus start number check
        if(!fields["bus"]){
           formIsValid = false;
           errors["input"] = "Field can not be empty";
        }
  
        if(typeof fields["bus"] !== "undefined"){
           if(!fields["bus"].match(/^[0-9\b]+$/)){
              formIsValid = false;
              errors["input"] = "Only numbers";
           }        
        }

        if(fields["bus"] < 10001 || fields["bus"] > 80100){
            formIsValid = false;
            errors["input"] = "Please enter a bus in the range of 10001 - 80100";
         }
   
        //level check
        if(!fields["level"]){
           formIsValid = false;
           errors["input"] = "Field can not be empty";
        }

        if(fields["level"] < 1){
            formIsValid = false;
            errors["input"] = "Please enter at least a level of 1.";
        }

       this.setState({errors: errors});
       return formIsValid;
    }

    handleChange(field, e){         
        let fields = this.state.fields;
        fields[field] = e.target.value;        
        this.setState({fields});
    }

    onFormSubmit = event => {
        event.preventDefault();
        if(this.handleValidation()){
            console.log('no errors')
            this.props.onFormSubmit(this.state.fields["bus"], this.state.fields["level"]);
        } 
    };

    render() {
        return (
            <div className='overview'>
                <p>To see a focused view on a particular portion of the grid, choose a starting bus and depth level.</p>
                <form onSubmit={this.onFormSubmit} className="form">
                    <div className='user-input'>
                        <div className="field">
                            <label>Starting Bus</label>
                            <input
                                type="number"
                                value={this.state.fields["bus"]}
                                placeholder="10001-80100"
                                onChange={this.handleChange.bind(this, "bus")}
                                required
                            />
                        </div>
                        <div className="field">
                            <label>Level</label>
                            <input
                                type="number"
                                value={this.state.fields["level"]}
                                onChange={this.handleChange.bind(this, "level")}
                                required
                            />
                        </div>
                    </div>
                    <div className='error' style={{color: "red"}}>{this.state.errors["input"]}</div>
                    <button type='submit' className="button button1">Fetch Graph</button>
                </form>
            </div>
        );
    }
}


export default UserInput;
