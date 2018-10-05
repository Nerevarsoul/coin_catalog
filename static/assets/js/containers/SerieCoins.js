import React from 'react';

import { SerieCoinsTable } from '../components/SerieCoinsTable'
import { fetchSerieCoins } from '../services/api';


export default class SerieCoins extends React.Component {
  constructor(props) {
    super(props);
    this.state = {nominals: [], coins: [], countries: []};
    this.loadCatalogue = this.loadCatalogue.bind(this);
    this.selectSerie = this.selectSerie.bind(this);
    this.selectPage = this.selectPage.bind(this);
  }

  componentDidMount() {
    fetchSerieCoins().then(
      this.setState( { coins: res } )
    )
  }

  render() {
    return (
      <div>
        <SerieCoinsTable coins={ this.state.coins } nominals={ this.state.nominals } countries={ this.state.countries } ></SerieCoinsTable> }
      </div>
    )
  }
}
