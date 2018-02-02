import React from 'react';
import ReactDOM from 'react-dom';
import Provider from 'react-redux/es/components/Provider';

import Root from './components/Root';


ReactDOM.render(
  <Provider store={store}>
    <Root/>
  </Provider>,
  document.getElementById('container')
);

