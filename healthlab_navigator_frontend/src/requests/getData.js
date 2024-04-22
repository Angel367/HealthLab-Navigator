import axios, {AxiosError} from "axios";
import axiosService from "./axiosService";
import {isAuth} from "../hooks/user.actions";

async function getData(urlPart, params) {
    let ax, config, url;
    if (isAuth()){
        url = urlPart;
        ax = axiosService;
        config = {
            params: params
        }
    } else {
        url = process.env.REACT_APP_HOST + urlPart;
        ax = axios
        config = {
            params: params,
            withCredentials: true,
            headers: {
                'Content-Type': 'application/json',
            }
        }
    }

    return await ax.get(url, config)
        .then((res) => {
            return {
                status: res.status,
                data: res.data
            };
        })
        .catch((err) => {
        if (err instanceof AxiosError) {
            const errors = err.response.data
            return {
                status: err.response.status,
                data: errors
            }
        }
        else {
            return {
                status: 500,
                data: err.message
            }
        }
    });

}
export default getData;