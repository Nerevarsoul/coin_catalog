import React from 'react';
import { BrowserRouter, Route, Link } from 'react-router-dom';
//import Provider from 'react-redux/es/components/Provider';

import { routes, RouteWithSubRoutes } from '../routes';

const Root = () => (
    <BrowserRouter>
      <div>
        <li><Link to='/test'>Test</Link></li>
        <li><Link to='/series'>Series</Link></li>

      {routes.map((route, index) => (
          <Route
            key={index}
            path={route.path}
            component={route.component}
          />
        ))}
    </div>
    </BrowserRouter>
)

export default Root

