import React from 'react';
import { Table } from 'semantic-ui-react';


const UserCoinsList = ({ coins }) => (
  <Table celled padded>
    <Table.Header>
      <Table.Row>
        <Table.HeaderCell>Номинал</Table.HeaderCell>
        <Table.HeaderCell>Год</Table.HeaderCell>
        <Table.HeaderCell>Тема</Table.HeaderCell>
        <Table.HeaderCell>Монетный двор</Table.HeaderCell>
        <Table.HeaderCell>Статус</Table.HeaderCell>
      </Table.Row>
    </Table.Header>
    <Table.Body>
      {coins.map((coin, index) =>
        <Table.Row key={index}>
          <Table.Cell> { `${coin['catalog_coin']['face_value']} ${coin['catalog_coin']['currency']}` } </Table.Cell>
          <Table.Cell> { coin['catalog_coin']['year'] } </Table.Cell>
          <Table.Cell> { coin['catalog_coin']['theme'] } </Table.Cell>
          <Table.Cell> { coin['catalog_coin']['mint'] } </Table.Cell>
          <Table.Cell> { coin['status'] } </Table.Cell>
          
        </Table.Row>
      )}
    </Table.Body>
  </Table>
)

export default UserCoinsList
