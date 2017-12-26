import React from 'react';


export default class CoinsList extends React.Component {
  constructor(props) {
    super(props);
  }

  render() {
    return (
      <table>
        <thead>
          <th>Номинал</th>
          <th>Год</th>
          <th>Тема</th>
          <th>Монетный двор</th>
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
  }
}

