import React from 'react';
import {Navigate} from "react-router-dom";
import {isRole} from "../hooks/user.actions";
import UserLayout from "./UserLayout";

function RoleMedInstLayout({children}) {
  return (
      <UserLayout>
        {isRole("med_inst") ? {children} : <Navigate to={'/error'} replace={true} />}
      </UserLayout>
    )
}
export default RoleMedInstLayout;