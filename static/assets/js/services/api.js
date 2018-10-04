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

export const addCoin = (data) => (
  callApi('coins/', null, 'POST', data)
);

export const getCoins = (serie, owner) => (
  callApi('coins/', {'catalog_coin__serie__name': serie, 'owner': owner})
);

export const authPost = (data) => (
  callApi('auth/api-token-auth/', null, 'POST', data)
)
