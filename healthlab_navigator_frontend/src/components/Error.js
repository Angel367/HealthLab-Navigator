import {useRouteError} from "react-router-dom";

function Error() {
    const error = useRouteError();
    return (
        <div className={"d-flex flex-column align-items-center"}>
            {process.env.PRODUCTION === true ?
                (<div>
                        <h1>Something went wrong</h1>
                        <img src={"https://http.cat/404"}
                                alt={"Error 404"}/>

                </div>)
                        :
                (<div>
                        <h1>Something went wrong</h1>
                        <p>{error?.statusText || error?.message}</p>
                        <img src={"https://http.cat/404"}
                             alt={"Error 404"}/>
                    </div>
                )
            }
        </div>
    );
}

export default Error;