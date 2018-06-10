import React from 'react';
import { Route } from 'react-router-dom';

import Auth from '../components/Auth';
import CatalogueCoins from '../containers/CatalogueCoins';
import UserCoins from '../containers/UserCoins';
import SerieCoins from '../containers/SerieCoins';

export const routes = [
  { path: '/catalogue',
    component: CatalogueCoins
  },
  {
    path: '/coins',
    component: UserCoins
  },
  {
    path: '/series',
    component: SerieCoins
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
