/* eslint-disable prettier/prettier */
export default function authHeader() {
    let user = JSON.parse(localStorage.getItem("token"))
    if (user && user.access) {
        console.log('user token',user)
        return {
            Authorization: 'Bearer' + user.access
        }
    } else {
        return {}
    }
}