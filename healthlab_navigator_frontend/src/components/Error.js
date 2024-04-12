import {useRouteError} from "react-router-dom";

function Error() {
    const error = useRouteError();
    return (
        <div>
            {process.env.PRODUCTION === true ?
                (<div>
                        <h1>Something went wrong</h1>
                        <p>Try refreshing the page</p>
                </div>)
                        :
                (<div>
                    <h1>Something went wrong</h1>
                    <p>{error.statusText || error.message}</p>
                </div>
                )
            }
        </div>
    );
}
export default Error;