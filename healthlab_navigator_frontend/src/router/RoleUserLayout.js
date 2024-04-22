import React from 'react';
import {isRole} from "../hooks/user.actions";
import {Navigate} from "react-router-dom";
import UserLayout from "./UserLayout";

function RoleUserLayout({children_for_patient}) {
  return (
    <UserLayout children_for_user=
      {isRole("patient") ? children_for_patient : <Navigate to="/" /> }
    />
  )
}
export default RoleUserLayout;