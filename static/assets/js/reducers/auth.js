const initialUsernameState = {
  username: '',
}

export function usernameReducer(state = initialUsernameState, action) {
  switch (action.type) {
    case 'SUCCESS_AUTH':
      return { ...state, username: action.username }

    default:
      return state
  }
}