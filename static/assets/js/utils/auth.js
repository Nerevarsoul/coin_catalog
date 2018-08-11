export const getToken = () => localStorage.getItem('Token');
export const setToken = (value) => localStorage.setItem('Token', value);
export const removeToken = () => localStorage.removeItem('Token');

export const getUsername = () => {
  if (getToken) {
    localStorage.getItem('Username');
  }
}
export const setUsername = (value) => localStorage.setItem('Username', value);
export const removeUsename = () => localStorage.removeItem('Username');


export const Login = (token, username) => {
  setToken(token);
  setUsername(username);
}

export const Logout = () => {
  removeToken();
  removeUsename();
}
