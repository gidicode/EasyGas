import axios from 'axios'
import authHeader from './auth-header';

const API_URL = 'http://localhost:8000/'
const currentUserId = JSON.parse(localStorage.getItem('user'))

class UserService {
    getLogedInUser(){
        return axios.get(API_URL + 'auth/users/' + currentUserId + '/', {headers: authHeader()})
    }
}

export default new UserService()