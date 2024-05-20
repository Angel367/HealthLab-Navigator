import React, { useEffect, useState } from 'react';
import makeAnimated from 'react-select/animated';
import Select from 'react-select';
import getData from '../requests/getData';
import InputRange from 'react-input-range';
import 'react-input-range/lib/css/index.css';

function FilterForm({
  setSelectedLaboratory,
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
  setDms
}) {
  const [analysis, setAnalysis] = useState([]);
  const [laboratoriesOptions, setLaboratoriesOptions] = useState([]);
  const [analysisOptions, setAnalysisOptions] = useState([]);
  const [metroStations, setMetroStations] = useState([]);
  const [metroLines, setMetroLines] = useState([]);
  const [metroLinesOptions, setMetroLinesOptions] = useState([]);
  const [selectedInputAnalysis, setSelectedInputAnalysis] = useState('');

  useEffect(() => {
    const fetchAnalysis = async () => {
      const resp = await getData('/api/medical-service/', { name__icontains: selectedInputAnalysis });
      setAnalysis(resp.data?.results);
      setPage(1);
    };
    fetchAnalysis();
  }, [selectedInputAnalysis, setPage]);

  useEffect(() => {
    const fetchLaboratories = async () => {
      const resp = await getData('/api/medical-institution/');
      setLaboratories(resp.data?.results);
    };
    fetchLaboratories();
  }, [setLaboratories]);

  useEffect(() => {
    if (analysis) {
      setAnalysisOptions(analysis.map(a => ({ value: a.id, label: a.name })));
    } else {
      setAnalysisOptions([]);
    }
  }, [analysis]);

  useEffect(() => {
    const fetchMetroLines = async () => {
      let page_l = 1;
      let metro_lines = [];
      while (true) {
        const resp = await getData(`/api/metro-line/?page=${page_l}`);
        metro_lines.push(resp.data?.results);
        if (resp.data?.next === null) break;
        page_l++;
      }
      setMetroLines(metro_lines.flat());
    };
    fetchMetroLines();
  }, []);

  useEffect(() => {
    const fetchMetroStations = async () => {
      let page = 1;
      let metro_stations = [];
      while (true) {
        const resp = await getData(`/api/metro-station/?page=${page}`);
        metro_stations.push(resp.data?.results);
        if (resp.data?.next === null) break;
        page++;
      }
      setMetroStations(metro_stations.flat());
    };
    fetchMetroStations();
  }, []);

  useEffect(() => {
    if (metroLines) {
      setMetroLinesOptions(
        metroLines.map(metroLine => ({
          label: metroLine?.name || '',
          options: metroStations.filter(station => station.line?.id === metroLine.id).map(station => ({
            value: station?.id,
            label: station?.name || ''
          }))
        }))
      );
    } else {
      setMetroLinesOptions([]);
    }
  }, [metroLines, metroStations]);

  useEffect(() => {
    if (laboratories) {
      setLaboratoriesOptions(
        laboratories.map(laboratory => ({ value: laboratory.id, label: laboratory.name }))
      );
    } else {
      setLaboratoriesOptions([]);
    }
  }, [laboratories]);

  const animatedComponents = makeAnimated();

  return (
    <div className="container mt-4">
      <div className="row">
        <div className="col-12 mb-3">
          <Select
            placeholder="Выберите лабораторию"
            name="select-laboratory"
            isMulti
            components={animatedComponents}
            onChange={value => {
              setSelectedLaboratory(value);
              setPage(1);
            }}
            isLoading={laboratories === undefined}
            options={laboratoriesOptions}
            className="basic-multi-select"
            classNamePrefix="select"
          />
        </div>
        <div className="col-12 mb-3">
          <Select
            placeholder="Выберите анализ"
            name="select-analysis"
            isMulti
            onInputChange={value => setSelectedInputAnalysis(value)}
            components={animatedComponents}
            onChange={value => {
              setSelectedAnalysis(value);
              setPage(1);
            }}
            isLoading={analysis === undefined}
            options={analysisOptions}
            className="basic-multi-select"
            classNamePrefix="select"
          />
        </div>
        <div className="col-12 mb-3">
          <Select
            placeholder="Выберите метро"
            name="select-metro"
            isMulti
            components={animatedComponents}
            onChange={value => {
              setSelectedMetroStations(value);
              setPage(1);
            }}
            isLoading={metroStations === undefined}
            options={metroLinesOptions}
            className="basic-multi-select"
            classNamePrefix="select"
            onMenuScrollToBottom={e => console.log(e)} // Placeholder for infinite scroll functionality
          />
        </div>
        <div className="col-12 mb-3">
          <div className="form-check">
            <input type="checkbox" id="oms" name="oms" className="form-check-input" onChange={e => setOms(e.target.checked)} />
            <label className="form-check-label" htmlFor="oms">ОМС</label>
          </div>
          <div className="form-check">
            <input type="checkbox" id="dms" name="dms" className="form-check-input" onChange={e => setDms(e.target.checked)} />
            <label className="form-check-label" htmlFor="dms">ДМС</label>
          </div>
          <div className="form-check">
            <input type="checkbox" id="at-home" name="at-home" className="form-check-input" onChange={e => setAtHome(e.target.checked)} />
            <label className="form-check-label" htmlFor="at-home">На дому</label>
          </div>
          <div className="form-check">
            <input type="checkbox" id="fast-result" name="fast-result" className="form-check-input" onChange={e => setFastResult(e.target.checked)} />
            <label className="form-check-label" htmlFor="fast-result">Быстрый результат</label>
          </div>
        </div>
        <div className="col-12 mb-3">
          <InputRange
            maxValue={maxMinPrice.max}
            minValue={maxMinPrice.min}
            value={selectedMinMaxPrice}
            onChange={value => setSelectedMinMaxPrice(value)}
            formatLabel={value => `${value} руб.`}
          />
        </div>
      </div>
    </div>
  );
}

export default FilterForm;
