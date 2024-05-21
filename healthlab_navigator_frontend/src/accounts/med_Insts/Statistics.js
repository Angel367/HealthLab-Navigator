import getData from "../../requests/getData";
import {useEffect, useState} from "react";
import {isAuth} from "../../hooks/user.actions";
function Statistics() {
    const [statistics, setStatistics] = useState([]);

    useEffect(() => {
        const fetchStatistics = async () => {
            console.log('fetching statistics', isAuth());
            const response = await getData(`/api/visiting-medical-institution/1`);
            setStatistics(response.data);
        };
        fetchStatistics();
    }, []);
    if (statistics === undefined) {
        return <div>Loading...</div>
    }
    return (
        <div>
            <h1>Statistics</h1>
            <ul>
                {/*{statistics?.length > 0 &&*/}
                {/*    statistics.map((stat, index) => {*/}
                {/*    return (*/}
                {/*        <li key={index}>*/}
                {/*            <p>{stat.date}</p>*/}
                {/*            <p>{stat.visits}</p>*/}
                {/*        </li>*/}
                {/*    )*/}
                {/*})}*/}
            </ul>

        </div>
    );
}
export default Statistics;