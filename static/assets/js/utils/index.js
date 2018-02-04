import 'whatwg-fetch';

let apiUrl = 'http://185.12.95.205:8000/api/'

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

export const getCoins = (serie, owner='d3698ffc-abc3-49b2-ac91-77f5273ccc2a') => (
  fetch(`${apiUrl}coins?serie__name=${serie}&owner=${owner}`)
    .then(res => res.json())
);
