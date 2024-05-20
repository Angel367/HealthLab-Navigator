import {Link} from "react-router-dom";
import CardAnalysis from "./CardAnalysis";

function CardLaboratory({ laboratory, analysis, laboratory_name}) {
    if (laboratory.medical_institution === 1){
        laboratory.img = "https://cdn1.flamp.ru/cd1d154836c8e7d59a0da017d8e1d380.png"
    } else if (laboratory.medical_institution === 2){
        laboratory.img = "https://p2.zoon.ru/1/e/5a6489a5a24fd9100f094bbf_628b05e7b38a94.19357826.jpg"
    } else{
        laboratory.img = "https://msal.ru/upload/medialibrary/0eb/s27i55i3b0s55ffuicuxaaxxfgdnurst.png";
    }
    console.log(analysis)
    return (
        <div className="card" style={{width: "18rem"}}>
            <img src={laboratory.img} className="card-img-top" alt="..."/>
            <div className="card-body">
                <h5 className="card-title">{laboratory_name}</h5>
                <h6 className="card-subtitle mb-2 text-muted">{laboratory.address}</h6>

            {laboratory.metro_stations !== undefined && laboratory.metro_stations.length > 0 &&
                <div>
                    <p className={"card-text"}>Метро: {laboratory.metro_stations.map((station) => {
                        return station.name
                    })
                    }</p>
                </div>
            }
            {laboratory.distance_to_user !== null &&
                <p className={"card-text"}
                >Расстояние: {Math.ceil(laboratory.distance_to_user / 1000) } км</p>
            }


            {analysis && analysis.map((analysis_one, index) => {

                return <CardAnalysis key={index} analysis_one={analysis_one}/>;
            })}
            <Link to={`/laboratory/${laboratory.medical_institution}#${laboratory.id}`}
            className="card-link">
                Подробнее об лаборатории
            </Link>
            </div>
        </div>
    );
}

export default CardLaboratory;