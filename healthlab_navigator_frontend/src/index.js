import React from 'react';
import ReactDOM from 'react-dom/client';
import Layout from './components/Layout';
import Error from './components/Error';
import {createBrowserRouter, RouterProvider} from "react-router-dom";
import AnonymousLayout from "./router/AnonymousLayout";
import UserLayout from "./router/UserLayout";
import RoleMedInstLayout from "./router/RoleMedInstLayout";
import Main from "./main/Main";
import Login from "./accounts/auth/Login";
import Register from "./accounts/auth/Register";
import About from "./main/About";
import ProfileEdit from "./accounts/auth/ProfileEdit";
import Profile from "./accounts/users/Profile";
import LaboratoryEdit from "./accounts/med_Insts/LaboratoryEdit";
import Laboratory from "./agregator/Laboratory";
import Analysis from "./agregator/Analysis";
import AnalysisEdit from "./accounts/med_Insts/AnalysisEdit";
import AnalysisPage from "./agregator/AnalysisPage";
import LaboratoryPage from "./agregator/LaboratoryPage";
import Partners from "./main/Partners";

const analysis = {
        path: 'analysis/',
        errorElement: <Layout children={<Error/>}/>,
        children: [
            {
                path: ':id_analysis/',
                errorElement: <Layout children={<Error/>}/>,
                children: [
                    {
                        index: true,
                        element: <Layout children={<AnalysisPage/>}/>,
                        errorElement: <Layout children={<Error/>}/>,
                    },
                    {
                        path: 'edit',
                        element: <Layout children={<RoleMedInstLayout children_for_med_inst={<AnalysisEdit/>}/>}/>,
                        errorElement: <Layout children={<Error/>}/>,

                    }
                    ]
            },

            {
                index: true,
                element: <Layout children={<Analysis/>}/>,
                errorElement: <Layout children={<Error/>}/>,
            },
            {
                path: 'create',
                element: <Layout children={<RoleMedInstLayout children_for_med_inst={<AnalysisEdit/>}/>}/>,
                errorElement: <Layout children={<Error/>}/>,
            }

        ],
    };

const laboratory = {
        path: '/laboratory/',
        errorElement: <Layout children={<Error/>}/>,
        children: [
            {
                path: ':id_laboratory/',
                errorElement: <Layout children={<Error/>}/>,
                children: [
                    analysis,
                    {
                        path: 'edit',
                        element: <Layout children={<RoleMedInstLayout children_for_med_inst={<LaboratoryEdit/>}/>} title={"edit"}/>,
                        errorElement: <Layout children={<Error/>}/>,
                    },
                    {
                        index: true,
                        element: <Layout children={<LaboratoryPage/>}/>,
                        errorElement: <Layout children={<Error/>}/>,
                    }
                ]
            },
            {
                index: true,
                element: <Layout children={<Laboratory/>}/>,
                errorElement: <Layout children={<Error/>}/>,
            },
            {
                path: 'create',
                element: <Layout children={<RoleMedInstLayout children_for_med_inst={<LaboratoryEdit/>}/>}/>,
                errorElement: <Layout children={<Error/>}/>,
            }
            ]
    };


const router = createBrowserRouter([
    {
        index: true,
        element: <Layout children={<Main/>}/>,
        errorElement: <Layout children={<Error/>}/>,
    },
    {
        path: '/login',
        element: <Layout children={<AnonymousLayout children_for_anonymous={<Login/>}/>} title={"log"}/>,
        errorElement: <Layout children={<Error/>}/>,
    },
    {
       path: '/register',
        element: <Layout children={<AnonymousLayout children_for_anonymous={<Register/>}/>} title={"reg"}/>,
        errorElement: <Layout children={<Error/>}/>,
    },
    {
        path: '/about',
        element: <Layout children={<About/>}/>,
        errorElement: <Layout children={<Error/>}/>,

    },
    {
        path: '/partners',
        element: <Layout children={<Partners/>}/>,
        errorElement: <Layout children={<Error/>}/>,
    },
    analysis,
    laboratory,
    {
        path: '/profile/',
        errorElement: <Layout children={<Error/>}/>,
        children: [
            {
                path: 'edit',
                element: <Layout children={<UserLayout children_for_user={<ProfileEdit/>}/>}/>,
                errorElement: <Layout children={<Error/>}/>,
            },
            {
                index: true,
                element: <Layout children={<UserLayout children_for_user={<Profile/>}/>}/>,
                errorElement: <Layout children={<Error/>}/>,
            },
        ],
    },


    {
        path: '/error',
        element: <Layout children={<Error/>}/>,
        errorElement: <Layout children={<Error/>}/>,
    },

    ]
);
const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
    <React.StrictMode>
        <RouterProvider router={router}/>
    </React.StrictMode>
);


