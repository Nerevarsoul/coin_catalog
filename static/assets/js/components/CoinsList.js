import React from 'react';
import { Table } from 'semantic-ui-react';


function renderBody(coins, user) {
  if (user) {
    return (
      <Table.Body>
        {coins.map((coin, index) =>
          <Table.Row key={index}>
            <Table.Cell>{ `${coin['face_value']} ${coin['currency']}` }</Table.Cell>
            <Table.Cell>{ coin['year'] }</Table.Cell>
            <Table.Cell>{ coin['theme'] }</Table.Cell>
            <Table.Cell>{ coin['mint'] }</Table.Cell>
            <Table.Cell>{ coin['collection'] }</Table.Cell>
            <Table.Cell>{ coin['exchange'] }</Table.Cell>
            <Table.Cell>{ coin['wishlist'] }</Table.Cell>
          </Table.Row>
        )}
      </Table.Body>
    )
  } else {
    return (
      <Table.Body>
        {coins.map((coin, index) =>
          <Table.Row key={index}>
            <Table.Cell>{ `${coin['face_value']} ${coin['currency']}` }</Table.Cell>
            <Table.Cell>{ coin['year'] }</Table.Cell>
            <Table.Cell>{ coin['theme'] }</Table.Cell>
            <Table.Cell>{ coin['mint'] }</Table.Cell>
          </Table.Row>
        )}
      </Table.Body>
    )
  }
}

function renderHeader(user) {
  if (user) {
    return (
      <Table.Row>
        <Table.HeaderCell>Номинал</Table.HeaderCell>
        <Table.HeaderCell>Год</Table.HeaderCell>
        <Table.HeaderCell>Тема</Table.HeaderCell>
        <Table.HeaderCell>Монетный двор</Table.HeaderCell>
        <Table.HeaderCell>В коллекции</Table.HeaderCell>
        <Table.HeaderCell>На обмен</Table.HeaderCell>
        <Table.HeaderCell>Ищу</Table.HeaderCell>
      </Table.Row>
    )
  } else {
    return (
      <Table.Row>
        <Table.HeaderCell>Номинал</Table.HeaderCell>
        <Table.HeaderCell>Год</Table.HeaderCell>
        <Table.HeaderCell>Тема</Table.HeaderCell>
        <Table.HeaderCell>Монетный двор</Table.HeaderCell>
      </Table.Row>
    )
  }
}


const CoinsList = ({ coins, user }) => (
  <Table celled>
    <Table.Header>
      { renderHeader(user) }
    </Table.Header>
    { renderBody(coins, user) }
  </Table>
)

export default CoinsList
