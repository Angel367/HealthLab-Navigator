import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import Layout from './components/Layout';
import Error from './components/Error';
import {createBrowserRouter, RouterProvider} from "react-router-dom";
import AnonymousLayout from "./router/AnonymousLayout";
import UserLayout from "./router/UserLayout";
import RoleMedInstLayout from "./router/RoleMedInstLayout";
import Index from "./main";
import Login from "./accounts/auth/Login";
import Register from "./accounts/auth/Register";
import About from "./main/About";
import ProfileEdit from "./accounts/auth/ProfileEdit";
import Profile from "./accounts/users/Profile";
import LaboratoryEdit from "./accounts/med_Insts/LaboratoryEdit";
import Laboratory from "./agregator/Laboratory";
import Analysis from "./agregator/Analysis";

const analysis = {
        path: '/analysis',
        errorElement: <Layout children={<Error/>}/>,
        children: [
            {
                path: '/:id_analysis',
                element: <Layout children={<Analysis/>}/>,
                errorElement: <Layout children={<Error/>}/>,
            },
            {
                path: '/:id_analysis/edit',
                element: <Layout children={<RoleMedInstLayout children={<AnalysisEdit/>}/>}/>,
                errorElement: <Layout children={<Error/>}/>,
            },
            // {
            //     index: true,
            //     element: <Layout children={<Analysis/>}/>,
            //     errorElement: <Layout children={<Error/>}/>,
            // },
            {
                path: '/create',
                element: <Layout children={<RoleMedInstLayout children={<AnalysisEdit/>}/>}/>,
                errorElement: <Layout children={<Error/>}/>,
            }

        ],
    };

const laboratory = {
        path: '/laboratory',
        errorElement: <Layout children={<Error/>}/>,
        children: [
            {
                path: '/:id_laboratory',
                errorElement: <Layout children={<Error/>}/>,
                children: [
                    analysis,
                    {
                        path: '/edit',
                        element: <Layout children={<RoleMedInstLayout children={<LaboratoryEdit/>}/>}/>,
                        errorElement: <Layout children={<Error/>}/>,
                    },
                    {
                        index: true,
                        element: <Layout children={<Laboratory/>}/>,
                        errorElement: <Layout children={<Error/>}/>,
                    }
                ]
            },
            // {
            //     index: true,
            //     element: <Layout {<Laboratory/>}/>,
            //     errorElement: <Layout {<Error/>}/>,
            // },
            {
                path: '/create',
                element: <Layout children={<RoleMedInstLayout children={<LaboratoryEdit/>}/>}/>,
                errorElement: <Layout children={<Error/>}/>,
            }
            ]
    };


const router = createBrowserRouter([
    {
        index: true,
        element: <Layout children={<Index/>}/>,
        errorElement: <Layout children={<Error/>}/>,
    },
    {
        path: '/login',
        element: <Layout children={<AnonymousLayout children={<Login/>}/>}/>,
        errorElement: <Layout children={<Error/>}/>,
    },
    {
       path: '/register',
        element: <Layout children={<AnonymousLayout children={<Register/>}/>}/>,
        errorElement: <Layout children={<Error/>}/>,
    },
    {
        path: '/about',
        element: <Layout children={<About/>}/>,
        errorElement: <Layout children={<Error/>}/>,

    },
    analysis,
    laboratory,
    {
        path: '/profile',
        errorElement: <Layout children={<Error/>}/>,
        children: [
            {
                path: '/edit',
                element: <Layout children={<UserLayout children={<ProfileEdit/>}/>}/>,
                errorElement: <Layout children={<Error/>}/>,
            },
            {
                index: true,
                element: <Layout children={<UserLayout children={<Profile/>}/>}/>,
                errorElement: <Layout children={<Error/>}/>,
            },
        ],
    },


    {
        path: '/error',
        element: <Layout {<Error/>}/>,
        errorElement: <Layout {<Error/>}/>,
    },

    ]
);
const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
    <React.StrictMode>
        <RouterProvider router={router}></RouterProvider>
    </React.StrictMode>
);


