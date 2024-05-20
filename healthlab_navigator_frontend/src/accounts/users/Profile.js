import {useEffect, useState} from "react";
import getData from "../../requests/getData";
import {Link} from "react-router-dom";


function Profile() {
    const [userData, setUserData] = useState(null);

    useEffect(() => {
        async function fetchUser() {
            const response = await getData('/api/profile/');
            setUserData(response.data);
        }
        fetchUser();
    }, []);

    return (
        <div className="container mt-5">
            <div className="row justify-content-center">
                <div className="col-md-8">
                    <div className="card">
                        <div className="card-header d-flex justify-content-between align-items-center">
                            <h1 className="card-title">Профиль</h1>
                            <Link to={'/profile/edit'} className="btn btn-primary">Редактировать</Link>
                        </div>
                        <div className="card-body">

                            <ul className="list-group list-group-flush">
                                <li className="list-group-item">Имя: {userData?.first_name}</li>
                                <li className="list-group-item">Фамилия: {userData?.last_name}</li>
                                <li className="list-group-item">Почта: {userData?.email}</li>
                                <li className="list-group-item">Телефон: {userData?.phone_number}</li>
                            </ul>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    );
}

export default Profile;
