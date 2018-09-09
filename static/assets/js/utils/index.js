import 'whatwg-fetch';

import { getToken } from './auth';

const API_URL = 'http://185.12.95.205:8000/api';

export const callApi = function(endPoint, params=null, method='GET', payload=null) {
  const options = {
    method: method.toUpperCase(),
    headers: headers(),
    body: payload ? JSON.stringify(payload) : undefined,
    credentials: 'same-origin',
    mode: 'same-origin',
    redirect: 'follow',
    cache: 'no-cache'
  }

  let url = `${API_URL}/${endPoint}`;

  if (params) {
    url = url + '?' + getQueryString(params);
  }
  
  return fetch(url, options)
    .then(res => res.json())
};

export const headers = function () {
  let headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json; charset=utf-8'
  };

  const token = getToken();
  if (token) {
    headers['Authorization'] = `Token ${token}`
  };
  return headers
};

export function getQueryString(params) {
  const esc = encodeURIComponent;
  return Object.keys(params)
    .filter(key => !!params[key])
    .map(key => esc(key) + '=' + esc(params[key]))
    .join('&')
};
