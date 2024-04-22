import {Link} from "react-router-dom";
import {isAuth, logout} from "../hooks/user.actions";

function Header() {
  return (
    <header className="App-header">
        <div className="App-header__logo">
          <Link to="/">HealthLab Navigator</Link>
        </div>
        <label htmlFor="menu-toggle" className="App-header__menu-icon">
          <span></span>
        </label>
        <input type="checkbox" id="menu-toggle"/>
        <div className="App-header__nav">
            <Link to="/laboratory">Лаборатории</Link>
            <Link to="/analysis">Анализы</Link>
            <Link to="/about">О нас</Link>
            {isAuth() ? <Link to="/profile">Профиль</Link> : null}
            {isAuth() ? <a href="#" onClick={logout}>Logout</a> : null}
            {!isAuth() ? <Link to="/login">Login</Link> : null}
            {!isAuth() ? <Link to="/register">Register</Link> : null}
        </div>
    </header>
  );
}

export default Header;
