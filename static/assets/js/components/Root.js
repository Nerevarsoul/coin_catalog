import React from 'react';
import { BrowserRouter, Route, Link } from 'react-router-dom';
import { Container, Menu } from 'semantic-ui-react';

import { routes, RouteWithSubRoutes } from '../routes';


const Root = () => (
    <BrowserRouter>
      <Container>
        <Menu pointing vertical>
          <Menu.Item link><Link to='/test'>Test</Link></Menu.Item>
          <Menu.Item link><Link to='/series'>Series</Link></Menu.Item>
          <Menu.Item link><Link to='/coins'>Coins</Link></Menu.Item>
        <Menu/>
      {routes.map((route, index) => (
          <Route
            key={index}
            path={route.path}
            component={route.component}
          />
        ))}
      </Container>
    </BrowserRouter>
)

export default Root

