import React from 'react';
import { Link } from 'react-router-dom';

function Footer() {
  return (
    <footer className="bg-light py-4 border-top">
      <div className="container">
        <div className="row">
          <div className="col-md-3 mb-3">
            <h5>Навигация</h5>
            <ul className="list-unstyled">
              <li><Link to="/">Главная</Link></li>
              <li><Link to="/about">О нас</Link></li>
              <li><Link to="/partners">Партнеры</Link></li>
            </ul>
          </div>
          <div className="col-md-3 mb-3">
            <h5>Контакты</h5>
            <ul className="list-unstyled">
              <li><a href="tel:+7(495)123-45-67">Телефон: +7(495)123-45-67</a></li>
              <li><a href="mailto:email@email.com">Email: email@email.com</a></li>
            </ul>
          </div>
          <div className="col-md-3 mb-3">
            <h5>Пользователям</h5>
            <ul className="list-unstyled">
              <li><Link to="/">Политика конфиденциальности</Link></li>
              <li><Link to="/">Пользовательское соглашение</Link></li>
              <li><Link to="/">Помощь</Link></li>
            </ul>
          </div>
          <div className="col-md-3 mb-3">
            <h5>Поиск по сайту</h5>
            <ul className="list-unstyled">
              <li><Link to="/laboratory">Лаборатории</Link></li>
              <li><Link to="/analysis">Анализы</Link></li>
            </ul>
          </div>
        </div>
        <div className="text-center mt-4">
          &copy; 2024 HealthLab Navigator
        </div>
      </div>
    </footer>
  );
}

export default Footer;

