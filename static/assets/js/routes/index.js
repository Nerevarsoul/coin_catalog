import React from 'react';
import { Switch, Route } from 'react-router-dom';

//import SerieList from '../components/SerieList';
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
      // pass the sub-routes down to keep nesting
      <route.component {...props} routes={route.routes}/>
    )}/>
  )



