import 'whatwg-fetch';

const API_URL = 'http://185.12.95.205:8000/api/';

export const getToken = () => localStorage.getItem('Token')
export const setToken = (value) => localStorage.setItem('Token', value)
export const removeToken = () => localStorage.removeItem('Token');


function getUrl(serie, stat, owner) {
  let url = `${apiUrl}coins?catalog_coin__serie__name=${serie}&owner=${owner}`
  if (stat) {
    url = url + `&status=${stat}`
  }
  return url
}

function apiCall(endpoint) {
  fetch(`${API_URL}${endpoint}`)
    .then(res => res.json())
}

export const callApi = function(endPoint, method='GET', payload=null) {
  const options = {
    method: method.toUpperCase(),
    headers: headers,
    body: payload ? JSON.stringify(payload) : undefined,
    credentials: 'same-origin',
    mode: 'same-origin',
    redirect: 'follow',
    cache: 'no-cache'
  }

  return fetch(${API_URL}/${endPoint}, options)
    .then(res => res.json())
}

export const fetchSeries = () => (
  fetch(`${apiUrl}series/`)
    .then(res => res.json())
);

export const fetchCatalogCoins = (serie) => (
  fetch(`${apiUrl}catalogue?serie__name=${serie}`)
    .then(res => res.json())
);

export const getCoins = (serie, stat, owner='d3698ffc-abc3-49b2-ac91-77f5273ccc2a') => (
  fetch(getUrl(serie, stat, owner))
    .then(res => res.json())
);

export const authPost = (body) => (
  fetch(`${apiUrl}auth/api-token-auth/`, {
    method: 'POST',
    body: data
  }).then(res => res.json())
)

export const headers = function () {
  let headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json; charset=utf-8'
  }

  const token = getToken()
  if (token) {
    headers['Authorization'] = `Token ${token}`
  }

  return headers
}

export function getQueryString(params) {
  const esc = encodeURIComponent
  return Object.keys(params)
    .filter(key => !!params[key])
    .map(key => esc(key) + '=' + esc(params[key]))
    .join('&')
}
