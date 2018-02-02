import { getCoins } from '../utils';

export const REQUEST_COINS = 'REQUEST_COINS'
export const RECEIVE_COINS = 'RECEIVE_COINS'
export const SELECT_SERIE = 'SELECT_SERIE'


export function selectSerie(serie) {
  return {
    type: SELECT_SERIE,
    serie
  }
}

function requestCoins(serie) {
  return {
    type: REQUEST_COINS,
    serie
  }
}

function receiveCoins(serie, json) {
  return {
    type: RECEIVE_COINS,
    serie,
    coins: json.data.children.map(child => child.data),
    receivedAt: Date.now()
  }
}

function fetchCoins(serie) {
  return dispatch => {
    dispatch(requestCoins(serie))
    return getCoins(serie)
      .then(json => dispatch(receiveCoins(serie, json)))
  }
}

function shouldFetchCoins(state, serie) {
  const coins = state.coins[serie]
  if (!coins) {
    return true
  } else if (coins.isFetching) {
    return false
  } else {
    return coins.didInvalidate
  }
}

export function fetchCoinsIfNeeded(serie) {
  return (dispatch, getState) => {
    if (shouldFetchCoins(getState(), serie)) {
      return dispatch(fetchCoins(serie))
    }
  }
}


