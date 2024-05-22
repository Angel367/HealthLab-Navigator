import {Link} from "react-router-dom";
import {getRole, isAuth, isRole, logout} from "../hooks/user.actions";
const logo_inline = process.env.PUBLIC_URL + '/logo_inline.jpg';
const profile = process.env.PUBLIC_URL + '/profile.svg';
const statistics = process.env.PUBLIC_URL + '/statistics.svg';

const Header = () => (
  <header>
    <nav className="navbar navbar-expand-lg navbar-light bg-light py-3 border-bottom">
      <div className="container">
        <Link to="/" className="navbar-brand">
          <img src={logo_inline} alt="MedLabNaV" height="80"/>
        </Link>
        <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
          <span className="navbar-toggler-icon"></span>
        </button>
        <div className="collapse navbar-collapse" id="navbarNav">
          <ul className="navbar-nav ms-auto">

            <li className="nav-item">
                <Link to="/" className="nav-link">Поиск</Link>
            </li>
            <li className="nav-item">
              <Link to="/laboratory" className="nav-link">Лаборатории</Link>
            </li>

            <li className="nav-item">
              <Link to="/about" className="nav-link">О нас</Link>
            </li>
            <li className="nav-item">
                <Link to="/partners" className="nav-link">Партнеры</Link>
            </li>
            {isAuth() ? (
              <>
                <li className="nav-item">
                  <Link to="/profile" className="nav-link">
                    <img src={profile} alt="Профиль" height="30"/>
                  </Link>
                </li>
                {getRole() === 'agent' ? (
                    <li className="nav-item">
                        <Link to="/statistics" className="nav-link">
                            <img src={statistics} alt="Статистика" height="30"/>
                        </Link>
                    </li>
                    ) : null}
                <li className="nav-item">
                  <Link to="/login" onClick={logout} className="nav-link">Выход</Link>
                </li>


              </>
            ) : (
              <>
                <li className="nav-item">
                  <Link to="/login" className="nav-link">Вход</Link>
                </li>
                <li className="nav-item">
                  <Link to="/register" className="nav-link">Регистрация</Link>
                </li>
              </>
            )}
          </ul>
        </div>
      </div>
    </nav>
  </header>
);


export default Header;
