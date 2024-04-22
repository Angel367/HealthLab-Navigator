import React from 'react';
import {isRole} from "../hooks/user.actions";
import {Navigate} from "react-router-dom";
import UserLayout from "./UserLayout";

function RoleUserLayout({children_for_patient}) {
  return (
    <UserLayout>
      {isRole("patient") ? children_for_patient : <Navigate to="/login" /> }
    </UserLayout>
  )
}
export default RoleUserLayout;