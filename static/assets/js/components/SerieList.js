import React from 'react';


const SerieList = ({ series, func }) => (
  <div>
    {series.map((serie, index) =>
       <li key={index}
           onClick={ () => func(serie['name']) }>
         {serie['name']}
       </li>
    )}
  </div>
)

export default SerieList