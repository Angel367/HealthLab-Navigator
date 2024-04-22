import {useEffect, useState} from "react";
import getData from "../../requests/getData";

function Profile() {
    const [userData, setUserData] = useState(null);
    useEffect(() => {
        async function fetchUser() {
            const response = await getData('/api/profile/');
            setUserData(response.data);
        }
        fetchUser();
        // return userData;
    }, []);
    // console.log(userData)
    return (
        <div>
            <h1>Профиль</h1>
            <p>Ваш профиль</p>
            <p>Имя: {userData?.first_name}</p>
            <p>Фамилия: {userData?.last_name}</p>
            <p>Почта: {userData?.email}</p>
            <p>Телефон: {userData?.phone_number}</p>
            <p>ROLE: {userData?.user_type}</p>
        </div>
    );
}
export default Profile;