import Cookies from "js-cookie";

function isAuth() {
 return getAccessToken() !== null && getAccessToken() !== undefined;
}
function isRole(role) {
    return getRole() === role;
}

// Get the access token
function getAccessToken() {
 return Cookies.get("access");
}
// Get the refresh token
function getRefreshToken() {
 return Cookies.get("refresh");
}
function getRole() {
 return Cookies.get("role");
}
function setRole(role) {
 Cookies.set("role", role);
}
// Set the access, token and user property
function setUserData(data) {
 Cookies.set("access", data.access, { expires: 1, secure: true });
 Cookies.set("refresh", data.refresh, { expires: 7, secure: true });
 // Cookies.set("role", data.role);

}
 // Logout the user
 function logout() {
    Cookies.remove("access");
    Cookies.remove("refresh");
    Cookies.remove("role");
    window.location.reload();
 }
 export {isAuth, getAccessToken, getRefreshToken, setUserData, logout, getRole, isRole, setRole};