import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import postData from '../../requests/postData';
import { NotificationManager } from 'react-notifications';
import { setUserData } from '../../hooks/user.actions';

function AuthForm({ path = "login/", buttonName = "Войти" }) {
  const [form, setForm] = useState({});
  const navigate = useNavigate();

  const handleSubmit = async (event) => {
    event.preventDefault();

    const data = {
      phone_number: form.phone_number,
      password: form.password
    };

    const authForm = await postData(path, data);
    if (authForm.status === 201 || authForm.status === 200) {
      navigate('/profile');
      setUserData(authForm.data);
    } else {
      NotificationManager.error("Произошла ошибка. Попробуйте позже", "Ошибка auth", 5000);
    }
  };

  return (
    <form method="POST" onSubmit={handleSubmit} className="container mt-4">
      <div className="mb-3">
        <label htmlFor="phone_number" className="form-label">Телефон:</label>
        <input
          id="phone_number"
          type="tel"
          className="form-control"
          placeholder="Ваш телефон..."
          required
          autoCorrect="off"
          autoCapitalize="off"
          spellCheck="false"
          autoComplete="off"
          onChange={(e) => setForm({ ...form, phone_number: e.target.value })}
        />
      </div>
      <div className="mb-3">
        <label htmlFor="password" className="form-label">Пароль:</label>
        <input
          type="password"
          id="password"
          name="password"
          className="form-control"
          minLength={8}
          required
          onChange={(e) => setForm({ ...form, password: e.target.value })}
        />
      </div>
      <button type="submit" id="submitAuth" className="btn btn-success">
        {buttonName}
      </button>
    </form>
  );
}

export default AuthForm;
