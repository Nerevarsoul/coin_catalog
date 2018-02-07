import React from 'react';


const CoinsList = ({ coins }) => (
  <table>
    <thead>
      <tr>
        <th>Номинал</th>
        <th>Год</th>
        <th>Тема</th>
        <th>Монетный двор</th>
      </tr>
    </thead>
    <tbody>
      {coins.map((coin, index) =>
        <tr key={index}>
          <td>{ `${coin['face_value']} ${coin['currency']}` }</td>
          <td>{ coin['year']  }</td>
          <td> { coin['theme']  } </td>
          <td> { coin['mint']  }  </td>
        </tr>
      )}
    </tbody>
  </table>
)

export default CoinsList