import React, {useEffect} from 'react';
import {getRole, isAuth, setRole} from "../hooks/user.actions";
import {Navigate} from "react-router-dom";
import getData from "../requests/getData";

function UserLayout({children_for_user}) {
    console.log(!isAuth(), !getRole() || getRole() === undefined)
    useEffect(() => {
       if (isAuth() && (!getRole() || getRole() === undefined)){
            async function fetchUserRole() {
                const response = await getData('/api/profile/');
                setRole(response.data?.user_type);
            }
            fetchUserRole();
            // return getRole();
        }
    }, []);
  return (
    <div>
      {isAuth() ? children_for_user : <Navigate to={'/login'} replace={true} />}
    </div>)
}
export default UserLayout;