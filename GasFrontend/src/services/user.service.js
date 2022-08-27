/* eslint-disable prettier/prettier */
import axios from 'axios'
import authHeader from './auth-header';

const API_URL = 'http://localhost:8000/'


class UserService {
    curentUser(){ 
        let userInstance = JSON.parse(localStorage.getItem('user'))
        let userId = userInstance.user_id
        return userId
    }

    getLogedInUser(){                        
        return axios.get(API_URL + 'auth/users/' + this.curentUser() + '/', {headers: authHeader()})
    };

    completeRegistration(user) {        
        return axios.put(API_URL + 'auth/users/' + this.curentUser() + '/' + 'completeRegistration/', 
        { 
            state: user.state,
            lga: user.lga,
            Address: user.address,
            phoneNumber: user.phoneNumber,
            reg_complete: user.reg_complete
        },
        {headers: authHeader()})
    }
}

export default new UserService()