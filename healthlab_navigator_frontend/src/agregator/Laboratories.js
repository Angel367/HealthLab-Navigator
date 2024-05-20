import {useEffect, useState} from "react";
import getData from "../requests/getData";
import Loading from "../components/Loading";
import {Link} from "react-router-dom";


function Laboratories() {
    const [laboratories, setLaboratories] = useState([]);
    useEffect(() => {
        const fetchLaboratories = async () => {
            const resp = await getData('/api/medical-institution/');
            setLaboratories(resp.data?.results);
        }
        fetchLaboratories();
    }, []);
    if (laboratories === undefined || laboratories?.length === 0) {
        return <Loading/>
    } else {
    return (
        <main>
            <div className="container mt-5 mb-5 g-4">
                <h1>Лаборатории</h1>
                <div className="row row-cols-1 row-cols-md-3 g-4">
                    {laboratories.map((laboratory, index) => {
                            let laboratory_img = "https://msal.ru/upload/medialibrary/0eb/s27i55i3b0s55ffuicuxaaxxfgdnurst.png";
                            if (laboratory.id === 1){
                                laboratory_img = "https://cdn1.flamp.ru/cd1d154836c8e7d59a0da017d8e1d380.png"
                            } else if (laboratory.id === 2){
                                laboratory_img = "https://p2.zoon.ru/1/e/5a6489a5a24fd9100f094bbf_628b05e7b38a94.19357826.jpg"
                            }
                            return (
                                <div className="col-md-3 d-flex align-items-stretch">
                                    <div className="card">
                                        <img src={laboratory_img} className="card-img-top" alt="..."
                                             style={{height: '150px', objectFit: 'cover'}}/>
                                        <div
                                            className="card-body d-flex flex-column justify-content-between
                                             text-justify">
                                            <h5 className="card-title">{laboratory.name}</h5>
                                            <p className="card-text">{laboratory.description.slice(0, 200)}...</p>
                                            <Link className="btn btn-primary align-self-center"
                                                  to={`/laboratory/${laboratory.id}`}>
                                                Подробнее
                                            </Link>
                                        </div>
                                    </div>
                                </div>

                            )
                    })
                    }
                </div>
            </div>
        </main>
    )
    }
}

export default Laboratories;