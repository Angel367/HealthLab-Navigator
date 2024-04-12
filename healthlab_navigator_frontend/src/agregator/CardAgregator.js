import {Link} from "react-router-dom";

function CardAgregator({name, price, id_analysis, duration, id_laboratory}) {
    let link = "";
    if (id_laboratory !== undefined && id_analysis !== undefined)
        link = `/laboratory/${id_laboratory}/analysis/${id_analysis}`;
    else if (id_laboratory !== undefined)
        link = `/laboratory/${id_laboratory}`;
    else if (id_analysis !== undefined)
        link = `/analysis/${id_analysis}`;
    else
        return null;

    return (
        <Link to={link} className="card">
            <div className="card__name">{name}</div>
            <div className="card__duration">{duration}</div>
            <div className="card__price">{price}</div>
        </Link>
    );
}
export default CardAgregator;