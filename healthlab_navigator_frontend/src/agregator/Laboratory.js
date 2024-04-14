import FilterForm from "./FilterForm";
import HolderAdv from "./HolderAdv";
import CardAgregator from "./CardAgregator";
import {useState} from "react";

function Laboratory() {
    const labList = [
        {
            id_laboratory: 1,
            name: 'Lab 1',
            price: 100,
            id_analysis: 1,
            duration: 1
        },
        {
            id_laboratory: 2,
            name: 'Lab 2',
            price: 200,
            id_analysis: 2,
            duration: 2
        },
        {
            id_laboratory: 3,
            name: 'Lab 3',
            price: 300,
            id_analysis: 3,
            duration: 3
        }];
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
    const [selectedOption, setSelectedOption] = useState([labList[0]]);
    return (
        <main>
            <h1>Laboratory</h1>
            <FilterForm options={labList} setSelectedOption={setSelectedOption}
                        labelName='name' valueName='id_laboratory'/>
            <HolderAdv advList={advList}/>
            <div className="laboratory cards">
                {selectedOption.map((lab, index) => {
                    return (
                       <CardAgregator key={index} {...lab}/>
                    );
                })}
            </div>
        </main>
    )
}
export default Laboratory;