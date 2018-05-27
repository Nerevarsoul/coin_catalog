import React from 'react';

import { Grid } from 'semantic-ui-react';

import SerieList from '../components/SerieList';
import CountriesList from '../components/CountriesList';
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

  loadSeriesByCountry(country) {
    fetchCatalogCoins(country).then(
      res => this.setState({ series: res })
    )
  }

  render() {
    return (
        <Grid columns={2} divided>
          <Grid.Row>
            <Grid.Column>
              <CountriesList countries= { this.state.countries } func={ this.loadSeriesByCountry }></CountriesList>
            </Grid.Column>
            <Grid.Column>
              <SerieList series={ this.state.series } func={ this.props.loadCatalogueBySerie }></SerieList>
            </Grid.Column>
          </Grid.Row>
        </Grid>
    )
  }
}
