import { callApi } from '../utils';


export const fetchCountries = () => (
  callApi('countries/')
);

export const fetchSeries = (country) => (
  callApi('series/', {'country': country})
);

export const fetchCatalogCoins = (serie, page) => (
  callApi('catalogue/', {'serie__name': serie, 'page': page})
);

export const getCoins = (serie, stat, owner='d3698ffc-abc3-49b2-ac91-77f5273ccc2a') => (
  callApi('coins/', {'catalog_coin__serie__name': serie, 'owner': owner})
);

export const authPost = (body) => (
  callApi('auth/api-token-auth/', null, 'POST', data)
)
