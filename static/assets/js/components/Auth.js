import React from 'react';
import { Form, Input } from 'semantic-ui-react';


export default class AuthComponent extends React.Component {
  constructor(props) {
    super(props);
    this.state = {login: '', password: ''};

    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  handleChange(event) {
    console.log(this.state);
    this.setState({[event.target.name]: event.target.value});
    console.log(this.state);
  }

  handleSubmit(event) {
    alert('A name was submitted: ' + this.state.value);
    event.preventDefault();

  }

  render() {
    return (
      <Form onSubmit={this.handleSubmit}>
        <Form.Field>
            <input placeholder='Введите логин...'
                   type="text"
                   name="login"
                   value={this.state.login}
                   onChange={this.handleChange} />
        </Form.Field>
        <Form.Field>
            <input placeholder='Введите пароль...'
                   type="password"
                   name="password"
                   value={this.state.password}
                   onChange={this.handleChange} />
        </Form.Field>
      </Form>
    );
  }


}
