import React from 'react';
import { connect } from 'react-redux';

import SerieList from '../components/SerieList';
import CoinsList from '../components/CoinsList';
import { fetchSeries } from '../utils';
import { SELECT_SERIE, REQUEST_COINS, RECEIVE_COINS } from '../actions/coins';


class UserCoins extends React.Component {
  constructor(props) {
    super(props);
    this.state = {series: [], coins: [], selectedSerie: null};
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
        <SerieList selectedSerie={ this.state.selectedSerie } series={ this.state.series } func={ this.SelectSerie }></SerieList>
        <CoinsList coins={ this.state.coins }></CoinsList>
      </div>
    )
  }
}

function mapStateToProps(state) {
  const { selectedSerie, coinsBySerie } = state
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

export default connect(mapStateToProps)(UserCoins)
