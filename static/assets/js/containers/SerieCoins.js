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

  onChangeCoin(e, coin) {
    console.log(coin);
  }

  render() {
    return (
      <div>
        <CatalogueFilter func={ this.loadCatalogueBySerie }></CatalogueFilter>
        { this.state.user ? <ActionCoinsList coins={ this.state.coins } func={ this.onChangeCoin } ></ActionCoinsList>
        : <CoinsList coins={ this.state.coins }></CoinsList> }
      </div>
    )
  }
}
