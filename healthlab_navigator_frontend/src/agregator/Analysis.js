import FilterForm from "./FilterForm";
import HolderAdv from "./HolderAdv";
import CardAgregator from "./CardAgregator";
import {useState} from "react";

function Analysis() {
    const advList = [
        {
            img: "https://via.placeholder.com/150",
            title: "Adv 1"
        },
        {
            img: "https://via.placeholder.com/150",
            title: "Adv 2"
        },
        {
            img: "https://via.placeholder.com/150",
            title: "Adv 3"
        }
    ];
    const analysisList = [
        {
            id_analysis: 1,
            name: 'Analysis 1',
            price: 100,
            duration: 1,
            id_laboratory: 1
        },
        {
            id_analysis: 2,
            name: 'Analysis 2',
            price: 200,
            duration: 2,
            id_laboratory: 2
        },
        {
            id_analysis: 3,
            name: 'Analysis 3',
            price: 300,
            duration: 3,
            id_laboratory: 3
        }];
    const [selectedOption, setSelectedOption] = useState(analysisList);

    return (
        <div>
            <h1>Analysis</h1>
            <FilterForm options={analysisList} labelName='name' valueName='id_analysis' setSelectedOption={setSelectedOption}/>
            <HolderAdv advList={advList}/>
            <div className="analysis cards">
                {selectedOption.map((analysis, index) => {
                    return (
                        <CardAgregator key={index} {...analysis}/>
                    );
                })}
            </div>

        </div>
    )
}
export default Analysis;