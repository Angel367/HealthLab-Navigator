import {useNavigate, useParams} from "react-router-dom";
import {useEffect, useState} from "react";
import axiosService from "../../requests/axiosService";
import getData from "../../requests/getData";
import Loading from "../../components/Loading";
import {NotificationManager} from "react-notifications";

function AnalysisEdit() {
    const { id_analysis } = useParams();
    const navigate  = useNavigate();
    const [analysis, setAnalysis] = useState({
        price: '',
        time_to_complete: '',
        is_available_fast_result: false,
        price_for_fast_result: '',
        time_to_complete_fast_result: '',
        is_available_oms: false,
        is_available_dms: false,
        is_available_at_home: false,
        price_for_at_home: ''
    });

    useEffect(() => {
        // Fetch analysis details
        const fetchAnalysis = async () => {
            if (!id_analysis) navigate('/error', { replace: true });
            const response = await getData(`/api/service-in-medical-institution/${id_analysis}/`)
            if (response.status !== 200) {
                console.log(response.status, response.data)
                // navigate('/error', { replace: true });
            }
            setAnalysis(response.data);
        }
        fetchAnalysis();

    }, [id_analysis]);

    const handleChange = (e) => {
        const { name, value, type, checked } = e.target;
        const val = type === 'checkbox' ? checked : value;
        setAnalysis({ ...analysis, [name]: val });
    };

    if (analysis === undefined) return <Loading />;

    const handleSubmit = (e) => {
        e.preventDefault();
        try {
            axiosService.put(`/api/service-in-medical-institution/${id_analysis}/`,
                analysis).then(navigate(`/laboratory/${analysis.medical_institution.id}/analysis/${id_analysis}`))
                .then((response) => {
                    if (response.status === 200) {
                        NotificationManager.success('Данные успешно сохранены');
                    }
                })
                .catch(error => {
                    NotificationManager.error('Ошибка при сохранении данных');
                });
        }
        catch (error) {
            console.error("Error updating analysis:", error);
        }

    };

    return (
        <div className="container">

            <form onSubmit={handleSubmit}>
                <div className="form-group">
                    <label htmlFor="serviceName">Наименование</label>
                    <input
                        type="text"
                        className="form-control"
                        id="serviceName"
                        name="service.name"
                        value={analysis.service?.name}
                        disabled={true}
                    />
                </div>
                <div className="form-group">
                    <label htmlFor="price">Цена</label>
                    <input
                        type="number"
                        className="form-control"
                        id="price"
                        name="price"
                        value={analysis.price}
                        onChange={handleChange}
                    />
                </div>
                <div className="form-group">
                    <label htmlFor="mainDescription">Описание</label>
                    <textarea
                        className="form-control"
                        id="mainDescription"
                        name="service.main_description"
                        value={analysis.service?.main_description}
                        disabled={true}

                    />
                </div>
                <div className="form-group">
                    <label htmlFor="timeToComplete">Срок выполнения (дней)</label>
                    <input
                        type="number"
                        className="form-control"
                        id="timeToComplete"
                        name="time_to_complete"
                        value={analysis.time_to_complete}
                        onChange={handleChange}
                    />
                </div>
                <div className="form-check">
                    <input
                        type="checkbox"
                        className="form-check-input"
                        id="isAvailableFastResult"
                        name="is_available_fast_result"
                        checked={analysis.is_available_fast_result}
                        onChange={handleChange}
                    />
                    <label className="form-check-label" htmlFor="isAvailableFastResult">
                        Доступен быстрый результат
                    </label>
                </div>
                {analysis.is_available_fast_result && (
                    <div className="form-group">
                        <label htmlFor="priceForFastResult">Цена за быстрый результат</label>
                        <input
                            type="number"
                            className="form-control"
                            id="priceForFastResult"
                            name="price_for_fast_result"
                            value={analysis.price_for_fast_result}
                            onChange={handleChange}
                        />
                        <label htmlFor="timeToCompleteFastResult">Время выполнения быстрого результата (часы)</label>
                        <input
                            type="number"
                            className="form-control"
                            id="timeToCompleteFastResult"
                            name="time_to_complete_fast_result"
                            value={analysis.time_to_complete_fast_result}
                            onChange={handleChange}
                        />
                    </div>
                )}
                <div className="form-check">
                    <input
                        type="checkbox"
                        className="form-check-input"
                        id="isAvailableOms"
                        name="is_available_oms"
                        checked={analysis.is_available_oms}
                        onChange={handleChange}
                    />
                    <label className="form-check-label" htmlFor="isAvailableOms">
                        Доступно по ОМС
                    </label>
                </div>
                <div className="form-check">
                    <input
                        type="checkbox"
                        className="form-check-input"
                        id="isAvailableDms"
                        name="is_available_dms"
                        checked={analysis.is_available_dms}
                        onChange={handleChange}
                    />
                    <label className="form-check-label" htmlFor="isAvailableDms">
                        Доступно по ДМС
                    </label>
                </div>
                <div className="form-check">
                    <input
                        type="checkbox"
                        className="form-check-input"
                        id="isAvailableAtHome"
                        name="is_available_at_home"
                        checked={analysis.is_available_at_home}
                        onChange={handleChange}
                    />
                    <label className="form-check-label" htmlFor="isAvailableAtHome">
                        Выезд на дом
                    </label>
                </div>
                {analysis.is_available_at_home && (
                    <div className="form-group">
                        <label htmlFor="priceForAtHome">Цена за выезд на дом</label>
                        <input
                            type="number"
                            className="form-control"
                            id="priceForAtHome"
                            name="price_for_at_home"
                            value={analysis.price_for_at_home}
                            onChange={handleChange}
                        />
                    </div>
                )}
                <button type="submit" className="btn btn-primary">Сохранить</button>
            </form>
        </div>
    );
};



export default AnalysisEdit;