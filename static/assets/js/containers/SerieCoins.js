import React from 'react';

import CatalogueFilter from './CatalogueFilter';
import SerieList from '../components/SerieList'
import CoinsList from '../components/CoinsList';
import { fetchCatalogCoins, fetchSeries } from '../services/api';
import { getToken } from '../utils';


export default class SerieCoins extends React.Component {
  constructor(props) {
    super(props);
    this.state = {series: [], coins: [], user: none};
    this.loadCatalogueBySerie = this.loadCatalogueBySerie.bind(this)
  }

  componentDidMount() {
    this.setState( { user: getToken() } )
    fetchSeries().then(
      res => this.setState({ series: res })
    )
  }

  loadCatalogueBySerie(serie) {
    fetchCatalogCoins(serie).then(
      res => this.setState({ coins: res })
    ) 
  }

  render() {
    return (
      <div>
        <SerieList series={ this.state.series } func={ this.loadCatalogueBySerie }></SerieList>
        <CoinsList coins= { this.state.coins, this.state.user }></CoinsList>
      </div>
    )
  }
}
