import { Table } from 'semantic-ui-react';


const SerieCoinsTables = ({ coins, nominals, countries }) => (
  <Table celled padded>
    <Table.Header>
      <Table.Row>
        <Table.HeaderCell> Страна / номинал </Table.HeaderCell>
        {nominals.map((nominal, index)
          <Table.HeaderCell> { nominal } </Table.HeaderCell>
        )}
      </Table.Row>
    </Table.Header>
    <Table.Body>
      {countries.map((coin, index) =>
        <Table.Row key={index}>
          <Table.Cell> { country } </Table.Cell>
          {coins['countries'].map((coin, index)
            <Table.HeaderCell> { coin } </Table.HeaderCell>
          )}
        </Table.Row>
      )}
    </Table.Body>
  </Table>
)

export default SerieCoinsTables
