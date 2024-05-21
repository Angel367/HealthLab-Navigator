import React, { useEffect, useState } from "react";

import getData from "../requests/getData";

import 'react-input-range/lib/css/index.css';
import FilterForm from "../agregator/FilterForm";
import CardLaboratory from "../agregator/CardLaboratory";
import { useGeolocated } from "react-geolocated";
import Loading from "../components/Loading";

function Main({fixedAnalysis = undefined, fixedLaboratories = undefined}) {

    const [analysisInLaboratories, setAnalysisInLaboratories] = useState([]);
    const [selectedLaboratories, setSelectedLaboratories] = useState([]);
    const [selectedAnalysis, setSelectedAnalysis] = useState([]);
    const [oms, setOms] = useState(false);
    const [dms, setDms] = useState(false);
    const [at_home, setAtHome] = useState(false);
    const [selectedMinMaxPrice, setSelectedMinMaxPrice] = useState({min:0, max:50000});
    const [fastResult, setFastResult] = useState(false);
    const [selectedMetroStations, setSelectedMetroStations] = useState([]);
    const [branches, setBranches] = useState([]);
    const [page, setPage] = useState(1);
    const [count, setCount] = useState(0);
    const [laboratories, setLaboratories] = useState(undefined);
    const [ordering, setOrdering] = useState(undefined);
    const { coords, isGeolocationAvailable, isGeolocationEnabled, positionError } = useGeolocated({
        positionOptions: {
            enableHighAccuracy: true,
        },
        userDecisionTimeout: 10000,
    });

    useEffect(() => {
        const fetchAnalysisInLaboratories = async () => {

            const params = new URLSearchParams();
            if (fixedLaboratories !== undefined) {

                params.append('medical_institution', fixedLaboratories.id);
            } else
            if (selectedLaboratories.length > 0) {
                selectedLaboratories.forEach(laboratory => {
                    params.append('medical_institution', laboratory.value);
                });
            }
            if (ordering !== undefined) {
                params.append('ordering', ordering.value);
            }
            if (fixedAnalysis !== undefined) {
                params.append('service', fixedAnalysis.id);
            } else
            if (selectedAnalysis.length > 0) {
                selectedAnalysis.forEach(analysis => {
                    params.append('service', analysis.value);
                });
            } else {
                setAnalysisInLaboratories([])
                return;
            }
            if (oms === true) {
                params.append('is_available_oms', oms);
            }
            if (dms === true) {
                params.append('is_available_dms', dms);
            }
            if (at_home === true) {
                params.append('is_available_at_home', at_home);
            }
            if (fastResult === true) {
                params.append('is_available_fast_result', fastResult);
            }
            if (selectedMinMaxPrice !== undefined) {
                params.append('price_min', selectedMinMaxPrice.min);
                params.append('price_max', selectedMinMaxPrice.max);
            }

                const resp = await getData('/api/service-in-medical-institution/', params);
                setAnalysisInLaboratories(resp.data?.results);

        };
        fetchAnalysisInLaboratories();
    }, [selectedLaboratories, selectedAnalysis, selectedMinMaxPrice, oms, dms, at_home, fastResult, ordering, fixedLaboratories, fixedAnalysis]);

    useEffect(() => {
        const fetchBranches = async () => {
            const params = new URLSearchParams();
            if (fixedLaboratories !== undefined) {
                params.append('medical_institution', fixedLaboratories.id);
            } else
            if (selectedLaboratories.length > 0) {
                selectedLaboratories.forEach(laboratory => {
                    params.append('medical_institution', laboratory.value);
                });
                setPage(1);

            }
            if (fixedAnalysis !== undefined) {
                params.append('service', fixedAnalysis.id);
            } else
            if (selectedAnalysis.length > 0) {
                selectedAnalysis.forEach(analysis => {
                    params.append('service', analysis.value);
                });
                setPage(1);
            }
            if (selectedMetroStations.length > 0) {
                selectedMetroStations.forEach(station => {
                    params.append('metro_stations', station.value);
                });
                setPage(1);
            }
            if (isGeolocationAvailable && isGeolocationEnabled && coords !== undefined) {
                params.append('longitude', coords?.longitude);
                params.append('latitude', coords?.latitude);

            }
            params.append('page', page);
            const resp = await getData('/api/medical-institution-branch/', params);
            setBranches(resp.data?.results);
            setCount(resp.data?.count);
        };
        fetchBranches();
    }, [selectedMetroStations, coords, selectedLaboratories, page, isGeolocationAvailable, isGeolocationEnabled, fixedLaboratories, fixedAnalysis, selectedAnalysis]);

    const nextPage = () => {
        setPage(page + 1);
    };

    const prevPage = () => {
        setPage(page - 1);
    };

    const firstPage = () => {
        setPage(1);
    };

    const lastPage = () => {
        setPage(Math.ceil(count / 10));
    };

    return (
        <div className={"container"}>
            <FilterForm
                setSelectedLaboratory={setSelectedLaboratories}
                setSelectedAnalysis={setSelectedAnalysis}
                setSelectedMetroStations={setSelectedMetroStations}
                maxMinPrice={{min:0, max:50000}}
                setSelectedMinMaxPrice={setSelectedMinMaxPrice}

                setAtHome={setAtHome}
                setFastResult={setFastResult}
                setOms={setOms}
                setDms={setDms}
                selectedMinMaxPrice={selectedMinMaxPrice}
                laboratories={laboratories}
                setLaboratories={setLaboratories}
                setPage={setPage}
                setOrdering={setOrdering}
                fixedAnalysis={fixedAnalysis}
                fixedLaboratories={fixedLaboratories}
            />
           <div className="container">
               <div>
                   {branches?.length > 0 ?
                       <>
                       <div className=" d-flex flex-row flex-wrap gap-4">
                           {analysisInLaboratories.length > 0 ?
                               branches.map((branch, index) => {
                                      return <CardLaboratory key={index} laboratory={branch}
                                                             analysis={analysisInLaboratories.filter(analysis => analysis.medical_institution.id === branch.medical_institution)}
                                                             laboratory_name={branch.name} />
                                 })


                               :
                               branches.map((branch, index) => {
                                   return <CardLaboratory key={index} laboratory={branch} analysis={[]}
                                                          laboratory_name={branch.name} />})


                           }
                           </div>
                           <div className="mt-3">
                                {page > 1 && (
                                  <>
                                    <button className="btn btn-link mr-2" onClick={firstPage}>Первая</button>
                                    <button className="btn btn-link mr-2" onClick={prevPage}>Назад</button>
                                  </>
                                )}
                                {page}
                                {page < Math.ceil(count / 10) ? (
                                  <>
                                    <button className="btn btn-link mr-2" onClick={nextPage}>Вперед</button>
                                    <button className="btn btn-link" onClick={lastPage}>Последняя</button>
                                  </>
                                ) : null}

                            </div>
                          </>

                       :
                       <>{branches === undefined ? <Loading/> : <h1>Ничего не найдено</h1>}</>
                   }


               </div>
           </div>
        </div>
    );
}

export default Main;
