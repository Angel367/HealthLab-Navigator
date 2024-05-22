
import React, { useEffect, useState } from 'react';
import { Link, useNavigate, useParams } from 'react-router-dom';
import getData from "../../requests/getData";
import axiosService from "../../requests/axiosService";
import {NotificationManager} from "react-notifications";
import CreatableSelect from "react-select/creatable";
import Select from "react-select";


function LaboratoryEdit() {
    const [labData, setLabData] = useState({
        name: '',
        website: '',
        description: ''
    });
    const [branchData, setBranchData] = useState({
        id: null,
        address: null,
        metro_stations: [],
        is_main: false,
        is_active: true,
        latitude: '',
        longitude: '',
        link: '',
        working_hours: [
            { day: 'пн', open_time: '07:00', close_time: '19:30' },
            { day: 'вт', open_time: '07:00', close_time: '19:30' },
            { day: 'ср', open_time: '07:00', close_time: '19:30' },
            { day: 'чт', open_time: '07:00', close_time: '19:30' },
            { day: 'пт', open_time: '07:00', close_time: '19:30' },
            { day: 'сб', open_time: '07:00', close_time: '19:30' },
            { day: 'вс', open_time: '07:00', close_time: '19:30' }
        ]
    });
    const [branches, setBranches] = useState([] );
    const [metroStations, setMetroStations] = useState([]);
    const [metroLines, setMetroLines] = useState([]);
    const [metroLinesOptions, setMetroLinesOptions] = useState([]);
    const [branches_options, setBranchesOptions] = useState([]);
    const navigate = useNavigate();
    const { id_laboratory} = useParams();

    useEffect(() => {
        async function fetchLabData() {
            const response = await getData(`/api/medical-institution/${id_laboratory}/`);
            if (response.data) {
                setLabData({
                    name: response.data.name || '',
                    website: response.data.website || '',
                    description: response.data.description || ''
                });
            }
        }
        fetchLabData();
    }, [id_laboratory]);
    useEffect(() => {
        async function fetchBranches() {
            const response = await getData(`/api/medical-institution-branch/?medical_institution=${id_laboratory}`);
            if (response.data) {
                setBranches(response.data?.results);
            }
        }
        fetchBranches();
    }, [id_laboratory]);
    useEffect(() => {
        async function fetchMetroStations() {
            const response = await getData(`/api/metro-station/`);
            if (response.data) {
                setMetroStations(response.data?.results);
            }
        }
        fetchMetroStations();
    }, []);
    useEffect(() => {
        async function fetchMetroLines() {
            const response = await getData(`/api/metro-line/`);
            if (response.data) {
                setMetroLines(response.data?.results);
            }
        }
        fetchMetroLines();
    }, []);

    useEffect(() => {
    if (metroLines !== undefined && metroStations !== undefined) {
        // console.log('metroLines', metroLines);
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
    if (branches !== undefined)
        setBranchesOptions(
            branches.map(branch => ({
            value: branch.id,
            label: branch.address
            }))
        );

    }, [branches]);

    const handleChange = (e) => {
        const { name, value } = e.target;
        setLabData({ ...labData, [name]: value });
    };
    const handleBranchFieldChange = (e) => {
        const { name, value } = e.target;
        if (name === 'is_main' || name === 'is_active') {
            setBranchData({ ...branchData, [name]: e.target.checked });
            return;
        }
        setBranchData({ ...branchData, [name]: value });
    };

    const handleMetroChange = (selectedOption) => {
        setBranchData({ ...branchData, metro_stations: selectedOption });
    };

    const handleWorkingHoursChange = (index, field, value) => {
        const updatedWorkingHours = [...branchData.working_hours];
        updatedWorkingHours[index][field] = value;
        console.log('updatedWorkingHours', updatedWorkingHours);
        setBranchData({ ...branchData, working_hours: updatedWorkingHours });
    };
    const handleSubmit = async (e) => {
        e.preventDefault();
         try {
            axiosService.put(`/api/medical-institution/${id_laboratory}/`, labData)
                // .then(navigate(`/laboratory/${id_laboratory}`))
                .then((response) => {
                    if (response.status === 200) {
                        // NotificationManager.success('Данные успешно сохранены');
                    }
                })
                .catch(error => {
                    NotificationManager.error('Ошибка при сохранении данных');
                });

        }
        catch (error) {
            console.error("Error updating analysis:", error);
        }
    };
    const handleSubmitBranch = async (e) => {
        e.preventDefault();

        try {
            if (branchData.id) {

                console.log('branchData', branchData);
                axiosService.put(`/api/medical-institution-branch/${branchData.id}/`, branchData)
                    // .then(navigate(`/laboratory/${id_laboratory}`))
                    .then((response) => {
                        if (response.status === 200) {
                            // NotificationManager.success('Данные успешно сохранены');
                        }
                    })
                    .catch(error => {
                        NotificationManager.error('Ошибка при сохранении данных');
                    });
            } else {
                axiosService.post(`/api/medical-institution-branch/`, {
                    ...branchData,
                    medical_institution: id_laboratory
                })
                    .then(navigate(`/laboratory/${id_laboratory}`))
                    .then((response) => {
                        if (response.status === 201) {
                            NotificationManager.success('Данные успешно сохранены');
                        }
                    })
                    .catch(error => {
                        NotificationManager.error('Ошибка при сохранении данных');
                    });
            }
        }
        catch (error) {
            console.error("Error updating analysis:", error);
        }
    }
    const handleBranchChange = (selectedOption) => {
        if (selectedOption) {
            // Fetch branch details if an existing branch is selected
            setBranchData(branches.find(branch => branch.id === selectedOption.value));
            console.log('selectedOption', selectedOption, branchData);


        } else {
            console.log('creating new branch', selectedOption);
            // Reset branch data if a new branch is being created
            setBranchData({
                ...branchData,
                id: null,
                metro_stations: [],
                latitude: '',
                longitude: '',
                url: '',
                is_active: true,
                is_main: false,
                working_hours: []
            });
        }
    };

    return (
        <div className="container mt-5">
            <div className="row justify-content-center">
                <div className="col-md-8">
                    <div className="card">
                        <div className="card-header">
                            <h1 className="card-title">Редактировать Лабораторию</h1>
                        </div>
                        <div className="card-body">
                            <form onSubmit={(e) => {
                                handleSubmit(e)
                                if (branchData.address) {
                                    handleSubmitBranch(e);
                            }   } } method={"post"}>
                                <div className="mb-3">
                                    <label htmlFor="name" className="form-label">Название</label>
                                    <input
                                        type="text"
                                        className="form-control"
                                        id="name"
                                        name="name"
                                        value={labData.name}
                                        disabled={true}
                                        // onChange={handleChange}
                                    />
                                </div>
                                <div className="mb-3">
                                    <label htmlFor="website" className="form-label">Сайт</label>
                                    <input
                                        type="url"
                                        className="form-control"
                                        id="website"
                                        name="website"
                                        value={labData.website}
                                        onChange={handleChange}
                                    />
                                </div>
                                <div className="mb-3">
                                    <label htmlFor="description" className="form-label">Описание</label>
                                    <textarea
                                        className="form-control"
                                        id="description"
                                        name="description"
                                        value={labData.description}
                                        onChange={handleChange}
                                        rows={15}
                                        maxLength={500}
                                    />
                                </div>
                                {/*<div className="mb-3">*/}
                                {/*    <label htmlFor="image" className="form-label">Изображение</label>*/}
                                {/*    <input*/}
                                {/*        type="file"*/}
                                {/*        className="form-control"*/}
                                {/*        id="image"*/}
                                {/*        name="image"*/}
                                {/*    />*/}
                                {/*</div>*/}

                                <div className="mb-3">
                                    <label htmlFor="address" className="form-label">Адрес</label>
                                    {/*<CreatableSelect*/}
                                    <Select
                                        id="address"
                                        name="address"
                                        // value={branchData.address}
                                        onChange={handleBranchChange}
                                        options={branches_options}
                                        // isClearable
                                        placeholder="Выберите филиал по адресу" // или создайте новый"
                                        // formatCreateLabel={(inputValue) => `Создать новый филиал "${inputValue}"`}
                                    />
                                </div>
                                {branchData?.address && (
                                    <>
                                        <div className="mb-3">
                                            <label htmlFor="metro" className="form-label">Метро</label>
                                            <Select
                                                id="metro"
                                                name="metro"
                                                isMulti
                                                value={branchData.metro_stations.map(station => ({
                                                    value: station.id,
                                                    label: station.name
                                                })) || []}
                                        isDisabled={true}

                                                // onChange={handleMetroChange}
                                                options={metroLinesOptions}
                                                placeholder={"Выберите станции метро"}
                                            />
                                        </div>
                                        <div className="mb-3">
                                            <label htmlFor="latitude" className="form-label">Широта</label>
                                            <input
                                                type="number"
                                                className="form-control"
                                                id="latitude"
                                                name="latitude"
                                                value={branchData.latitude}
                                                onChange={handleBranchFieldChange}
                                            />
                                        </div>
                                        <div className="mb-3">
                                            <label htmlFor="longitude" className="form-label">Долгота</label>
                                            <input
                                                type="number"
                                                className="form-control"
                                                id="longitude"
                                                name="longitude"
                                                value={branchData.longitude}
                                                onChange={handleBranchFieldChange}
                                            />
                                        </div>
                                        <div className="mb-3">
                                            <label htmlFor="link" className="form-label">Ссылка</label>
                                            <input
                                                type="url"
                                                className="form-control"
                                                id="url"
                                                name="url"
                                                value={branchData.url}
                                                onChange={handleBranchFieldChange}
                                            />
                                        </div>
                                        {/*<div className="mb-3">*/}
                                        {/*    <label className="form-label">Часы работы</label>*/}
                                        {/*    {branchData.working_hours.map((wh, index) => (*/}
                                        {/*        <div key={index} className="d-flex align-items-center mb-2">*/}
                                        {/*            <span className="me-2">{wh.day.toUpperCase()}:</span>*/}
                                        {/*            <input*/}
                                        {/*                type="time"*/}
                                        {/*                className="form-control me-2"*/}
                                        {/*                value={wh.open_time}*/}
                                        {/*                onChange={(e) => handleWorkingHoursChange(index, 'open_time', e.target.value)}*/}
                                        {/*            />*/}
                                        {/*            <span className="me-2">-</span>*/}
                                        {/*            <input*/}
                                        {/*                type="time"*/}
                                        {/*                className="form-control"*/}
                                        {/*                value={wh.close_time}*/}
                                        {/*                onChange={(e) => handleWorkingHoursChange(index, 'close_time', e.target.value)}*/}
                                        {/*            />*/}
                                        {/*        </div>*/}
                                        {/*    ))}*/}
                                        {/*</div>*/}
                                        <div className="mb-3">
                                            <input type={"checkbox"} id={"is_main"} name={"is_main"}
                                                    defaultChecked={branchData.is_main}

                                                   onChange={handleBranchFieldChange}
                                                   className={"form-check-input"} />
                                            <label className={"form-check-label"} htmlFor={"is_main"}>Главный филиал</label>
                                        </div>
                                        <div className="mb-3">
                                            <input type={"checkbox"} id={"is_active"} name={"is_active"}
                                                   defaultChecked={branchData.is_active}

                                                   onChange={handleBranchFieldChange}
                                                   className={"form-check-input"} />
                                            <label className={"form-check-label"} htmlFor={"is_active"}>Активный</label>
                                        </div>
                                    </>
                                )}

                                    <button type="submit" className="btn btn-primary">Сохранить</button>
                                    <Link to={`/laboratory/${id_laboratory}`} className="btn btn-link">Отмена
                            </Link>
                        </form>
                    </div>
                </div>
            </div>
        </div>
</div>
)
    ;
}

export default LaboratoryEdit;
