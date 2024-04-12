import React from 'react';
import {isRole} from "../hooks/user.actions";
import {Navigate} from "react-router-dom";
import UserLayout from "./UserLayout";

function RoleUserLayout({children}) {
  return (
    <UserLayout>
      {isRole("user") ? children : <Navigate to="/login" /> }
    </UserLayout>
  )
}
export default RoleUserLayout;