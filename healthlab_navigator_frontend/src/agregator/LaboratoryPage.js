import {Link, useNavigate, useParams} from "react-router-dom";
import {useEffect, useState} from "react";
import getData from "../requests/getData";
import CardLaboratory from "./CardLaboratory";
import {useGeolocated} from "react-geolocated";
import Loading from "../components/Loading";
import Main from "../main/Main";
import { isRole} from "../hooks/user.actions";
const img_edit = process.env.PUBLIC_URL + '/edit.svg';
function LaboratoryPage() {
    const {id_laboratory} = useParams();
    const navigate = useNavigate();
    const [laboratory, setLaboratory] = useState(undefined);
    const [branches, setBranches] = useState([]);
    const {coords} = useGeolocated();

    useEffect(() => {
        const fetchLaboratory = async () => {
            const response = await getData(`/api/medical-institution/${id_laboratory}/`);
            setLaboratory(response.data);
            if (response.status !== 200) {
                navigate('/error', {replace: true});
            }
        };
        fetchLaboratory();
    }, [id_laboratory]);

    useEffect(() => {
        const fetchBranches = async () => {
            const params = new URLSearchParams();
            if (coords !== undefined) {
                params.append('latitude', coords.latitude);
                params.append('longitude', coords.longitude);
            }
            const response = await getData(`/api/medical-institution-branch/?medical_institution=${id_laboratory}`,
                params);
            setBranches(response.data?.results);
        }
        fetchBranches();
    }, [id_laboratory, coords]);

    if (laboratory === undefined) {
        return <Loading/>
    }

    return (
        <div className={"container d-flex flex-column"}>
            <div className="d-flex flex-column flex-grow-1">
                <div className="d-flex flex-row justify-content-between align-items-center">
                <h1>{laboratory.name}</h1>
                <a href={laboratory.website} target="_blank" rel="noreferrer"
                                          className={"btn btn-primary flex-grow-0"}>
                    Сайт лаборатории</a>
                    {
                    isRole({role: 'agent', medical_institution: laboratory.id}) &&
                    <Link to={`edit`}>
                        <img src={img_edit} alt="edit" height="20" width="20"/>
                    </Link>
                }
                </div>
                <p>{laboratory.description}</p>

                <div className="d-flex flex-row justify-content-center align-items-center">
                    <a href="#laboratory-branches" className={"btn btn-link flex-grow-0"}>Филиалы</a>
                    <a href="#laboratory-analysis" className={"btn btn-link flex-grow-0"}>Анализы</a>
                </div>
            </div>
            {branches !== undefined && branches.length > 0 &&
            <div className="col g-4" id="laboratory-branches">
                <h2>Филиалы</h2>
                <div className="col g-4" style={{width: "100%"}}>
                {branches.map((branch, index) => {
                        return (
                           <CardLaboratory
                                style={{width: "100%"}}
                               id={branch.id}
                               no_img={true} key={index} laboratory={branch} laboratory_name={branch.name}/>
                        )
                    })
                    }
                </div>
            </div>
            }

            <div className="col g-4" id="laboratory-analysis">

                <h2>Анализы</h2>
                <Main fixedLaboratories={laboratory} />
            </div>

        </div>
            );


            }

            export default LaboratoryPage;