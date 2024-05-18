import FilterForm from "./FilterForm";
import HolderAdv from "./HolderAdv";
import CardAnalysis from "./CardAnalysis";
import {Link, Navigate, useParams} from "react-router-dom";
import {isRole} from "../hooks/user.actions";
import {useEffect, useState} from "react";
import getData from "../requests/getData";


function LaboratoryPage() {
    const {id_laboratory} = useParams();
    const [laboratory, setLaboratory] = useState({});
    const [branches, setBranches] = useState([]);
    const [offers, setOffers] = useState([]);
    const [reviews, setReviews] = useState([]);

    useEffect(() => {
        const fetchLaboratory = async () => {
            const resp = await getData(`/api/laboratory/${id_laboratory}/`);
            setLaboratory(resp.data);
        }
        fetchLaboratory();
    }, [id_laboratory]);
    useEffect(() => {
        const fetchBranches = async () => {
            const resp = await getData(`/api/laboratory-branch/`, {id_laboratory: id_laboratory});
            setBranches(resp.data);
        }
        fetchBranches();
    }, [id_laboratory]);
    useEffect(() => {
        const fetchOffers = async () => {
            const resp = await getData(`/api/special-offer/`, {id_laboratory: id_laboratory});
            setOffers(resp.data);
        }
        fetchOffers();
    }, [id_laboratory]);
    useEffect(() => {
        const fetchReviews = async () => {
            const resp = await getData(`api/reviews/`, {id_laboratory: id_laboratory});
            setReviews(resp.data);
        }
        fetchReviews();
    }, [id_laboratory]);



    return (
        <div>
            <h1>{laboratory.name}</h1>
            {isRole("medical_institution_agent") ?
                <Link to={`/laboratory/${id_laboratory}/edit`} > Редактировать </Link> :
                null
            }
            <p>{laboratory.description}</p>
            <a href={laboratory.website}>Перейти на сайт</a>

            {/*todo offers*/}
            {/*{offers.length > 0 ?*/}
            {/*    <div>*/}
            {/*        <h2>Акции</h2>*/}
            {/*        {offers.map((offer, index) => {*/}
            {/*            return (*/}
            {/*                <div key={index}>*/}
            {/*                    <h3>{offer.name}</h3>*/}
            {/*                    <p>{offer.description}</p>*/}
            {/*                    <p>{offer.date_start} - {offer.date_end}</p>*/}
            {/*                </div>*/}
            {/*            )*/}
            {/*        })}*/}
            {/*    </div> :*/}
            {/*    null*/}
            {/*}*/}

            {/*todo reviews*/}

            {branches !== undefined && branches.length > 0  ?
                <div>
                    <h2>Филиалы</h2>
                    {branches.map((branch, index) => {
                        let address = branch.address;
                        let street = address !== undefined ? address.street : undefined;
                        let addressStr = street !== undefined ?
                            `${street.district?.city?.name}, ${street.name}, ${street.house}` : '';
                        return (
                            <div key={index} id={"branch"+branch.id}>
                                <h3>{branch.is_main}</h3>
                                <p>{addressStr}</p>
                                <p>ПН: {branch?.working_hours?.пн}</p>
                                <p>ВТ: {branch?.working_hours?.вт}</p>
                                <p>СР: {branch?.working_hours?.ср}</p>
                                <p>ЧТ: {branch?.working_hours?.чт}</p>
                                <p>ПТ: {branch?.working_hours?.пт}</p>
                                <p>СБ: {branch?.working_hours?.сб}</p>
                                <p>ВС: {branch?.working_hours?.вс}</p>
                            </div>
                        )
                    })}
                </div> :
                null
            }
        {/*  todo add filter by this lab */}



        </div>
    )


}

export default LaboratoryPage;