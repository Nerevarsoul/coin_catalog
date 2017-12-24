import React from 'react';

import { fetchSeries } from '../utils';

export default class SerieList extends React.Component {
  constructor(props) {
    super(props);
    this.state = {series: []};
    this.getSeries();
  }

  getSeries() {
    fetchSeries().then(
      res => this.setState({ series: res })
    )
  }

  render() {
    return (
      <div>
        {this.state.series.map((serie, index) => 
           <p key={index}> {serie['name']} </p>
        )}
      </div>
    )
  }
}

