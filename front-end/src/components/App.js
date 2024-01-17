import React from "react";
import UserInput from "./UserInput";
import GraphDisplay from "./GraphDisplay";
import "./page.css";
import axios from "axios";

class App extends React.Component {
  state = {
    graph: null,
    showGraph: false,
  };

  onFormSubmit = async (target, levels) => {
    const endpoint =
      process.env.NODE_ENV === "development"
        ? "http://127.0.0.1:5000/graph"
        : "https://grid-graph-bf4b1268c069.herokuapp.com/graph";

    this.setState({ graph: null });
    this.setState({ showGraph: true });
    const { data } = await axios.post(endpoint, {
      target: target,
      levels: levels,
    });

    if (data.image === null) {
      alert(data.message);
      this.setState({ showGraph: false });
    } else {
      this.setState({ graph: data.image });
    }
  };

  render() {
    return (
      <div className="container">
        <div>
          <div className="image-bg-fluid-height fadeImage">
            <h4 className="header-pic-title">Grid Graph</h4>
            <h3 className="header-pic-title title-small">2021</h3>
          </div>
          <div className="header">
            <h3>Electrical grid system</h3>
            <p>
              This project utilizes React and Python/Flask to provide the user a
              visualized specific portion of the electric grid according to a
              bus number and level depth.
            </p>
            <p>
              A breath first search algorithm is used to provide a visual
              picture of the desired portion of the grid from a JSON file of
              over 70,000 electrical grid components.
            </p>
          </div>
          <div className="main-content">
            <UserInput onFormSubmit={this.onFormSubmit} />
            {this.state.showGraph && <GraphDisplay graph={this.state.graph} />}
          </div>
        </div>
      </div>
    );
  }
}

export default App;
