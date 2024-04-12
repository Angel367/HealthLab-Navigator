import React from 'react';
import {isAuth} from "../hooks/user.actions";
import {Navigate} from "react-router-dom";

function AnonymousLayout({children}) {
  return (
    <div>
      {!isAuth() ? {children} : <Navigate to={'/'} replace={true} />}
    </div>)
}
export default AnonymousLayout;