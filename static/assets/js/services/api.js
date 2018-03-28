import {callApi} from 'utils';


export const fetchSeries = () => (
  callApi('series/');
);

export const fetchCatalogCoins = (serie) => (
  callApi('catalogue/', params={'serie__name': serie});
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
