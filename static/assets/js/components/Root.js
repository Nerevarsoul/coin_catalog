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
              <Menu pointing vertical>
                <Menu.Item link><Link to='/test'>Test</Link></Menu.Item>
                <Menu.Item link><Link to='/series'>Series</Link></Menu.Item>
                <Menu.Item link><Link to='/coins'>Coins</Link></Menu.Item>
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

