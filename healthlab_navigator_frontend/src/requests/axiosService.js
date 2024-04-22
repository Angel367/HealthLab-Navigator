import axios from "axios";
import createAuthRefreshInterceptor from "axios-auth-refresh";
import {getAccessToken, getRefreshToken, logout} from "../hooks/user.actions";
import Cookies from 'js-cookie';

const axiosService = axios.create(
        {
            baseURL: process.env.REACT_APP_HOST + "/api/auth/token/verify/",
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
        const {refresh} = refreshRes;
        const {access} = accessRes;
        return axios.post(
            "/api/auth/token/refresh/",
            null,
            {
                baseURL: process.env.REACT_APP_HOST ,
                withCredentials: true,
                headers: {
                    Authorization: `Bearer ${access}`,
                },
                body: {
                    refresh: refresh
                }
    ,})
    .then((resp) => {
        const { access, refresh } = resp.data;
        failedRequest.response.config.headers["Authorization"] = "Bearer " + access;
        Cookies.set('access', access, { expires: 1, secure: true });
        Cookies.set('refresh', refresh, { expires: 7, secure: true });
    })
    .catch(() => {
        logout();
    });
     }
    else {
        logout();
    }
}
createAuthRefreshInterceptor(axiosService,  refreshAuthLogic);
// export function fetcherUser() {
//  return axiosService.get(getBaseUrl() + 'auth/update/').then((res) => res.data)
//         .catch((error) => {
//             if (error.response.status === 401) {
//                 logout();
//             }
//             return error.response.data;
//         });
// }
// export async function updateUser(data) {
//  return await axiosService.put( process.env.REACT_APP_HOST + '/api/auth/update/', data)
//      .then((res) => res.data)
//      .catch((error) => {
//             if (error.response.status === 401) {
//                 logout();
//             }
//          return error.response.data;
//      });
// }
export default axiosService;
