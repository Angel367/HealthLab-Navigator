
import AuthForm from "./AuthForm";

function Register() {


    return (
        <div>
            <AuthForm path="/api/auth/register/" buttonName="Зарегистрироваться"/>
        </div>
    );
}
export default Register;