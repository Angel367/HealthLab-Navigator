import {Link} from "react-router-dom";
import {isAuth, logout} from "../hooks/user.actions";
import styles from "../styles/Header.module.css";
const logo_inline = process.env.PUBLIC_URL + '/logo_inline.jpg';
const profile = process.env.PUBLIC_URL + '/profile.svg';

function Header() {

  return (
            <header className={styles.app_header}>
                <Link to="/" className={styles.app_header__logo}>
                    <img src={logo_inline} alt="MedLabNaV"/>
                </Link>
                <label htmlFor="menu-toggle" className={styles.app_header__menu_icon_box}>
                    <span className={styles.app_header__menu_icon_object} />
                </label>
                <input type="checkbox" id="menu-toggle" className={styles.always_hidden}/>
                <nav className={styles.app_header__menu}>
                    <Link to="/laboratory" className={styles.app_header__menu__item}>Лаборатория</Link>
                    <Link to="/analysis" className={styles.app_header__menu__item}>Анализы</Link>
                    <Link to="/about" className={styles.app_header__menu__item}>О нас</Link>
                    {isAuth() ?
                        <Link to="/profile" className={styles.app_header__menu__item}>
                            <img src={profile} alt="Профиль"/>
                        </Link> : null}
                    {isAuth() ? <Link to="/login" onClick={logout} className={styles.app_header__menu__item}>Выход</Link> : null}
                    {!isAuth() ? <Link to="/login" className={styles.app_header__menu__item}>Вход</Link> : null}
                    {!isAuth() ? <Link to="/register" className={styles.app_header__menu__item}>Регистрация</Link> : null}
                </nav>
            </header>
  );
}

export default Header;
