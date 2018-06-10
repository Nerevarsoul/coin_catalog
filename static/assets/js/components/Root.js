import React from 'react';
import { BrowserRouter, Route, Link } from 'react-router-dom';
import { Container, Menu, Grid } from 'semantic-ui-react';

import { routes, RouteWithSubRoutes } from '../routes';


const Root = () => (
    <BrowserRouter>
      <Container>
        <Grid>
          <Grid.Row>
            <Grid.Column width={3}>
              <Menu vertical>
                <Menu.Item link>
                  <Menu.Menu>
                    <Menu.Item link><Link to='/registration'>Регистрация</Link></Menu.Item>
                    <Menu.Item link><Link to='/auth'>Войти</Link></Menu.Item>
                  </Menu.Menu>
                </Menu.Item>
                <Menu.Item link><Link to='/test'>Мой кабинет</Link></Menu.Item>
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
            </Grid.Column>
            <Grid.Column width={13}>
              {routes.map((route, index) => (
                  <Route
                    key={index}
                    path={route.path}
                    component={route.component}
                  />
                ))}
            </Grid.Column>
          </Grid.Row>
        </Grid>
      </Container>
    </BrowserRouter>
)

export default Root
