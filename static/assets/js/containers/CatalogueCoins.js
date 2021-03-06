import React from 'react';

import { Pagination } from 'semantic-ui-react';
import { NotificationSystem } from 'react-notification-system';

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
    _notificationSystem: null;
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

  onCheckCoin(e, data, coinState, coinId) {
    if (data.checked ) {
      addCoin({'catalog_coin': coinId, 'status': coinState}).then(
        res => {
          console.log(res);
          this._notificationSystem.addNotification({
            message: 'Монета успешно добавлена',
            level: 'success'
          });
        }
      )
    }
  }

  onInputCoin(e, data, coinId) {
    let value = data['value'];
    if (value) {
      value = data['value']-data['defaultValue'];
    } else {
      console.log('error');
      return
    }
    let query_data = {'catalog_coin': coinId, 'status': 'for_exchange'};
    if (value < 1) {
      console.log('error');
      return
    }
    if (value > 1) {
      let list_data = []
      for (let i = 0; i < value; i++) {
        list_data.push(query_data);
      }
      query_data = list_data;
    }
    addCoin(query_data).then(
      res => {
        console.log(res);
        this._notificationSystem.addNotification({
            message: 'Монета успешно добавлена',
            level: 'success'
          });
      }
    )
  }

  render() {
    return (
      <div>
        <NotificationSystem ref="notificationSystem" />
        <CatalogueFilter func={ this.selectSerie }></CatalogueFilter>
        { this.state.user ? <ActionCoinsList coins={ this.state.coins } handleCheck={ this.onCheckCoin } handleInput={ this.onInputCoin  }></ActionCoinsList>
        : <CoinsList coins={ this.state.coins }></CoinsList> }
        { this.state.count ? 
          <Pagination defaultActivePage={1} activePage={this.state.ActivePage} totalPages={Math.ceil(this.state.count / 100)} onPageChange={ this.selectPage  }/>
        : ''}
      </div>
    )
  }
}
