import React from 'react';
import { Route } from 'react-router-dom';

import Test from '../components/Test';
import SerieCoins from '../containers/SerieCoins'; 
import UserCoins from '../containers/UserCoins';

export const routes = [
  { path: '/test',
    component: Test
  },
  { path: '/series',
    component: SerieCoins
  },
  {
    path: '/coins',
    component: UserCoins
  }
]

export const RouteWithSubRoutes = (route) => (
  <Route path={route.path} render={props => (
    <route.component {...props} routes={route.routes}/>
  )}/>
)

