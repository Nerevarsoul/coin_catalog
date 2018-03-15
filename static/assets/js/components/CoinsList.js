import React from 'react';
import { Table } from 'semantic-ui-react';


const CoinsList = ({ coins }) => (
  <Table celled>
    <Table.Header>
      <Table.Row>
        <Table.HeaderCell>Номинал</Table.HeaderCell>
        <Table.HeaderCell>Год</Table.HeaderCell>
        <Table.HeaderCell>Тема</Table.HeaderCell>
        <Table.HeaderCell>Монетный двор</Table.HeaderCell>
      </Table.Row>
    </Table.Header>
    <Table.Body>
      {coins.map((coin, index) =>
        <Table.Row key={index}>
          <Table.Cell>{ `${coin['face_value']} ${coin['currency']}` }</Table.Cell>
          <Table.Cell>{ coin['year']  }</Table.Cell>
          <Table.Cell> { coin['theme']  } </Table.Cell>
          <Table.Cell> { coin['mint']  }  </Table.Cell>
        </Table.Row>
      )}
    </Table.Body>
  </Table>
)

export default CoinsList