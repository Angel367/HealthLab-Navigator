import Cookies from "js-cookie";

function isAuth() {
 return getAccessToken() !== null && getAccessToken() !== undefined;
}
function isRole(role) {
    if (getRole() === undefined)
        return false;
    if (role?.medical_institution !== undefined)
        return getRole() === role.role && (getMedicalInstitution() == role.medical_institution);
    return getRole() === role;
}

function getRole() {
    return Cookies.get("role");
}
function getMedicalInstitution() {
    return Cookies.get("medical_institution");
}
// Get the access token
function getAccessToken() {
 return Cookies.get("access");
}
// Get the refresh token
function getRefreshToken() {
 return Cookies.get("refresh");
}

function setRole(role)
{
    if (role.medical_institution !== undefined)
        Cookies.set("medical_institution", role.medical_institution, { expires: 1})
    Cookies.set("role", role.role || role, { expires: 1 });
        // Cookies.set("medical_institution", role.medical_institution, { expires: 1, secure: true })
    // Cookies.set("role", role.role || role, { expires: 1, secure: true });
}
// Set the access, token and user property
function setUserData(data) {
    Cookies.set("access", data.access, { expires:  1});
    Cookies.set("refresh", data.refresh, { expires: 1});
    // Cookies.set("access", data.access, { expires:  1, secure: true });
    // Cookies.set("refresh", data.refresh, { expires: 1, secure: true });
}
 // Logout the user
 function logout() {
    Cookies.remove("access");
    Cookies.remove("refresh");
    Cookies.remove("role");
    if (Cookies.get("medical_institution") !== undefined)
        Cookies.remove("medical_institution");

 }
 export {isAuth, getAccessToken, getRefreshToken, setUserData, logout, isRole, setRole, getRole};