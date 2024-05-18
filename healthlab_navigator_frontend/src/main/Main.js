import FilterForm from "../agregator/FilterForm";
import {useEffect, useState} from "react";
import getData from "../requests/getData";
import URLSearchParams from "url-search-params";
import CardLaboratory from "../agregator/CardLaboratory";

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
    const [laboratories, setLaboratories] = useState(undefined);
    const [userLocation, setUserLocation] = useState({
        'longitude': 37.617635,
        'latitude': 55.755814
    });
    useEffect(() => {
        const fetchLaboratories = async () => {
            const resp = await getData('/api/medical-institution/')
            setLaboratories(resp.data?.results);
        }
        fetchLaboratories();
    }, []);
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
            if (oms === true) {
                params['is_available_oms'] = oms;
            }
            if (dms === true) {
                params['is_available_dms'] = dms;
            }
            if (at_home === true) {
                params['is_available_at_home'] = at_home;
            }
            if (fastResult === true) {
                params['is_available_fast_result'] = fastResult;
            }
            if (selectedMinMaxPrice !== undefined
                && selectedMinMaxPrice.min !== undefined
                && selectedMinMaxPrice.max !== undefined) {
                params['price_min'] = selectedMinMaxPrice.min;
                params['price_max'] = selectedMinMaxPrice.max;
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
                min = analysis.price;
            }
            if (analysis.price > max) {
                max = analysis.price;
            }
        });
        return {min: min, max: max};
    }
    useEffect(() => {
        const fetchBranches = async () => {
            const params = new URLSearchParams();
            if (selectedMetroStations.length > 0) {
                selectedMetroStations.forEach(station => {
                    params.append('metro_station', station.value);
                });
            }
            if (userLocation !== undefined) {
                params['latitude'] = userLocation.latitude;
                params['longitude'] = userLocation.longitude;
            }
            const resp = await getData('/api/medical-institution-branch/')
            setBranches(resp.data?.results);
        }
        fetchBranches();
    }, [selectedMetroStations, userLocation]);

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
            />
            <div>
                {/*todo вызов разных карточек в зависимости от контекста*/}
                {analysisInLaboratories !== undefined
                    &&
                    branches !== undefined
                    &&
                    branches.map((branch, index) => {
                    return (

                        <CardLaboratory key={index}
                                        laboratory={branch}
                                        laboratory_name={laboratories.find(laboratory => laboratory.id === branch.medical_institution)?.name}

                                        analysis={analysisInLaboratories.filter(
                                            analysis => analysis.medical_institution?.id === branch.medical_institution
                                        && selectedAnalysis.map(analysis => analysis.value).includes(analysis.service?.id)
                                        )}
                        />
                    )
                })}
            </div>
        </div>
    );

}
export default Main;