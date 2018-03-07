/* eslint-disable */
import { HTTP }  from './common'

export const User = {
  login (config) {
    return HTTP.post('/auth/', config)
    .then( response => {
        return response
  })
    .catch( err => {
        return err
    })
}
}