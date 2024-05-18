import React, {useEffect, useState} from "react";
import makeAnimated from "react-select/animated";
import Select from 'react-select';
import getData from "../requests/getData";


function FilterForm({setSelectedLaboratory, setSelectedAnalysis, maxMinPrice, setSelectedMinMaxPrice,

                      setSelectedLocation, setSelectedPeriod, setOms, setDms, setRating}) {
    const [laboratories, setLaboratories] = useState([]);
    const [analysis, setAnalysis] = useState([]);
    const [branches, setBranches] = useState([]);
    const [laboratoriesOptions, setLaboratoriesOptions] = useState([]);
    // useEffect(() => {
    //     const fetchAnalysis = async () => {
    //         const resp = await getData('/api/analysis/')
    //         setAnalysis(resp.data?.results);
    //     }
    //     fetchAnalysis();
    // }, []);
    useEffect(() => {
        const fetchLaboratories = async () => {
            const resp = await getData('/api/laboratory/')
            setLaboratories(resp.data);
        }
        fetchLaboratories();
    }, []);
    useEffect(() => {
        laboratories !== undefined ? setLaboratoriesOptions(laboratories.map(laboratory => {
                // console.log(laboratory);
                return {value: laboratory.id, label: laboratory.name}
            })) : setLaboratoriesOptions([]);
    }, [laboratories]);
    // useEffect(() => {
    //     const fetchBranches = async () => {
    //         const resp = await getData('/api/laboratory-branch/')
    //         setBranches(resp.data?.results);
    //     }
    //     fetchBranches();
    // }, []);

    // console.log(laboratoriesOptions, laboratories);
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
                                    closeMenuOnSelect={false}
                                    onChange={(value) => setSelectedLaboratory(value)}
                                    isLoading={laboratories === undefined}
                                    options={laboratoriesOptions}
                                />
                                {/*<AsyncSelect*/}
                                {/*    placeholder={"Выберите анализ"}*/}
                                {/*    name={"select-analyses"}*/}
                                {/*    isMulti*/}
                                {/*    components={animatedComponents}*/}
                                {/*    closeMenuOnSelect={false}*/}
                                {/*    onChange={(value) => setSelectedAnalysis(value)}*/}
                                {/*    options={analysis}*/}
                                {/*/>*/}
                                {/*<AsyncSelect*/}
                                {/*    name={"select-location"}*/}
                                {/*    isMulti*/}
                                {/*    components={animatedComponents}*/}
                                {/*    closeMenuOnSelect={false}*/}
                                {/*    onChange={(value) => setSelectedLocation(value)}*/}
                                {/*/>*/}
                                {/*<InputRange*/}
                                {/*  maxValue={maxMinPrice.max}*/}
                                {/*  minValue={maxMinPrice.min}*/}
                                {/*  formatLabel={value => `${value} ₽`}*/}
                                {/*  value={{min: maxMinPrice.min, max: maxMinPrice.max}}*/}
                                {/*  onChange={value => setSelectedMinMaxPrice(value)}*/}
                                {/*/>*/}
                                {/*<AsyncSelect*/}
                                {/*    name={"select-period"}*/}
                                {/*    isMulti*/}
                                {/*    components={animatedComponents}*/}
                                {/*    closeMenuOnSelect={false}*/}
                                {/*    onChange={(value) => setSelectedPeriod(value)}*/}
                                {/*/>*/}
                                <div>
                                    <input type="checkbox" id="oms" name="oms" value="oms"
                                           onChange={(e) => setOms(e.target.checked)}/>
                                    <label htmlFor="oms">ОМС</label>
                                    <input type="checkbox" id="dms" name="dms" value="dms"
                                           onChange={(e) => setDms(e.target.checked)}/>
                                    <label htmlFor="dms">ДМС</label>
                                </div>
                                {/*<InputRange*/}
                                {/*    maxValue={5}*/}
                                {/*    minValue={0}*/}
                                {/*    formatLabel={value => `${value} ⭐`}*/}
                                {/*    value={{ min: 0, max: 5 }}*/}
                                {/*    onChange={value => setRating(value)}*/}
                                {/*    onChangeComplete={value => console.log(value)}*/}
                                {/*/>*/}
                            </div>

                        </div>
                    </div>
                );

        }
export default FilterForm;