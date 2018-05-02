import React from 'react';

import CatalogueFilter from './CatalogueFilter';
import CoinsList from '../components/CoinsList';
import { fetchCatalogCoins } from '../services/api';


export default class SerieCoins extends React.Component {
  constructor(props) {
    super(props);
    this.state = {series: [], coins: []};
    this.loadCatalogueBySerie = this.loadCatalogueBySerie.bind(this)
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
        <CoinsList coins= { this.state.coins }></CoinsList>
      </div>
    )
  }
}
