import {Link, useNavigate, useParams} from "react-router-dom";
import {useEffect, useState} from "react";
import getData from "../requests/getData";
import Loading from "../components/Loading";
import {isRole} from "../hooks/user.actions";
import Main from "../main/Main";
const img_edit = process.env.PUBLIC_URL + '/edit.svg';
function AnalysisPage() {
    const {id_analysis} = useParams();
    const navigate = useNavigate();
    const [analysis, setAnalysis] = useState(undefined);
    useEffect(() => {
        const fetchAnalysis = async () => {
            const response = await getData(`/api/service-in-medical-institution/${id_analysis}/`);
            if (response.status !== 200) {
                navigate('/error', {replace: true});
            }
            setAnalysis(response.data);

        };
        fetchAnalysis();
    }, [id_analysis]);
    if (analysis === undefined) {
        return <Loading/>
    }
    document.title = analysis.service?.name;
    return (
        <div className={"container d-flex flex-column"}>
            <div className="d-flex flex-column flex-grow-1">
                <div className="d-flex flex-row justify-content-between align-items-center flex-wrap">

                    <h1>{analysis.service?.name}</h1> <h2>{analysis.price}руб</h2>
                    <a className={"btn btn-primary"} href={analysis.url}
                          target="_blank" rel="noreferrer">Записаться</a>
                    {
                    isRole({role: 'agent', medical_institution: analysis.medical_institution?.id}) &&
                    <Link to={`edit`}>
                        <img src={img_edit} alt="edit" height="20" width="20"/>
                    </Link>
                }
                </div>

                <div>
                    <div className="d-flex flex-row">
                    <h3>Материал исследования:</h3>
                    {analysis.service?.research_material?.map((material, index) => {

                        return (
                            <div key={index}>
                                <h3>{material.name}</h3>
                                <p>{material.description}</p>
                            </div>
                        )
                    }
                    )}
                    </div>

                <p>{analysis.service.main_description}</p>
                <div className="d-flex flex-row">
                    <p>Срок выполнения: {analysis.time_to_complete} дней</p>
                    {analysis?.is_available_fast_result ? <p>Доступен быстрый результат за
                    {analysis?.price_for_fast_result} руб в течение {analysis.time_to_complete_fast_result} часов</p> : null}
                    {analysis?.is_available_oms ? <p>Доступно по ОМС</p> : null}
                    {analysis?.is_available_dms ? <p>Доступно по ДМС</p> : null}
                    {analysis?.is_available_at_home ? <div>
                        <p>Выезд на дом</p>
                        {analysis.price_for_at_home !== null ? <p>
                        {analysis.price_for_at_home} руб. за выезд
                        </p> : null}

                    </div>
                        : null}
                </div>
                </div>
            </div>
            <Main fixedAnalysis={analysis}/>
        </div>

            )
            }

            export default AnalysisPage;