import React from 'react'
import 'whatwg-fetch';

export default class SerieList extends React.Component {
    constructor(props) {
        super(props);
        this.state = {series: [{'name': 'work!'}]};
        this.getSeries();
    }

    getSeries() {
        fetch('http://185.12.95.205:8000/api/series').then(res => {
            console.log(res.json());
            if (res) {
                this.setState({ series: res });
            }
         });
    }

    render() {
        console.log(this.series);
        return (
            <div>
                <p>{ this.state.series[0]['name'] }</p>
            </div>
        )
    }
}

