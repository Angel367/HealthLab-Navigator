import Header from "./Header";
import Footer from "./Footer";
import NotificationContainer from "react-notifications/lib/NotificationContainer";

function Layout({children, title="HealthLab Navigator"}) {
    // console.log(children);
    document.title = title;
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
