import axios from 'axios'

export const HTTP = axios.create({
  baseURL: process.env.API_BASE_URL
  // baseURL: 'http://localhost:8000'
})
