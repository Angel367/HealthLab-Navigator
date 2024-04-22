import axios, {AxiosError} from "axios";
import axiosService from "./axiosService";
import {isAuth} from "../hooks/user.actions";

async function postData(urlPart, data) {
    let ax, config, url;
    if (isAuth()){
        ax = axiosService;
        config = {};
        url = urlPart;
    } else {
        ax = axios
        config = {

            withCredentials: true,
            headers: {
                'Content-Type': 'application/json',
            }
        }
         url = process.env.REACT_APP_HOST + urlPart;
    }

    return await ax.post(url,
        data,
        config
        // {
        //     withCredentials: true,
        //     headers: {
        //         'Content-Type': 'application/json',
        //
        //     }
        // }
    ).then((res) => {
        return {
            status: res.status,
            data: res.data
        };
    }
    ).catch((err) => {
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
export default postData;