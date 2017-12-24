import React from 'react';


export default class SerieList extends React.Component {
  constructor(props) {
    super(props);
  }

  render() {
    return (
      <div>
        {this.props.series.map((serie, index) => 
           <li key={index} 
               onClick={ () => this.props.func(serie['name']) }> 
             {serie['name']} 
           </li>
        )}
      </div>
    )
  }
}

