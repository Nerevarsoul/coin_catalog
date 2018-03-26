import React from 'react';
import { Input } from 'semantic-ui-react';




export default class AuthComponent extends React.Component {
  constructor(props) {
    super(props);
    this.state = {login: '', password: ''};

    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  handleChange(event) {
    this.setState({event.target.name: event.target.value});
  }

  handleSubmit(event) {
    alert('A name was submitted: ' + this.state.value);
    event.preventDefault();

  }

  render() {
    return (
      <form onSubmit={this.handleSubmit}>
        <Input placeholder='Введите логин...' name='login' value={this.state.login} onChange={this.handleChange} />
        <Input placeholder='Введите пароль...' name='password' value={this.state.password} onChange={this.handleChange} />
      </form>
    );
  }

}
