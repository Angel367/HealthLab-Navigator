import './App.css';
import Header from "./Header";
import Footer from "./Footer";
import NotificationContainer from "react-notifications/lib/NotificationContainer";

function Layout({children}) {
  return (
    <div className="App">
        <Header/>
        <NotificationContainer/>

        {children}
      <Footer/>
    </div>
  );
}

export default Layout;
