let React = require('react')


class Coin extends React.Component {
    getDefaultProps() {
        return {
            year: 1982,
            name: '5 копеек',
            mint: 'g'
        };
    }

    render() {
        let name = this.props.name;
        let year = this.props.year;
        let mint = this.props.mint;
        return (
            <div>
                <h3>{ name } { year }</h3>
                <p>{ mint }</p>
            </div>
        )
    }
}

module.exports = Coin;
