function HolderAdv({advList = []}){
    if (advList.length > 0){
        return (
            <div className="holder-adv">
                {advList.map((adv, index) => {
                    return (
                        <div key={index} className="adv">
                            <img src={adv.img} alt={''} />
                            <p>{adv.title}</p>
                        </div>
                    );
                })}
            </div>
        );
    }
    return null;

}
export default HolderAdv;