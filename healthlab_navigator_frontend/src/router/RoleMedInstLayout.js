import React, {useEffect} from 'react';
import {Navigate} from "react-router-dom";
import {getRole, isAuth, isRole, setRole} from "../hooks/user.actions";
import UserLayout from "./UserLayout";
import getData from "../requests/getData";

function RoleMedInstLayout({children_for_med_inst}) {
  return (
      <UserLayout>
        {isRole("medical_institution_agent") ? children_for_med_inst : <Navigate to={'/error'} replace={true} />}
      </UserLayout>
    )
}
export default RoleMedInstLayout;