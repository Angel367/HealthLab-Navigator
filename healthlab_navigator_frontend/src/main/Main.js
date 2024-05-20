import FilterForm from "../agregator/FilterForm";
import {useEffect, useState} from "react";
import getData from "../requests/getData";
import URLSearchParams from "url-search-params";
import CardLaboratory from "../agregator/CardLaboratory";
import {useGeolocated} from "react-geolocated";

function Main() {
    const [analysisInLaboratories, setAnalysisInLaboratories] = useState([]);
    const [selectedLaboratories, setSelectedLaboratories] = useState([]);
    const [selectedAnalysis, setSelectedAnalysis] = useState([]);

    const [oms, setOms] = useState(false);
    const [dms, setDms] = useState(false);
    const [at_home, setAtHome] = useState(false);
    const [selectedMinMaxPrice, setSelectedMinMaxPrice] = useState(undefined);
    const [fastResult, setFastResult] = useState(false);
    const [selectedMetroStations, setSelectedMetroStations] = useState([]);
    const [branches, setBranches] = useState([]);
    const [page, setPage] = useState(1);
    const [laboratories, setLaboratories] = useState(undefined);
    const { coords, isGeolocationAvailable, isGeolocationEnabled, positionError}=
        useGeolocated({
            positionOptions: {
                enableHighAccuracy: true,
            },
            userDecisionTimeout: 10000,
        });
    // console.log(positionError)

    useEffect(() => {
        const fetchAnalysisInLaboratories = async () => {
            const params = new URLSearchParams();
            if (selectedLaboratories.length > 0) {
                selectedLaboratories.forEach(laboratory => {
                    params.append('medical_institution', laboratory.value);
                });
            }
            if (selectedAnalysis.length > 0) {
                selectedAnalysis.forEach(analysis => {
                    params.append('service', analysis.value);
                });
            }
            else {
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
            if (selectedMinMaxPrice !== undefined
                && selectedMinMaxPrice.min !== undefined
                && selectedMinMaxPrice.max !== undefined) {
                params.append('price_min', selectedMinMaxPrice.min);
                params.append('price_max', selectedMinMaxPrice.max);
            }
            const resp = await getData('/api/service-in-medical-institution/',
                params
            )
            setAnalysisInLaboratories(resp.data?.results);

        }
        fetchAnalysisInLaboratories();
    }, [selectedLaboratories, selectedAnalysis, selectedMinMaxPrice, oms, dms, at_home, fastResult]);
    const calcMinMaxPrice = (analysisInLaboratories) => {
        if (analysisInLaboratories?.length === 0 || true) {
            return {min: 0, max: 100000};
        }
        let min = analysisInLaboratories[0].price;
        let max = analysisInLaboratories[0].price;
        analysisInLaboratories.forEach(analysis => {
            if (analysis.price < min) {
                min = analysis.price || 0;
            }
            if (analysis.price > max) {
                max = analysis.price || 100000;
            }
        });
        return {min: min, max: max};
    }
    useEffect(() => {
        const fetchBranches = async () => {
            const params = new URLSearchParams();
            if (selectedLaboratories.length > 0) {
                selectedLaboratories.forEach(laboratory => {
                    params.append('medical_institution', laboratory.value);
                });

            }
            if (selectedMetroStations.length > 0) {
                selectedMetroStations.forEach(station => {
                    params.append('metro_stations', station.value);
                });
            }
            if (isGeolocationAvailable && isGeolocationEnabled && coords !== undefined) {
                params.append('longitude', coords?.longitude)
                params.append('latitude', coords?.latitude)

            }
            params.append('page', page);
            const resp = await getData('/api/medical-institution-branch/',
            params);
            setBranches(resp.data || []);
        }
        fetchBranches();
    }, [selectedMetroStations, coords, selectedLaboratories, page, isGeolocationAvailable, isGeolocationEnabled]);
    const nextPage = () => {
        setPage(page + 1);
    }
    const prevPage = () => {
        setPage(page - 1);
    }
    const firstPage = () => {
        setPage(1);
    }
    const lastPage = () => {
        setPage(Math.ceil(branches.count / 10));
    }
    return (
        <div>
            <FilterForm
                setSelectedLaboratory={setSelectedLaboratories}
                setSelectedAnalysis={setSelectedAnalysis}
                setSelectedMetroStations={setSelectedMetroStations}
                maxMinPrice={calcMinMaxPrice(analysisInLaboratories)}
                setSelectedMinMaxPrice={setSelectedMinMaxPrice}
                setAtHome={setAtHome}
                setFastResult={setFastResult}
                setOms={setOms}
                setDms={setDms}
                selectedMinMaxPrice={selectedMinMaxPrice}
                laboratories={laboratories}
                setLaboratories={setLaboratories}
                setPage={setPage}
            />
            <div>
                <div>

                    {branches.results !== undefined && branches.results.length > 0 &&
                        selectedAnalysis?.length >= 0 &&
                        branches.results.map((branch, index) => {
                            if (selectedAnalysis.length > 0 && analysisInLaboratories?.length>0 &&
                                analysisInLaboratories.find(analysis => analysis.medical_institution === branch.medical_institution)) {
                                // console.log(analysisInLaboratories.find(analysis => analysis.medical_institution === branch.medical_institution));
                                return null;
                            }

                            const lab_name = laboratories.find(laboratory => laboratory.id === branch.medical_institution).name || '';
                            return (
                                <CardLaboratory key={index}
                                                laboratory={branch}
                                                laboratory_name={lab_name}
                                                analysis={analysisInLaboratories.filter(analysis => analysis.medical_institution === branch.medical_institution)}
                                />
                            )
                        }
                        )}

                    {branches.results?.length === 0 &&
                        <p>Ничего не найдено</p>
                        }
                     </div>
                         <div>
                             {page > 1 &&
                                 <>
                                    <button onClick={firstPage}>Первая</button>
                                     <button onClick={prevPage}>Назад</button>
                                 </>
                             }
                             {page}
                                {page < Math.ceil(branches.count / 10) &&
                                    <>
                                        <button onClick={nextPage}>Вперед</button>
                                        <button onClick={lastPage}>Последняя</button>
                                    </>
                                }
                         </div>

                </div>

            </div>

    );

}
export default Main;