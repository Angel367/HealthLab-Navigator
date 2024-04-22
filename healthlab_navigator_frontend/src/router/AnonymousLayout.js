import React from 'react';
import {isAuth} from "../hooks/user.actions";
import {Navigate} from "react-router-dom";

function AnonymousLayout({children_for_anonymous}) {
  return (
    <div>
      {!isAuth() ? children_for_anonymous : <Navigate to={'/'} replace={true} />}
    </div>)
}
export default AnonymousLayout;