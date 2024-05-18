import {Link} from "react-router-dom";
import CardAnalysis from "./CardAnalysis";

function CardLaboratory({ laboratory, analysis, laboratory_name}) {
    console.log(analysis, laboratory_name)
    return (
            <div className="card">
                <h2>{laboratory_name}</h2>
                <p>Адрес: {laboratory.address}</p>
                {laboratory.metro_stations !== undefined &&
                    <div>
                    <p>Метро:</p>
                    <p> {laboratory.metro_stations.map((station, index) => {
                        return <span key={index}>{station.name} </span>
                    })
                    }</p>
                    </div>
                }
                {laboratory.distance_to_user !== null &&
                    <p>Расстояние: {laboratory.distance_to_user} км</p>
                }


                {analysis && analysis.map((analysis_one, index) => {
                    return <CardAnalysis key={index} analysis_one={analysis}/>;
                })}
                <Link to={`/laboratory/${laboratory.medical_institution}#${laboratory.id}`}>
                    Подробнее об лаборатории
                </Link>
            </div>
    );
}
export default CardLaboratory;