import React from 'react';
//import { connect } from 'react-redux'
import SerieList from '../components/SerieList';
import CoinsList from '../components/CoinsList';
import { fetchSeries, fetchCatalogCoins } from '../utils';


export default class SerieCoins extends React.Component {
  constructor(props) {
    super(props);
    this.state = {series: [], coins: []};
    this.loadCatalogueBySerie = this.loadCatalogueBySerie.bind(this)
  }

  componentDidMount() {
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
        <CoinsList coins= { this.state.coins }></CoinsList>
      </div>
    )
  }
}

