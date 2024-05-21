import React from 'react';
import Header from './Header';
import Footer from './Footer';

import { NotificationContainer } from 'react-notifications';
import {useLocation} from "react-router-dom";

function Layout({ children, title = "HealthLab Navigator" }) {
  const {hash} = useLocation();
  const scroll = () => {
    if (hash === '') {
      window.scrollTo(0, 0);
    } else {
      let el = document.getElementById(hash.slice(1));
      console.log(el, hash);
      if (el) {
        el.scrollIntoView({behavior: "smooth", block: "start"});
      } else {
        window.scrollTo(0, 0);
      }
    }
  };
  // console.log(hash);
    React.useEffect(() => {
    document.title = title;
    scroll();
  }, [hash, title]);

  return (
    <div className="d-flex flex-column min-vh-100">
      <Header />
      <NotificationContainer />
      <main className="flex-grow-1">
        {children}
      </main>
      <Footer />
    </div>
  );
}

export default Layout;

