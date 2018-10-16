import { authPost } from '../services/api';
import { Login } from '../utils/auth';

export const REQUEST_AUTH = 'REQUEST_AUTH';
export const FAILURE_AUTH = 'FAILURE_AUTH';
export const SUCCESS_AUTH = 'SUCCESS_AUTH';


function login(username, password) {
  return dispatch => {
    dispatch(REQUEST_AUTH)
    authPost({'username': username, 'password': password}).then(
      res => {
        Login(res['token'], data["username"]);
        dispatch({
          type: SUCCESS_AUTH,
          payload: data["username"]
        })
      },
      err => {
        console.log(err);
      }
    )
  }
}
