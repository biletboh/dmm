/* eslint-disable */
import { HTTP }  from './common'

export const Comment = {
  update (id, data, token) {
    return HTTP.put('/comment/'+id, data, {
      headers: {
        'Authorization': 'Token ' + token
      }
    })
    .then( response => {
      return response
    })
  }
}