import React from 'react';

import { Pagination } from 'semantic-ui-react';

import CatalogueFilter from './CatalogueFilter';
import CoinsList from '../components/CoinsList';
import ActionCoinsList from '../components/ActionCoinsList';
import { fetchCatalogCoins, addCoin } from '../services/api';
import { getToken } from '../utils/auth';


export default class CatalogueCoins extends React.Component {
  constructor(props) {
    super(props);
    this.state = {series: [], coins: [], user: '', selectedSerie: '', activePage: 1, count: 0};
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
      res => this.setState({ coins: res['results'], count: res['count'] })
    ) 
  }

  onChangeCoin(e, coinState, coinId) {
    if (coinState !== 'exchange' || e.target.value) {
      addCoin(coinId, coinState).then(
        res => console.log(res)
      )
    }
  }

  render() {
    return (
      <div>
        <CatalogueFilter func={ this.selectSerie }></CatalogueFilter>
        { this.state.user ? <ActionCoinsList coins={ this.state.coins } func={ this.onChangeCoin } ></ActionCoinsList>
        : <CoinsList coins={ this.state.coins }></CoinsList> }
        { this.state.count ? 
          <Pagination defaultActivePage={1} activePage={this.state.ActivePage} totalPages={Math.ceil(this.state.count / 100)} onPageChange={ this.selectPage  }/>
        : ''}
      </div>
    )
  }
}
