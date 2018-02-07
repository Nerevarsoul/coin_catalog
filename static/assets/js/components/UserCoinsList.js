import React from 'react';


const UserCoinsList = ({ coins }) => (
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
          <td>{ `${coin['catalog_coin']['face_value']} ${coin['catalog_coin']['currency']}` }</td>
          <td>{ coin['catalog_coin']['year']  }</td>
          <td> { coin['catalog_coin']['theme']  } </td>
          <td> { coin['catalog_coin']['mint']  }  </td>
        </tr>
      )}
    </tbody>
  </table>
)

export default UserCoinsList