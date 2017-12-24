import React from 'react';
//import { connect } from 'react-redux'
import SerieList from '../components/SerieList';
import { fetchSeries } from '../utils';


export default class SerieCoins extends React.Component {
  constructor(props) {
    super(props);
    this.state = {series: []};
  }

  componentDidMount() {
    fetchSeries().then(
      res => this.setState({ series: res })
    )
  }

  render() {
    return (
      <SerieList series={ this.state.series }></SerieList>
    )
  }

}

