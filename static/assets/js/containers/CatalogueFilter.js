import React from 'react';

import SerieList from '../components/SerieList';
import CountriesList from '../components/CountriesList';
import { fetchSeries, fetchCountries } from '../services/api';


export default class CatalogueFilter extends React.Component {
  constructor(props) {
    super(props);
    this.state = {series: [], countries: []};
    this.loadSeriesBySerie = this.loadSeriesBySerie.bind(this)
  }

  componentDidMount() {
    fetchCountries().then(
      res => this.setState({ countries: res })
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
              <CountriesList coins= { this.state.countries } func={ this.loadSeriesByCountry }></CountriesList>
            </Grid.Column>
            <Grid.Column>
              <SerieList series={ this.state.series } func={ this.loadCatalogueBySerie }></SerieList>
            </Grid.Column>
          </Grid.Row>
        </Grid>
    )
  }
}
