import { callApi } from '../utils';


export const fetchSeries = () => (
  callApi('series/')
);

export const fetchCatalogCoins = (serie) => (
  callApi('catalogue/', {'serie__name': serie})
);

export const getCoins = (serie, stat, owner='d3698ffc-abc3-49b2-ac91-77f5273ccc2a') => (
  callApi('coins/', {'serie__name': serie, 'owner': owner})
    .then(res => res.json())
);

export const authPost = (body) => (
  callApi('auth/api-token-auth/', null, 'POST', data}
  ).then(res => res.json())
)
