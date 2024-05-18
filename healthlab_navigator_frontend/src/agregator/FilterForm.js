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
                        setAtHome,
                        setFastResult,
                        setSelectedAnalysis,
                        laboratories,
                        setSelectedMetroStations,
                       setOms,
                        setDms}) {

    const [analysis, setAnalysis] = useState([]);
    const [laboratoriesOptions, setLaboratoriesOptions] = useState([]);
    const [analysisOptions, setAnalysisOptions] = useState([]);
    const [metroStations, setMetroStations] = useState([]);

    const [metroLines, setMetroLines] = useState([]);
    const [metroLinesOptions, setMetroLinesOptions] = useState([]);
    useEffect(() => {
        const fetchAnalysis = async () => {
            const resp = await getData('/api/medical-service/')
            setAnalysis(resp.data?.results);
        }
        fetchAnalysis();
    }, []);
    useEffect(() => {
        analysis !== undefined
            ? setAnalysisOptions(analysis.map(analysis => {
                return {value: analysis.id, label: analysis.name}
            })) : setAnalysisOptions([]);
    }, [analysis]);
    useEffect(() => {
        const fetchMetroLines = async () => {
            const resp = await getData('/api/metro-line/')
            setMetroLines(resp.data?.results);
        }
        fetchMetroLines();
    }, []);

    useEffect(() => {
        const fetchMetroStations = async () => {
            const resp = await getData('/api/metro-station/')
            setMetroStations(resp.data?.results);
        }
        fetchMetroStations();
    }, []);
     useEffect(() => {
        metroLines !== undefined
            ? setMetroLinesOptions(metroLines.map(metroLine => {
                console.log(metroLine.name)
                return { label: metroLine.name,
                    options: metroStations.filter(station => station.line?.id === metroLine.id).map(station => {

                        return {value: station.id, label: station.name}
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

                                    onChange={(value) => setSelectedLaboratory(value)}
                                    isLoading={laboratories === undefined}
                                    options={laboratoriesOptions}
                                />
                                <Select
                                    placeholder={"Выберите анализ"}
                                    name={"select-analysis"}
                                    isMulti

                                    components={animatedComponents}
                                    onChange={(value) => setSelectedAnalysis(value)}
                                    isLoading={analysis === undefined}
                                    options={analysisOptions}
                                />
                                <Select
                                    placeholder={"Выберите метро"}
                                    name={"select-metro"}
                                    isMulti
                                    components={animatedComponents}
                                    onChange={(value) => setSelectedMetroStations(value)}
                                    isLoading={metroStations === undefined}
                                    options={metroLinesOptions}
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
                                <InputRange
                                    maxValue={maxMinPrice.max}
                                    minValue={maxMinPrice.min}
                                    draggableTrack
                                    formatLabel={value => `${value} руб.`}
                                    value={selectedMinMaxPrice}
                                    onChange={value => setSelectedMinMaxPrice(value)}
                                    // onChangeComplete={value => console.log(value)}
                                />
                            </div>

                        </div>
                    </div>
                );

        }
export default FilterForm;