import React from 'react';
import {isAuth} from "../hooks/user.actions";
import {Navigate} from "react-router-dom";

function UserLayout({children}) {
  return (
    <div>
      {isAuth() ? {children} : <Navigate to={'/login'} replace={true} />}
    </div>)
}
export default UserLayout;