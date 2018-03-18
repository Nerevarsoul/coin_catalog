import React from 'react';


let statuses = [
  'in_collection', 'for_exchange', 'in_wishlist',
] 

const StatusList = ({ func }) => (
  <div>
    {statuses.map((status, index) =>
       <li key={index}
           onClick={ () => func(status) }>
         {status}
       </li>
    )}
  </div>
)

export default StatusList
