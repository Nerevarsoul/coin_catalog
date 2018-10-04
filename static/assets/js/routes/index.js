import React from 'react';
import { Route } from 'react-router-dom';

import Auth from '../components/Auth';
import CatalogueCoins from '../containers/CatalogueCoins';
import SerieCoins from '../containers/SerieCoins';
import UserCoins from '../containers/UserCoins';
import Profile from '../containers/Profile';

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
  {
    path: '/profile',
    component: Profile
  },
]

export const RouteWithSubRoutes = (route) => (
  <Route path={route.path} render={props => (
    <route.component {...props} routes={route.routes}/>
  )}/>
)
