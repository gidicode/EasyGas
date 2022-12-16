/* eslint-disable prettier/prettier */
 import axios from "axios"
 import authHeader from "./auth-header"

const API_URL = "http://localhost:8000/vendor/"

class VenorService {
    creatVendor(vendor) {
      console.log(vendor, "hhhh")
        return axios.post(API_URL + "create-vendor-profile/", {
          business_name: vendor.businessName,
          opening_hours: vendor.openingHours,
          closing_hours: vendor.closingHours,
          gas_price: vendor.gasPrice,
          description:vendor.bio,
          vendor_profile_completed: vendor.vendorProfileCompleted
        }, 
        {headers: authHeader()})
    }
}

export default new VenorService()