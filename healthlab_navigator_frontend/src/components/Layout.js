import React from 'react';
import Header from './Header';
import Footer from './Footer';
import { NotificationContainer } from 'react-notifications';

function Layout({ children, title = "HealthLab Navigator" }) {
  React.useEffect(() => {
    document.title = title;
  }, [title]);

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

