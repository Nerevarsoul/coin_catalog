import React from 'react';
import { connect } from 'react-redux';

import SerieList from '../components/SerieList';
import UserCoinsList from '../components/UserCoinsList';
import { fetchSeries } from '../utils';
import { fetchCoinsIfNeeded } from '../actions/coins';


class UserCoins extends React.Component {
  constructor(props) {
    super(props);
    this.state = {series: [], coins: [], selectedSerie: null};
    this.SelectSerie = this.SelectSerie.bind(this);
  }

  componentDidMount() {
    fetchSeries().then(
      res => this.setState({ series: res })
    )
  }

  componentDidUpdate(prevProps) {
    if (this.props.selectedSerie !== prevProps.selectedSerie) {
      const { dispatch, selectedSerie } = this.props;
      dispatch(fetchCoinsIfNeeded(selectedSerie));
    }
  }

  SelectSerie(serie) {
    if (this.props.selectedSerie !== serie) {
      this.setState({ selectedSerie: serie });
      const { dispatch, selectedSerie } = this.props;
      dispatch(fetchCoinsIfNeeded(serie));
    }
  }

  render() {
    const { serie, coins, isFetching, lastUpdated } = this.props
    return (
      <div>
        <SerieList selectedSerie={ this.state.selectedSerie } series={ this.state.series } func={ this.SelectSerie }></SerieList>
        <UserCoinsList coins={ coins }></UserCoinsList>
      </div>
    )
  }
}

function mapStateToProps(state) {
  const { serie, coinsBySerie } = state;
  const {
    isFetching,
    lastUpdated,
    coins: coins
  } = coinsBySerie['coins'] || {
    isFetching: true,
    coins: []
  }
  return {
    serie,
    coins,
    isFetching,
    lastUpdated
  }
}

export default connect(mapStateToProps)(UserCoins)
