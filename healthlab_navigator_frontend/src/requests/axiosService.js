import axios from "axios";
import createAuthRefreshInterceptor from "axios-auth-refresh";
import {getAccessToken, getRefreshToken, logout, setUserData} from "../hooks/user.actions";

const axiosService = axios.create(
        {
            baseURL: process.env.REACT_APP_HOST,
            withCredentials: true,
            headers: {
                "Content-Type": "application/json",
            },
        }
    );
axiosService.interceptors.request.use(
    async (config) => {
         config.headers.Authorization = `Bearer ${getAccessToken()}`;
         return config;
});

axiosService.interceptors.response.use(
 (res) => Promise.resolve(res),
 (err) => Promise.reject(err),
);

const refreshAuthLogic = async (failedRequest) => {
    const  refreshRes  = getRefreshToken();
    const accessRes = getAccessToken();
     if (refreshRes && accessRes){
        return axiosService.post(
            "/api/auth/token/refresh/",
            { refresh: refreshRes },
        )
    .then((resp) => {
        const { access, refresh } = resp.data;
        failedRequest.response.config.headers["Authorization"] = "Bearer " + access;
        setUserData({access, refresh});
    })
    .catch((ex) => {
        // console.log(ex)
        logout();
    });
     }
    else {
        // console.log("no refresh token found. Logging out.")
        logout();
    }
}
createAuthRefreshInterceptor(axiosService,  refreshAuthLogic);
export default axiosService;
