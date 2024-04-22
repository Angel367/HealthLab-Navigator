import FilterForm from "./FilterForm";
import HolderAdv from "./HolderAdv";
import CardAgregator from "./CardAgregator";
import {Link, Navigate, useParams} from "react-router-dom";
import analysis from "./Analysis";

function AnalysisPage() {
    const {id_analysis, id_laboratory} = useParams();
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
    let analysis;
    if (id_analysis !== undefined && id_laboratory !== undefined)
     analysis = labsList.find(
        lab => lab.id_analysis == id_analysis && lab.id_laboratory == id_laboratory
    )
    else if (id_analysis !== undefined)
     analysis = labsList.find(
        lab => lab.id_analysis == id_analysis
    )
    else
        return (
            <Navigate to={'error'}/>
        )

    return (
        <div>
            <h1>Analysis</h1>
            <div>
                <CardAgregator {...analysis}/>
                <Link to={`/laboratory/${id_laboratory}`} > Перейти к лабе</Link>
            </div>
            <FilterForm/>
            <HolderAdv advList={advList}/>


        </div>
    )
}

export default AnalysisPage;