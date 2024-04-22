import {useState} from "react";
import postData from "../../requests/postData";
import {NotificationManager} from "react-notifications";
import {useNavigate} from "react-router-dom";
import AuthForm from "./AuthForm";

function Login() {

    return (
        <div>
           <AuthForm path="/api/auth/token/" buttonName="Войти"/>
        </div>
    );
}

export default Login;