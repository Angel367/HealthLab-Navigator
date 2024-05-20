
import AuthForm from "./AuthForm";

function Login() {

    return (
        <div>
           <AuthForm path="/api/auth/token/" buttonName="Войти"/>
        </div>
    );
}

export default Login;