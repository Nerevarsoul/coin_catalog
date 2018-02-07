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
      console.log(serie);
      this.setState({ selectedSerie: serie });
      const { dispatch, selectedSerie } = this.props;
      dispatch(fetchCoinsIfNeeded(serie));
    }
  }

  render() {
    return (
      <div>
        <SerieList selectedSerie={ this.state.selectedSerie } series={ this.state.series } func={ this.SelectSerie }></SerieList>
        <UserCoinsList coins={ this.state.coins }></UserCoinsList>
      </div>
    )
  }
}

function mapStateToProps(state) {
  const { selectedSerie, coinsBySerie } = state;
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
