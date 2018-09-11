import React from 'react';
import { Link } from 'react-router-dom';
import { Menu} from 'semantic-ui-react';

import { getUsername, Logout } from '../utils/auth';

export default class CoinMenu extends React.Component {
  constructor(props) {
    super(props);
    this.state = {username: getUsername()};
  }

  logoutHandle() {
    Logout()
    this.setState({username: null});
  }

  render() {
    return (
      <Menu vertical>
        {
        this.state.username ?
        <Menu.Item link>
            {this.state.username}
            <Menu.Item link><Link to='/test'>Мой кабинет</Link></Menu.Item>
            <Menu.Item onClick={this.logoutHandle}>Выйти</Menu.Item>
        </Menu.Item>
        :
        <Menu.Item link>
          <Menu.Menu>
            <Menu.Item link><Link to='/registration'>Регистрация</Link></Menu.Item>
            <Menu.Item link><Link to='/auth'>Войти</Link></Menu.Item>
          </Menu.Menu>
        </Menu.Item>
        }
        <Menu.Item link>
            Монеты
            <Menu.Menu>
              <Menu.Item link><Link to='/catalogue'>Каталог</Link></Menu.Item>
              <Menu.Item link><Link to='/series'>Серии</Link></Menu.Item>
              <Menu.Item link><Link to='/coins'>Обменник</Link></Menu.Item>
              <Menu.Item link><Link to='/coins'>Монеты на обмен</Link></Menu.Item>
              <Menu.Item link><Link to='/coins'>Монеты в поиске</Link></Menu.Item>
            </Menu.Menu>
        </Menu.Item>
        <Menu.Item link><Link to='/users'>Пользователи</Link></Menu.Item>
      </Menu>
    )
  }
}
