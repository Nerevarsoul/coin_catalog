import React from 'react';


export default const SerieList = ({ series, func }) => (
  <div>
    {this.props.series.map((serie, index) =>
       <li key={index}
           onClick={ () => this.props.func(serie['name']) }>
         {serie['name']}
       </li>
    )}
  </div>
)
