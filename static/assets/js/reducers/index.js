import { combineReducers } from 'redux';

import { usernameReducer } from './auth';
import { coinsBySerie, selectedSerie } from './coins';

const rootReducer = combineReducers({
  coinsBySerie,
  selectedSerie,
  username: usernameReducer
})

export default rootReducer
