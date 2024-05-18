import {Link} from "react-router-dom";

function CardAnalysis({analysis_one}) {


    return (

            <div className="card">
                <h3>{analysis_one.service?.name}</h3>
                <p>Стоимость: {analysis_one.price} руб.</p>
                <p>Срок выполнения: {analysis_one.time_to_complete} дней</p>

                {analysis_one.is_available_fast_result ? <p>Доступен быстрый результат</p> : null}
                {analysis_one.is_available_oms ? <p>Доступно по ОМС</p> : null}
                {analysis_one.is_available_dms ? <p>Доступно по ДМС</p> : null}
                {analysis_one.is_available_at_home ? <p>Выезд на дом</p> : null}

                <Link to={`/laboratory/${analysis_one.medical_institution}/analysis/${analysis_one.id}`}>
                    Подробнее об анализе
                </Link>
            </div>

    );
}
export default CardAnalysis;