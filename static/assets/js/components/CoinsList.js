import React from 'react';


export default const CoinsList = ({ coins }) => (
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
      {this.props.coins.map((coin, index) =>
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
