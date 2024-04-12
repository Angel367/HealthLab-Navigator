
import {Link} from "react-router-dom";

function Footer() {
  return (
    <footer className="App-footer">
      <div className="App-footer__links-holder">
        <div className="App-footer__links-item">
          <div>Навигация</div>
          <Link to="/">Главная</Link>
          <Link to={'/about'}>О нас</Link>
          <Link to={'/partners'}>Партнеры</Link>

        </div>
        <div className="App-footer__links-item">
          <div>Контакты</div>
          <a href={'tel:+7(495)123-45-67'}>Телефон: +7(495)123-45-67</a>
          <a href={'mailto:email@email.com'}>Email: email@email.com</a>
        </div>
        <div className="App-footer__links-item">
          <div>Пользователям</div>
          <Link to={'/'}>Политика конфиденциальности</Link>
          <Link to={'/'}>Пользовательское соглашение</Link>
          <Link to={'/'}>Помощь</Link>
        </div>
      <div className="App-footer__links-item">
        <div>Поиск по сайту</div>
        <Link to={'/laboratory'}>Лаборатории</Link>
        <Link to={'/analysis'}>Анализы</Link>
        </div>
      </div>
      <div className="App-footer__copy">
        &copy; 2024 HealthLab Navigator
      </div>

    </footer>
  );
}

export default Footer;
