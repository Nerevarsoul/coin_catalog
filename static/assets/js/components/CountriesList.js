import React from 'react';
import { Select } from 'semantic-ui-react';


const CountriesList = ({ countries, func }) => (
  <Select placeholder='Select your country' options={countries} />
)

export default CountriesList