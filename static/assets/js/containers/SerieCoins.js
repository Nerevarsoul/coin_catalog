import React from 'react';

import CatalogueFilter from './CatalogueFilter';
import CoinsList from '../components/CoinsList';
import ActionCoinsList from '../components/ActionCoinsList';
import { fetchCatalogCoins } from '../services/api';
import { getToken } from '../utils';


export default class SerieCoins extends React.Component {
  constructor(props) {
    super(props);
    this.state = {series: [], coins: [], user: ''};
    this.loadCatalogueBySerie = this.loadCatalogueBySerie.bind(this)
  }

  componentDidMount() {
    this.setState( { user: getToken() } )
  }

  loadCatalogueBySerie(e, serie) {
    fetchCatalogCoins(serie["value"]).then(
      res => this.setState({ coins: res })
    ) 
  }

  render() {
    return (
      <div>
        <CatalogueFilter func={ this.loadCatalogueBySerie }></CatalogueFilter>
        { this.state.user ? <ActionCoinsList coins={ this.state.coins }></ActionCoinsList>
        : <CoinsList coins={ this.state.coins }></CoinsList> }
      </div>
    )
  }
}
