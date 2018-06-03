import React from 'react';

import { Pagination } from 'semantic-ui-react';

import CatalogueFilter from './CatalogueFilter';
import CoinsList from '../components/CoinsList';
import ActionCoinsList from '../components/ActionCoinsList';
import { fetchCatalogCoins } from '../services/api';
import { getToken } from '../utils';


export default class SerieCoins extends React.Component {
  constructor(props) {
    super(props);
    this.state = {series: [], coins: [], user: '', selectedSerie: '', activePage: 1};
    this.loadCatalogue = this.loadCatalogue.bind(this);
    this.selectSerie = this.selectSerie.bind(this);
    this.selectPage = this.selectPage.bind(this);
  }

  componentDidMount() {
    this.setState( { user: getToken() } );
  }

  selectSerie(e, serie) {
    this.setState( { selectedSerie: serie["value"] } );
    this.loadCatalogue(serie["value"], this.state.activePage);
  }

  selectPage(e, page) {
    this.setState( { activePage: page["activePage"] } );
    this.loadCatalogue(this.state.selectedSerie, page["activePage"])
  }

  loadCatalogue(serie, page) {
    fetchCatalogCoins(serie, page).then(
      res => this.setState({ coins: res })
    ) 
  }

  onChangeCoin(e, coin) {
    console.log(coin);
  }

  render() {
    return (
      <div>
        <CatalogueFilter func={ this.selectSerie }></CatalogueFilter>
        { this.state.user ? <ActionCoinsList coins={ this.state.coins } func={ this.onChangeCoin } ></ActionCoinsList>
        : <CoinsList coins={ this.state.coins }></CoinsList> }
        <Pagination defaultActivePage={1} activePage={this.state.ActivePage} totalPages={10} onPageChange={ this.selectPage  }/>
      </div>
    )
  }
}
