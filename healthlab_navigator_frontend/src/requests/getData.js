import axios, {AxiosError} from "axios";

async function getData(urlPart, params) {
    let url = process.env.REACT_APP_HOST + urlPart;
    return await axios.get(url,
        {
            params: params,
            withCredentials: true,
            headers: {
                'Content-Type': 'application/json',
            }
        }
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
export default getData;