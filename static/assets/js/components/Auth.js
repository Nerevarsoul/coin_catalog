import React from 'react';
import { Form, Button } from 'semantic-ui-react';

import { authPost } from '../services/api';

export default class AuthComponent extends React.Component {
  constructor(props) {
    super(props);
    this.state = {username: '', password: ''};

    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  handleChange(event) {
    this.setState({[event.target.name]: event.target.value});
  }

  handleSubmit(event) {
    console.log(this.state);
    event.preventDefault();
    authPost(this.state).then(
      res => console.log(res)
    )
  }

  render() {
    return (
      <Form onSubmit={this.handleSubmit}>
        <Form.Field>
            <input placeholder='Введите логин...'
                   type="text"
                   name="username"
                   value={this.state.username}
                   onChange={this.handleChange} />
        </Form.Field>
        <Form.Field>
            <input placeholder='Введите пароль...'
                   type="password"
                   name="password"
                   value={this.state.password}
                   onChange={this.handleChange} />
        </Form.Field>
        <Button type='submit'>Submit</Button>
      </Form>
    );
  }


}
