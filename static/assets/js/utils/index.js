import 'whatwg-fetch';

let apiUrl = 'http://185.12.95.205:8000/api/'

function getUrl(serie, stat, owner) {
  let url = `${apiUrl}coins?catalog_coin__serie__name=${serie}&owner=${owner}`
  if (stat) {
    url = url + `&status=${stat}`
  }
  return url
}

function apiCall(endpoint) {
  fetch(`${apiUrl}${endpoint}`)
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

export const authByToken = (body) => (
  fetch(`${apiUrl}auth/api-token-auth/`, {
    method: 'POST',
    body: data
  }).then(res => res.json())
)
