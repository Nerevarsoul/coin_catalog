import React from 'react';

import { Grid, Select } from 'semantic-ui-react';

import SerieList from '../components/SerieList';
import { fetchSeries, fetchCountries } from '../services/api';


export default class CatalogueFilter extends React.Component {
  constructor(props) {
    super(props);
    this.state = {series: [], countries: []};
    this.loadSeriesByCountry = this.loadSeriesByCountry.bind(this)
  }

  componentDidMount() {
    fetchCountries().then(
      res => this.setState({ countries: res.map((country, index) => ({"key": index, "value": country["name"], "text": country["name"]})) })
    )
  }

  loadSeriesByCountry(e, country) {
    fetchSeries(country["value"]).then(
      res => this.setState({ series: res.map((serie, index) => ({"key": index, "value": serie["name"], "text": serie["name"]})) })
    )
  }

  render() {
    return (
        <Grid columns={2} divided>
          <Grid.Row>
            <Grid.Column>
              <Select placeholder='Select country' options={ this.state.countries } onChange={ this.loadSeriesByCountry } />
            </Grid.Column>
            <Grid.Column>
              <Select placeholder='Select series' options={ this.state.series } onChange={ () => func(serie['name']) }/>
            </Grid.Column>
          </Grid.Row>
        </Grid>
    )
  }
}
