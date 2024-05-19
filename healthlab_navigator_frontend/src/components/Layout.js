import Header from "./Header";
import Footer from "./Footer";
import NotificationContainer from "react-notifications/lib/NotificationContainer";
import { useGeolocated } from "react-geolocated";

function Layout({children, title="HealthLab Navigator"}) {

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
