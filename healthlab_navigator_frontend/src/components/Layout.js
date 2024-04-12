import Header from "./Header";
import Footer from "./Footer";
import NotificationContainer from "react-notifications/lib/NotificationContainer";

function Layout({children}) {
    console.log(children);
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
