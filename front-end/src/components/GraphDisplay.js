import React from "react";

const GraphDisplay = ({ graph }) => {
  if (!graph) {
    return <div className="loading">Loading...</div>;
  }

  return (
    <div className="graph-container">
      <img className="graph" src={`data:image/png;base64,${graph}`} alt="img" />
    </div>
  );
};

export default GraphDisplay;
