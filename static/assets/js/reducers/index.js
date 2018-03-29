import { combineReducers } from 'redux';

import { coinsBySerie, selectedSerie } from '.coins';

const rootReducer = combineReducers({
  coinsBySerie,
  selectedSerie
})

export default rootReducer
