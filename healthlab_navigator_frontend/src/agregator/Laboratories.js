import FilterForm from "./FilterForm";
import HolderAdv from "./HolderAdv";
import CardAgregator from "./CardAgregator";
import {useState} from "react";

function Laboratories() {
    const [selectedItems, setSelectedItems] = useState([]);
    // selectedItems is
    // const []
    return (
        <main>
            {/*<h1>Лаборатории</h1>*/}
            {/*<FilterForm options={labList} setSelectedOption={setSelectedItems}*/}
            {/*            labelName='name' valueName='id_laboratory'/>*/}
            {/*<HolderAdv advList={advList}/>*/}
            {/*<div className="laboratory cards">*/}
            {/*    {selectedItems.map((lab, index) => {*/}
            {/*        return (*/}
            {/*           <CardAgregator key={index} {...lab}/>*/}
            {/*        );*/}
            {/*    })}*/}
            {/*</div>*/}
        </main>
    )
}
export default Laboratories;