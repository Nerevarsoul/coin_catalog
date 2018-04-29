import { getCoins } from '../services/api';

export const REQUEST_COINS = 'REQUEST_COINS';
export const RECEIVE_COINS = 'RECEIVE_COINS';
export const SELECT_SERIE = 'SELECT_SERIE';


export function selectSerie(serie) {
  return {
    type: SELECT_SERIE,
    serie
  }
}

function requestCoins(serie, stat) {
  return {
    type: REQUEST_COINS,
    serie
  }
}

function receiveCoins(serie, json) {
  return {
    type: RECEIVE_COINS,
    serie,
    coins: json,
    receivedAt: Date.now()
  }
}

function fetchCoins(serie, stat) {
  return dispatch => {
    dispatch(requestCoins(serie, stat))
    return getCoins(serie, stat)
      .then(json => dispatch(receiveCoins(serie, json)))
  }
}

function shouldFetchCoins(state, serie) {
  const coins = state.coins
  if (!coins) {
    return true
  } else if (coins.isFetching) {
    return false
  } else {
    return coins.didInvalidate
  }
}

export function fetchCoinsIfNeeded(serie, stat) {
  return (dispatch, getState) => {
    if (shouldFetchCoins(getState(), serie)) {
      return dispatch(fetchCoins(serie, stat))
    }
  }
}


