/* eslint-disable prettier/prettier */
import axios from 'axios'
import authHeader from './auth-header';

const API_URL = 'http://localhost:8000/auth/users/'


class UserService {
    curentUser(){ 
        let userInstance = JSON.parse(localStorage.getItem('user'))
        let userId = userInstance.user_id
        return userId
    }

    getLogedInUser(){                        
        return axios.get(API_URL + this.curentUser() + '/', {headers: authHeader()})
    };

    completeRegistration(user) {        
        return axios.put(API_URL + this.curentUser() + '/' + 'completeRegistration/', 
        { 
            state: user.state,
            lga: user.lga,
            Address: user.address,
            phoneNumber: user.phoneNumber,
            reg_complete: user.reg_complete
        },
        {headers: authHeader()})
    };

    userEditProfile(user) {
        return axios.put(API_URL + this.curentUser() + '/' + 'editUser/', {
            state: user.state,
            lga:user.lga,
            Address: user.address,
            phoneNumber: user.phoneNumber,            
        },
        { headers: authHeader()})
    };

    changeProfilePicture(user, onUploadProgress) {                      
        return axios.put(API_URL + this.curentUser() + '/' + 'changeProfilePicture/', {
            profile_picture: user.profile_picture
        },
        {headers:{
            Authorization: authHeader().Authorization,
            "Content-Type": "multipart/form-data"
          }, onUploadProgress})
    };

    changePassword(user) {        
        return axios.put(API_URL + this.curentUser() + '/' + 'changePassword/', {
            password: user.password,
            password2: user.password2,
            old_password: user.oldPassword
        }, { headers: authHeader()})
    }
}

export default new UserService()