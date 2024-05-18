import {Link} from "react-router-dom";
import CardAnalysis from "./CardAnalysis";

function CardLaboratory({ id_laboratory, laboratory_name,
    address, analysis=[], rating=null, id_branch}) {
    return (
            <div className="card">
                <h2>{laboratory_name}</h2>
                <p>Адрес: {address}</p>
                {rating ? <p>Рейтинг: {rating}</p> : null}
                {analysis.map((analysis, index) => {
                    return <CardAnalysis key={index} {...analysis}/>;
                })}
                <Link to={`/laboratory/${id_laboratory}/#${id_branch}`}>
                    Подробнее об лаборатории
                </Link>
            </div>
    );
}
export default CardLaboratory;