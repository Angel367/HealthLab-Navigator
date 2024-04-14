import makeAnimated from "react-select/animated";
import { useState} from "react";
import Select from 'react-select';

function updateSelected(value, labs) {
    console.log(value);
    return labs.filter((lab)=> value.some((v) => v.value === lab.id_laboratory ));

}

const styles = {
  multiValue: (base, state) => {
    return state.data.isFixed ? { ...base, backgroundColor: 'gray' } : base;
  },
  multiValueLabel: (base, state) => {
    return state.data.isFixed
      ? { ...base, fontWeight: 'bold', color: 'white', paddingRight: 6 }
      : base;
  },
  multiValueRemove: (base, state) => {
    return state.data.isFixed ? { ...base, display: 'none' } : base;
  },
};



function makeOptions(labList, labelName, valueName) {
        let options = [];
        for (let i = 0; i < labList.length; i++) {
            options.push({
                value: labList[i][valueName],
                label: labList[i][labelName],
                isDisabled: false,
                isFixed: labList[i][valueName] === 1,
            });
        }
        console.log(options);
        return options;
    }
function FilterForm({options = [], setSelectedOption, labelName = 'name', valueName = 'id'}){
    const animatedComponents = makeAnimated();
    const [value, setValue] = useState(makeOptions(options, labelName, valueName).filter((v) => v.isFixed));


    const onChangeSelect = (
    newValue,
    actionMeta
  ) => {
    switch (actionMeta.action) {
      case 'remove-value':
      case 'pop-value':
        if (actionMeta.removedValue.isFixed) {
          return;
        }
        break;
      case 'clear':
        newValue = value.filter((v) => v.isFixed);
        break;
    }
    setValue(newValue);


  };
    return (
        <div>
            <h2>Фильтр</h2>
            <div>
                <div>
                    <Select
      value={value}
      isMulti
      styles={styles}
      isClearable={value.some((v) => !v.isFixed)}
      onChange={(newValue, actionMeta) => {
        onChangeSelect(newValue, actionMeta);
        if (newValue.length > 0) {
          setSelectedOption(updateSelected(newValue, options));
        } else {
            setSelectedOption(updateSelected(value.filter((v) => v.isFixed), options));
        }
      }}
      options={makeOptions(options, labelName, valueName)}
      components={animatedComponents}
      closeMenuOnSelect={false}
    />

                    {/* select for analysis */}
                    {/* select for lab name*/}
                    {/* время работы*/}
                    {/* рейтинг */}
                    {/* for location*/}
                    {/* price*/}
                    {/* duration (доплата?)*/}
                    {/* oms dms*/}
                    {/* */}

                </div>





                {/*<Select*/}
                {/*    isMulti*/}
                {/*    components={animatedComponents}*/}
                {/*    closeMenuOnSelect={false}*/}
                {/*    */}
                {/*    */}
                {/*    options={makeOptions(options, labelName, valueName)}*/}
                {/*    onInputChange={(e) => {console.log(e);}}*/}
                {/*    onChange={(selectedOption) => {*/}

                {/*    }}*/}
                {/*/>*/}
            </div>
        </div>
    );
}
export default FilterForm;