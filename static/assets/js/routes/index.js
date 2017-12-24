import React from 'react';
import { Route } from 'react-router-dom';

import Test from '../components/Test';
import SerieCoins from '../containers/SerieCoins'; 

export const routes = [
  { path: '/test',
    component: Test
  },
  { path: '/series',
    component: SerieCoins
  }
]

export const RouteWithSubRoutes = (route) => (
  <Route path={route.path} render={props => (
    <route.component {...props} routes={route.routes}/>
  )}/>
)

