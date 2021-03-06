import {
  SELECT_SERIE,
  REQUEST_COINS,
  RECEIVE_COINS
} from '../actions/coins';


export function selectedSerie(state = null, action) {
  switch (action.type) {
    case SELECT_SERIE:
      return action.serie
    default:
      return state
  }
}

function coins (
  state = {
    isFetching: false,
    didInvalidate: false,
    coins: []
  },
  action
) {
  switch (action.type) {
    case REQUEST_COINS:
      return Object.assign({}, state, {
        isFetching: true,
        didInvalidate: false
      })
    case RECEIVE_COINS:
      return Object.assign({}, state, {
        isFetching: false,
        didInvalidate: false,
        coins: action.coins,
        lastUpdated: action.receivedAt
      })
    default:
      return state
  }
}

export function coinsBySerie(state = {}, action) {
  switch (action.type) {
    case RECEIVE_COINS:
    case REQUEST_COINS:
      return Object.assign({}, state, {
        coins: coins(state[action.serie], action)
      })
    default:
      return state
  }
}
