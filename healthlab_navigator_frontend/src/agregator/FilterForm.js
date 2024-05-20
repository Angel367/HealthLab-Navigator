import React, {useEffect, useState} from "react";
import makeAnimated from "react-select/animated";
import Select from 'react-select';
import getData from "../requests/getData";
import InputRange from 'react-input-range';
import 'react-input-range/lib/css/index.css';

function FilterForm({setSelectedLaboratory,
                        maxMinPrice,
                        setSelectedMinMaxPrice,
                        selectedMinMaxPrice,
                        setPage,
                        setAtHome,
                        setFastResult,
                        setSelectedAnalysis,
                        laboratories,
                        setLaboratories,
                        setSelectedMetroStations,
                       setOms,
                        setDms}) {

    const [analysis, setAnalysis] = useState([]);
    const [laboratoriesOptions, setLaboratoriesOptions] = useState([]);
    const [analysisOptions, setAnalysisOptions] = useState([]);
    const [metroStations, setMetroStations] = useState([]);
    const [metroLines, setMetroLines] = useState([]);
    const [metroLinesOptions, setMetroLinesOptions] = useState([]);
    const [selectedInputAnalysis, setSelectedInputAnalysis] = useState('');
    useEffect(() => {
        const fetchAnalysis = async () => {
                const resp = await getData('/api/medical-service/',
                    {name__icontains: selectedInputAnalysis})
                setAnalysis(resp.data?.results);
                setPage(1)
        }
        fetchAnalysis();
    }, [selectedInputAnalysis]);
    useEffect(() => {
        const fetchLaboratories = async () => {

                const resp = await getData('/api/medical-institution/')
                setLaboratories(resp.data?.results);


        }
        fetchLaboratories();
    }, []);
    useEffect(() => {
        analysis !== undefined
            ? setAnalysisOptions(analysis.map(analysis => {
                return {value: analysis.id, label: analysis.name}
            })) : setAnalysisOptions([]);
    }, [analysis]);
    useEffect(() => {
        const fetchMetroLines = async () => {
            let page_l = 1;
            let metro_lines=[];
            while (true){
                const resp = await getData('/api/metro-line/?page='+page_l)
                metro_lines.push(resp.data?.results);
                if (resp.data?.next === null){
                    break;
                }
                page_l++;
                setMetroLines(metro_lines.flat());
            }


        }
        fetchMetroLines();
    }, []);

    useEffect(() => {
        const fetchMetroStations = async () => {
            let page = 1;
            let metro_stations=[];
            while (true){
                const resp = await getData('/api/metro-station/?page='+page);
                metro_stations.push(resp.data?.results);
                if (resp.data?.next === null){
                    break;
                }
                page++;

            }

            setMetroStations(metro_stations.flat());
        }
        fetchMetroStations();
    }, []);
     useEffect(() => {
        metroLines !== undefined
            ? setMetroLinesOptions(metroLines.map(metroLine => {

                return { label: metroLine?.name || '',
                    options: metroStations.filter(station => station.line?.id === metroLine.id).map(station => {

                        return {value: station?.id, label: station?.name || ''}
                    })}
            })) : setMetroLinesOptions([]);
    }, [metroLines, metroStations]);



    useEffect(() => {
        laboratories !== undefined
            ? setLaboratoriesOptions(laboratories.map(laboratory => {
                return {value: laboratory.id, label: laboratory.name}
            })) : setLaboratoriesOptions([]);
    }, [laboratories]);

    const animatedComponents = makeAnimated();
                return (
                    <div>
                        <div>
                            <div>

                                <Select
                                    placeholder={"Выберите лабораторию"}
                                    name={"select-laboratory"}
                                    isMulti
                                    components={animatedComponents}

                                    onChange={(value) =>{
                                    setSelectedLaboratory(value);
                                    setPage(1)
                                        ;}}
                                    isLoading={laboratories === undefined}
                                    options={laboratoriesOptions}
                                />
                                <Select
                                    placeholder={"Выберите анализ"}
                                    name={"select-analysis"}
                                    isMulti
                                    onInputChange={(value)=>
                                    {setSelectedInputAnalysis(value);}}
                                    components={animatedComponents}
                                    onChange={(value) =>{ setSelectedAnalysis(value);
                                    setPage(1)}

                                }
                                    isLoading={analysis === undefined}
                                    options={analysisOptions}
                                />
                                <Select
                                    placeholder={"Выберите метро"}
                                    name={"select-metro"}
                                    isMulti
                                    components={animatedComponents}
                                    onChange={(value) =>
                                    {setSelectedMetroStations(value);
                                    setPage(1)
                                    }}
                                    isLoading={metroStations === undefined}
                                    options={metroLinesOptions}

                                    onMenuScrollToBottom={(e) =>
                                    /*todo scrolll догрузка по скролу*/
                                        console.log(e)}
                                />

                                <div>


                                    <input type="checkbox" id="oms" name="oms" value="oms"
                                           onChange={(e) => setOms(e.target.checked)}/>
                                    <label htmlFor="oms">ОМС</label>
                                    <input type="checkbox" id="dms" name="dms" value="dms"
                                           onChange={(e) => setDms(e.target.checked)}/>
                                    <label htmlFor="dms">ДМС</label>
                                    <input type="checkbox" id="at-home" name="at-home" value="at-home"
                                             onChange={(e) => setAtHome(e.target.checked)}/>
                                    <label htmlFor="at-home">На дому</label>
                                    <input type="checkbox" id="fast-result" name="fast-result" value="fast-result"
                                           onChange={(e) => setFastResult(e.target.checked)}/>
                                    <label htmlFor="fast-result">Быстрый результат</label>

                                </div>
                                {/*<InputRange*/}
                                {/*    maxValue={maxMinPrice.max}*/}
                                {/*    minValue={maxMinPrice.min}*/}
                                {/*    draggableTrack*/}
                                {/*    formatLabel={value => `${value} руб.`}*/}
                                {/*    value={selectedMinMaxPrice}*/}
                                {/*    onChange={value => setSelectedMinMaxPrice(value)}*/}
                                {/*    // onChangeComplete={value => console.log(value)}*/}
                                {/*/>*/}
                            </div>

                        </div>
                    </div>
                );

        }
export default FilterForm;