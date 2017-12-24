import React from 'react';


export default class SerieList extends React.Component {
  constructor(props) {
    super(props);
  }

  render() {
    return (
      <div>
        {this.props.series.map((serie, index) => 
           <p key={index}> {serie['name']} </p>
        )}
      </div>
    )
  }
}

