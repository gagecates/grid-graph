import React from 'react';

const GraphDisplay = ({graph}) => {
    console.log(graph)

    if (!graph) {
        return <div className='loading'>Loading...</div>;
      }

    return(

        <div className='graph-container'>
            <img className='graph' src={graph} alt="img" />
        </div>
    )
};

export default GraphDisplay;