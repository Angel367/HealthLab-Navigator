import {useEffect, useState} from "react";
import getData from "../../requests/getData";
import {setRole} from "../../hooks/user.actions";
import {Link} from "react-router-dom";


function Profile() {
    const [userData, setUserData] = useState(null);
    const [lab, setLab] = useState(null);
    useEffect(() => {
        async function fetchUser() {
            const response = await getData('/api/profile/');
            setUserData(response.data);
            if (response.data?.role?.role === "agent" || response.data?.role === "patient") {
                setRole(response.data.role);
            }
        }
        fetchUser();
    }, []);
    useEffect(() => {
        const fetchLaboratory = async () => {
            if (userData?.role?.role === "agent") {
                const response = await getData(`/api/medical-institution/${userData?.role?.medical_institution}/`);
                setLab(response.data);
            }
        }
        fetchLaboratory();
    }, [userData]);

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
                                <li className="list-group-item">Дата рождения: {userData?.date_of_birth}</li>
                                <li className="list-group-item">Пол: {userData?.gender}</li>
                                {lab && <li className="list-group-item">Лаборатория:
                                    <Link to={`/laboratory/${lab.id}`}>{lab.name}</Link>
                                </li>}
                            </ul>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    );
}

export default Profile;
