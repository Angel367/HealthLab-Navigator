import React, {useEffect} from 'react';
import {getRole, isAuth, setRole} from "../hooks/user.actions";
import {Navigate} from "react-router-dom";
import getData from "../requests/getData";

function UserLayout({children_for_user}) {
    useEffect(() => {
        if (!isAuth()) {
            return <Navigate to={'/login'} replace={true}/>
        } if (!getRole()) {
            async function fetchUserRole() {
                const response = await getData('/api/profile/');
                setRole(response.data?.user_type);
            }

            fetchUserRole();
        }
    }, []);
  return (
    <div>
      {isAuth() ? children_for_user : <Navigate to={'/login'} replace={true} />}
    </div>)
}
export default UserLayout;