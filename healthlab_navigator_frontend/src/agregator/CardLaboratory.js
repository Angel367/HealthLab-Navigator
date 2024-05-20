import {Link} from "react-router-dom";
import CardAnalysis from "./CardAnalysis";

function CardLaboratory({ laboratory, analysis, laboratory_name, no_img}) {
    if (laboratory.medical_institution === 1){
        laboratory.img = "https://cdn1.flamp.ru/cd1d154836c8e7d59a0da017d8e1d380.png"
    } else if (laboratory.medical_institution === 2){
        laboratory.img = "https://p2.zoon.ru/1/e/5a6489a5a24fd9100f094bbf_628b05e7b38a94.19357826.jpg"
    } else{
        laboratory.img = "https://msal.ru/upload/medialibrary/0eb/s27i55i3b0s55ffuicuxaaxxfgdnurst.png";
    }
    // console.log(analysis)
    return (
        <div className="card" style={{width: "100%"}} id={"laboratory-"+laboratory.id}>
            {no_img !== true &&
            <img src={laboratory.img} className="card-img-top" alt="..." style={{height: "100px", width:"100px", objectFit: "cover"}}/>}
            <div className="card-body">
                <h5 className="card-title">{laboratory_name}</h5>
                <h6 className="card-subtitle mb-2 text-muted">{laboratory.address}</h6>

            {laboratory.metro_stations !== undefined && laboratory.metro_stations.length > 0 &&
                    <div className={"d-flex flex-row flex-wrap gap-4"}>
                       {laboratory.metro_stations.map((station) => {
                        return (<div key={station.id} className={"d-flex flex-row justify-content-between align-items-center"}>
                            <span style={{background: "#"+station?.line?.color, width:
                                    "10px", height: "10px", borderRadius: "50%",
                                    display: "inline-block", marginRight: "5px"
                            }}></span><span>{station.name}</span>
                        </div>)
                    })}</div>


            }
            {laboratory.distance_to_user !== null &&
                <p className={"card-text"}
                >Расстояние: {Math.ceil(laboratory.distance_to_user / 1000) } км</p>
            }


            {analysis && analysis.map((analysis_one, index) => {

                return <CardAnalysis key={index} analysis_one={analysis_one}/>;
            })}
                {no_img !== true ?
            <Link to={`/laboratory/${laboratory?.medical_institution}#laboratory-${laboratory.id}`}
            className="card-link">
                Подробнее об лаборатории
            </Link> :
                    <div className={"d-flex flex-col justify-content-between"}>
                        {laboratory.working_hours !== null && laboratory.working_hours.length > 0 &&
                            laboratory.working_hours.map((working_hour, index) => {
                                return (
                                    <div key={index} className={"d-flex flex-col justify-content-between align-items-center"}>
                                        <p>{working_hour.day} {working_hour.open_time} - {working_hour.close_time}</p>
                                    </div>
                                )
                            }
                            )
                        }
                    </div>
                }
            </div>
        </div>
    );
}

export default CardLaboratory;