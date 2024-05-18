import {Link} from "react-router-dom";

function CardAnalysis({id_analysis_in_laboratory, name_analysis, id_laboratory,
    duration_analysis, price_analysis, fast_duration_analysis, fast_price_analysis,
    is_available_oms, is_available_dms, is_available_fast, is_available_at_home,
    price_at_home
}) {


    return (

            <div className="card">
                <h3>{name_analysis}</h3>
                <p>Стоимость: {price_analysis} руб.</p>
                <p>Срок выполнения: {duration_analysis} дней</p>
                {fast_duration_analysis && fast_price_analysis && is_available_fast ?
                    <p>Срочно: {fast_price_analysis} руб. / {fast_duration_analysis} дней</p> :
                    null
                }
                {is_available_oms ? <p>Доступен по ОМС</p> : null}
                {is_available_dms ? <p>Доступен по ДМС</p> : null}
                {is_available_at_home ? <p>Доступна сдача на дому
                    {price_at_home ? `: за ${price_at_home} руб.` : null}</p> : null}
                <Link to={`/laboratory/${id_laboratory}/analysis/${id_analysis_in_laboratory}`}>
                    Подробнее об анализе
                </Link>
            </div>

    );
}
export default CardAnalysis;