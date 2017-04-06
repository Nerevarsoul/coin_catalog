var React = require('react');
var ReactDOM = require('react-dom');


var Coin = require('components/Coin');

var coins = [
    {
        year: 1982,
        name: '5 копеек',
        mint: 'g'
    },
    {
        year: 1983,
        name: '10 копеек',
        mint: 'g'
    },
    {
        year: 1982,
        name: '2 копейки',
        mint: 'g'
    }
]

var CoinList = React.createClass ({
    render: function() {
        return (
            <div>
                <Coin name={coins[2]['name']}/>
            </div>
        )
    }
})


ReactDOM.render(<CoinList />, document.getElementById('container'))