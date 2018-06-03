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
    this.loadCatalogueBySerie = this.loadCatalogueBySerie.bind(this)
  }

  componentDidMount() {
    this.setState( { user: getToken() } )
  }

  selectSerie(e, serie) {
    this.setState( { selectedSerie: serie["value"] } )
    this.loadCatalogue()
  }

  selectPage(e, page) {
    console.log(page);
    this.setState( { activePage: page["value"] } )
    this.loadCatalogue()
  }

  loadCatalogue() {
    fetchCatalogCoins(this.selectedSerie, this.ActivePage).then(
      res => this.setState({ coins: res })
    ) 
  }

  onChangeCoin(e, coin) {
    console.log(coin);
  }

  render() {
    return (
      <div>
        <CatalogueFilter func={ this.loadCatalogue }></CatalogueFilter>
        { this.state.user ? <ActionCoinsList coins={ this.state.coins } func={ this.onChangeCoin } ></ActionCoinsList>
        : <CoinsList coins={ this.state.coins }></CoinsList> }
        <Pagination defaultActivePage={1} activePage={this.state.ActivePage} totalPages={10} onPageChange={  }/>
      </div>
    )
  }
}
