import React from 'react';


export default class Profile extends React.Component {
  constructor(props) {
    super(props);
    this.state = {username: getUsername()};
  }

  render() {
    return (
      <div>
      </div>
    )
  }
}
