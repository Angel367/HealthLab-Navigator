import FilterForm from "../agregator/FilterForm";
import {useEffect, useState} from "react";
import getData from "../requests/getData";
import CardAnalysis from "../agregator/CardAnalysis";
import CardLaboratory from "../agregator/CardLaboratory";

function Main() {
    const [minMaxPrice, setMinMaxPrice] = useState({min:0, max:100000});

    const [analysisInLaboratories, setAnalysisInLaboratories] = useState([]);
    const [selectedLaboratories, setSelectedLaboratories] = useState([]);
    const [selectedAnalysis, setSelectedAnalysis] = useState([]);
    const [selectedLocation, setSelectedLocation] = useState([]);
    const [selectedPeriod, setSelectedPeriod] = useState([]);
    const [oms, setOms] = useState(false);
    const [dms, setDms] = useState(false);
    const [rating, setRating] = useState(0);
    const [selectedMinMaxPrice, setSelectedMinMaxPrice] = useState(minMaxPrice);



    useEffect(() => {
        const fetchAnalysisInLaboratories = async () => {
            const resp = await getData('/api/laboratory-analysis/',
                {id_laboratories: selectedLaboratories.map(laboratory => laboratory.value)},
                {id_analysis: selectedAnalysis.map(analysis => analysis.value)},
                {price: selectedMinMaxPrice},
                // {id_location: selectedLocation.map(location => location.value)},
                // {period: selectedPeriod.map(period => period.value)},
                {oms: oms},
                {dms: dms},
                {rating: rating}
            )
            setAnalysisInLaboratories(resp.data?.results);
            // setMinMaxPrice(analysisInLaboratories.reduce((acc, analysis) => {
            //     return {min: Math.min(acc.min, analysis.price?.price_value || 0),
            //         max: Math.max(acc.max, analysis.price?.price_value || 100000)}
            // }));
        }
        fetchAnalysisInLaboratories();
    }, [selectedLaboratories, selectedAnalysis, selectedMinMaxPrice,
        selectedLocation, selectedPeriod, oms,
        dms, rating, analysisInLaboratories]);





    return (
        <div>
            <FilterForm
                setSelectedLaboratory={setSelectedLaboratories}
                setSelectedAnalysis={setSelectedAnalysis}
                maxMinPrice={minMaxPrice}
                setSelectedMinMaxPrice={setSelectedMinMaxPrice}
                setSelectedLocation={setSelectedLocation}
                setSelectedPeriod={setSelectedPeriod}
                setOms={setOms}
                setDms={setDms}
                setRating={setRating}

            />
            <div>
                {analysisInLaboratories !== undefined && analysisInLaboratories.map((analysis, index) => {
                    return (
                        <div key={index}></div>
                        // <CardLaboratory key={index}
                        //                 // laboratory={branches.find(branch => branch.id_laboratory === analysis.id_laboratory)}
                        //                 analysis={analysis}
                        // />
                    )
                })}
            </div>
        </div>
    );

}
export default Main;