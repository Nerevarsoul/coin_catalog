import React from 'react';
import { connect } from 'react-redux';
import { Header, Grid } from 'semantic-ui-react';

import SerieList from '../components/SerieList';
import StatusList from '../components/StatusList';
import UserCoinsList from '../components/UserCoinsList';
import { fetchSeries } from '../services/api';
import { fetchCoinsIfNeeded } from '../actions/coins';


class UserCoins extends React.Component {
  constructor(props) {
    super(props);
    this.state = {series: [], coins: [], selectedSerie: null, selectedStatus: null};
    this.selectStatus = this.selectStatus.bind(this);
    this.selectSerie = this.selectSerie.bind(this);
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

  selectSerie(serie) {
    if (this.props.selectedSerie !== serie) {
      this.setState({ selectedSerie: serie });
      const { dispatch, selectedSerie } = this.props;
      dispatch(fetchCoinsIfNeeded(serie, this.state.SelectedStatus));
    }
  }

  selectStatus(stat) {
    if (this.props.selectedStatus !== stat) {
      this.setState({ selectedStatus: stat });
      const { dispatch, selectedStatus } = this.props;
      dispatch(fetchCoinsIfNeeded(this.state.selectedSerie, stat));
    }
  }

  render() {
    const { serie, coins, isFetching, lastUpdated } = this.props
    return (
      <div>
        <Grid columns={2} divided>
          <Grid.Row>
            <Grid.Column>  
              <SerieList selectedSerie={ this.state.selectedSerie } series={ this.state.series } func={ this.selectSerie }></SerieList>
            </Grid.Column>
            <Grid.Column>
              <StatusList func={ this.selectStatus }></StatusList>
            </Grid.Column>
          </Grid.Row>
        </Grid>
        <Header as='h2'> { this.state.selectedSerie } </Header>
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
