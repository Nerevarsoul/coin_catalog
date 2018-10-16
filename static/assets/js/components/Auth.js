import React from 'react';
import { connect } from 'react-redux';
import { Form, Button } from 'semantic-ui-react';
import { NotificationSystem } from 'react-notification-system';

import { authPost } from '../services/api';
import { Login } from '../utils/auth';

class AuthComponent extends React.Component {
  constructor(props) {
    super(props);
    this.state = {username: '', password: ''};

    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
    _notificationSystem: null;
  }

  handleChange(event) {
    this.setState({[event.target.name]: event.target.value});
  }

  handleSubmit(event) {
    event.preventDefault();
    authPost(this.state).then(
      res => Login(res['token'], this.state.username),
      err => {
        console.log(err);
        this._notificationSystem.addNotification({
            message: 'Ошибка логина',
            level: 'error'
        });
      }
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

const mapStateToProps = store => {
  console.log(store)
  return {
    username: store.username,
  }
}

export default connect(mapStateToProps)(AuthComponent)