import React from 'react';
import { Table, Checkbox, Form } from 'semantic-ui-react';


const ActionCoinsList = ({ coins }) => (
  <Form>
    <Table celled>
      <Table.Header>
        <Table.Row>
          <Table.HeaderCell>Номинал</Table.HeaderCell>
          <Table.HeaderCell>Год</Table.HeaderCell>
          <Table.HeaderCell>Тема</Table.HeaderCell>
          <Table.HeaderCell>Монетный двор</Table.HeaderCell>
          <Table.HeaderCell>В коллекции</Table.HeaderCell>
          <Table.HeaderCell>На обмен</Table.HeaderCell>
          <Table.HeaderCell>Ищу</Table.HeaderCell>
        </Table.Row>}
      </Table.Header>
      <Table.Body>
        {coins.map((coin, index) =>
          <Table.Row key={index}>
            <Table.Cell>{ `${coin['face_value']} ${coin['currency']}` }</Table.Cell>
            <Table.Cell>{ coin['year'] }</Table.Cell>
            <Table.Cell>{ coin['theme'] }</Table.Cell>
            <Table.Cell>{ coin['mint'] }</Table.Cell>

            <Table.Cell>
              <Form.Field>
                <Checkbox value={ coin['collection'] } />
              </Form.Field>
            </Table.Cell>

            <Table.Cell>
              <Form.Field>
                <input value={ coin['exchange'] } />
              </Form.Field>
            </Table.Cell>

            <Table.Cell>
              <Form.Field>
                <Checkbox value={ coin['wishlist'] } />
              </Form.Field>
            </Table.Cell>
          </Table.Row>
        )}
      </Table.Body>
    </Table>
  </Form>
)

export default ActionCoinsList
