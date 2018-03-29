import { authPost } from '../utils';

export const REQUEST_AUTH = 'REQUEST_AUTH';
export const FAILURE_AUTH = 'FAILURE_AUTH';
export const SUCCESS_AUTH = 'SUCCESS_AUTH';


function requestAuth() {
  return {
    type: REQUEST_AUTH
  }
}


function receiveAuth(json) {
  return {
    type: SUCCESS_AUTH,
    token: json,
    receivedAt: Date.now()
  }
}


function login(password, username) {
  return dispatch => {
    dispatch(requestAuth())
    return authPost({'password': password, 'username': username})
      .then(json => dispatch(receiveAuth(json)))
  }
}
