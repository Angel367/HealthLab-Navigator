import {Link} from "react-router-dom";
import {isRole} from "../hooks/user.actions";
const img_edit = process.env.PUBLIC_URL + '/edit.svg';
function CardAnalysis({analysis_one}) {
    if (analysis_one === undefined) {
        return null;
    }
    // console.log(analysis_one, 'one')
    return (

        <div className="card">
            <div className={"card-header d-flex justify-content-between align-items-center"}>
            <h5 className="card-title">{analysis_one.service?.name}</h5>
                {
                    isRole({role: 'agent', medical_institution: analysis_one.medical_institution?.id}) &&
                    <Link to={`/laboratory/${analysis_one.medical_institution?.id}/analysis/${analysis_one.id}/edit`}>
                        <img src={img_edit} alt="edit" height="20" width="20"/>
                    </Link>
                }
                    </div>
                    <div className="card-body">
                    <p className="card-text">Стоимость: {analysis_one.price} руб.</p>
            <p className="card-text">Срок выполнения: {analysis_one.time_to_complete} дней</p>

            {analysis_one?.service?.is_available_fast_result ? <p>Доступен быстрый результат</p> : null}
            {analysis_one?.service?.is_available_oms ? <p>Доступно по ОМС</p> : null}
            {analysis_one?.service?.is_available_dms ? <p>Доступно по ДМС</p> : null}
            {analysis_one?.service?.is_available_at_home ? <p>Выезд на дом</p> : null}

            <Link  className={"card-link"}
                to={`/laboratory/${analysis_one.medical_institution?.id}/analysis/${analysis_one.id}`}>
                Подробнее об анализе
            </Link>
            </div>
        </div>

    );
}

export default CardAnalysis;