import React from 'react';
import {isAuth, isRole} from "../hooks/user.actions";
import {Navigate} from "react-router-dom";

function UserLayout({children_for_user, role=undefined}) {
  console.log(role, isAuth(), isRole(role));
  return (
    <div>
      {role === undefined && isAuth() || isRole(role)
          ? children_for_user : <Navigate to={'/login'} replace={true} />}
    </div>)
}
export default UserLayout;