import React from 'react';

import CatalogueFilter from './CatalogueFilter';
import SerieList from '../components/SerieList'
import CoinsList from '../components/CoinsList';
import { fetchCatalogCoins, fetchSeries } from '../services/api';
import { getToken } from '../utils';


export default class SerieCoins extends React.Component {
  constructor(props) {
    super(props);
    this.state = {series: [], coins: [], user: ''};
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
        <CatalogueFilter func={ this.loadCatalogueBySerie }></CatalogueFilter>
        <CoinsList coins={ this.state.coins } user={ this.state.user }></CoinsList>
      </div>
    )
  }
}
