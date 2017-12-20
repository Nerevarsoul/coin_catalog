import React from 'react';
import { BrowserRouter, Route } from 'react-router-dom'
import Router from 'react-router/es/Router';
//import Provider from 'react-redux/es/components/Provider';

import routes from '../routes'

function Root() {
  return (
    <BrowserRouter>
    <div>
      <Route path='/' component={ routes }/>
    </div>
    </BrowserRouter>
  )
}

export default Root

