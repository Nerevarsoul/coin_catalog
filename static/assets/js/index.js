var React = require('react')
var ReactDOM = require('react-dom')


var Coin = React.createClass ({
    getDefaultProps: function () {
        return {
            year: 1982,
            name: '5 копеек',
            mint: 'g'
        };
    },
    render: function() {
        var name = this.props.name;
        var year = this.props.year;
        var mint = this.props.mint;
        return (
            <div>
                <h3>{ name } { year }</h3>
                <p>{ mint }</p>
            </div>
        )
    }
})

var CoinList = React.createClass ({
    render: function() {
        return (
            <div>
                <Coin />
                <Coin />
                <Coin />
            </div>
        )
    }
})


ReactDOM.render(<CoinList />, document.getElementById('container'))