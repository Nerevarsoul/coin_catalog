import React from 'react';
import { connect } from 'react-redux';

import SerieList from '../components/SerieList';
import CoinsList from '../components/CoinsList';
import { fetchSeries } from '../utils';
import { SELECT_SERIE, REQUEST_COINS, RECEIVE_COINS } from '../actions/coins';


export default class SerieCoins extends React.Component {
  constructor(props) {
    super(props);
    this.state = {series: [], coins: [], selectedSerie: null};
    this.loadCatalogueBySerie = this.loadCatalogueBySerie.bind(this)
  }

  componentDidMount() {
    fetchSeries().then(
      res => this.setState({ series: res })
    )
  }

  componentDidUpdate(prevProps) {
    if (this.props.selectedSerie !== prevProps.selectedSerie) {
      const { dispatch, selectedSerie } = this.props
      dispatch(fetchCoinsIfNeeded(selectedSerie))
    }
  }

  SelectSerie(selectedSerie) {
    this.setState({ selectedSerie })
  }

  render() {
    return (
      <div>
        <SerieList selectedSerie={ selectedSerie } series={ this.state.series } func={ this.SelectSerie }></SerieList>
        <CoinsList coins={ this.state.coins }></CoinsList>
      </div>
    )
  }
}

function mapStateToProps(state) {
  const { selectedSerie } = state
  const {
    isFetching,
    lastUpdated,
    items: coins
  } = coinsBySerie[selectedSerie] || {
    isFetching: true,
    items: []
  }

  return {
    selectedSerie,
    coins,
    isFetching,
    lastUpdated
  }
}

export default connect(mapStateToProps)(SerieCoins)
