import {useState} from "react";
import {useNavigate} from "react-router-dom";
import postData from "../../requests/postData";
import {NotificationManager} from "react-notifications";
import {setUserData} from "../../hooks/user.actions";

function AuthForm({path="login/", buttonName="Войти"}) {
    // console.log(path);
    const [form, setForm] = useState({});
    const navigate = useNavigate();
    const handleSubmit = async (event) => {
        event.preventDefault();

        const data = {
            phone_number: form.phone_number,
            password: form.password
        }
        console.log(data);
        const authForm = await postData(path, data);
        if (authForm.status === 201 || authForm.status === 200) {
            NotificationManager.success("Вы успешно зарегистрировались", "Успешная регистрация", 5000);
            navigate('/profile');
            console.log("success");
            setUserData(authForm.data);
        } else {
            NotificationManager.error("Произошла ошибка. Попробуйте позже", "Ошибка auth", 5000);
            console.log(authForm.data);
        }
    }
    return (
        <form method={"POST"} onSubmit={handleSubmit}>
        <label htmlFor="username">Username:</label>
        <input
            id={"phone_number"}
            type="tel"
            placeholder="Ваш телефон..."
            required
            autoCorrect={"off"}
            autoCapitalize={"off"}
            spellCheck={"false"}
            autoComplete={"off"}
            onChange={(e) =>
                setForm({...form, phone_number: e.target.value})}
        />
        <label htmlFor="password">Password:</label>
        <input type="password" id="password"
               name="password"
               minLength={8}
               required
               onChange={(e) =>
                   setForm({...form, password: e.target.value})}/>
        <button type={"submit"}
                id={"submitAuth"}
                onSubmit={handleSubmit}>
            {buttonName}
        </button>
    </form>)

}

export default AuthForm;