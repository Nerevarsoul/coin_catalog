import React from 'react';
import { Route } from 'react-router-dom';

import Auth from '../components/Auth';
import SerieCoins from '../containers/SerieCoins'; 
import UserCoins from '../containers/UserCoins';

export const routes = [
  { path: '/catalogue',
    component: SerieCoins
  },
  {
    path: '/coins',
    component: UserCoins
  },
  {
    path: '/auth',
    component: Auth
  },
]

export const RouteWithSubRoutes = (route) => (
  <Route path={route.path} render={props => (
    <route.component {...props} routes={route.routes}/>
  )}/>
)
