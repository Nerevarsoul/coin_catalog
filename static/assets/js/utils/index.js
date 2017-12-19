import 'whatwg-fetch';

let apiUrl = 'http://185.12.95.205:8000/api'

apiCall(endpoint) {
  fetch(`${apiUrl}${endpoint}`)
  .then(res => res.json())
  .then(res => return res)
}

