import FilterForm from "./FilterForm";
import HolderAdv from "./HolderAdv";
import CardAgregator from "./CardAgregator";
import {Link, Navigate, useParams} from "react-router-dom";
import {isAuth, isRole} from "../hooks/user.actions";
import RoleMedInstLayout from "../router/RoleMedInstLayout";

function LaboratoryPage() {
    const {id_laboratory} = useParams();
    const advList = [
        {
            img: "https://via.placeholder.com/150",
            title: "Adv 1"
        },
        {
            img: "https://via.placeholder.com/150",
            title: "Adv 2"
        },
        {
            img: "https://via.placeholder.com/150",
            title: "Adv 3"
        }
    ];
    const labsList = [
        {
            id_analysis: 1,
            name: 'Analysis 1',
            price: 100,
            duration: 1,
            id_laboratory: 1
        },
        {
            id_analysis: 2,
            name: 'Analysis 2',
            price: 200,
            duration: 2,
            id_laboratory: 2
        },
        {
            id_analysis: 3,
            name: 'Analysis 3',
            price: 300,
            duration: 3,
            id_laboratory: 3
        }];
    let laboratory;
    if (id_laboratory !== undefined)
        laboratory = labsList.find(
            lab => lab.id_laboratory == id_laboratory
        )
    else
        return (
            <Navigate to={'error'}/>
        )

    return (
        <div>

            <h1>{laboratory.name}</h1>

            {isRole("medical_institution_agent") ?
                <Link to={`/laboratory/${id_laboratory}/edit`} > Редактировать </Link> :
                <div>
                    ПОТОМ ДОБАВЛЮ КОММЕТАРИИ
                </div>
            }
            <div>
                <CardAgregator {...laboratory}/>
            </div>
            <FilterForm/>
            <HolderAdv advList={advList}/>
        </div>
    )


}

export default LaboratoryPage;