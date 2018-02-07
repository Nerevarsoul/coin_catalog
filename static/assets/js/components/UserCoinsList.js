import React from 'react';


export default const UserCoinsList = ({ coins }) => (
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
          <td>{ `${coin['catalog_coin']['face_value']} ${coin['catalog_coin']['currency']}` }</td>
          <td>{ coin['catalog_coin']['year']  }</td>
          <td> { coin['catalog_coin']['theme']  } </td>
          <td> { coin['catalog_coin']['mint']  }  </td>
        </tr>
      )}
    </tbody>
  </table>
)
