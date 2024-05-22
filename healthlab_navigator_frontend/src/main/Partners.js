import {Link} from "react-router-dom";

function Partners() {

    return (
        <div className={"container d-flex flex-column mt-5 mb-5 gap-4"}>
            <h1 className={"text-center"}
            >Наши партнеры</h1>
            <div> Партнерство позволяет развивать наш проект, а значит и улучшать качество предоставляемых услуг.
                Это позволяет нам предоставлять больше информации о лабораториях и анализах для наших пользователей,
                а также делать продукты наших партнеров более доступными.
            </div>
            <div className={"d-flex flex-row justify-content-around align-items-center gap-4"}>
                <div className={"card d-flex flex-column justify-content-between  gap-4"}>
                    <img alt={""} src={"https://cdn1.flamp.ru/cd1d154836c8e7d59a0da017d8e1d380.png"} height={"200px"}
                    width={"200px"} className={"align-self-center"}
                    />
                    <div className={"card-header"}>
                    <h2 className={"card-title text-center"}>
                        Гемотест
                    </h2>
                </div>
                <div className={"card-body"}>
                    <div className={"card-text"} >
                        Наш партнер с 2025 года. Гемотест - это сеть лабораторий,
                        которая предоставляет широкий спектр анализов. Они продолжают развиваться и улучшать качество своих
                        услуг,
                        превращаясь в цифровую лабораторию с возможностью проведения врачебных приемов как в оффлайн, так и
                        в онлайн формате.
                        Помимо этого, Гемотест предоставляет возможность сдачи анализов и некоторых процедур на дому.
                    </div>
                    <Link to={"/laboratory/1"} className={"btn btn-light"}>Подробнее</Link>
                </div>
                </div>
                <div className={"card d-flex flex-column justify-content-between  gap-4"}>

                    <img alt={""} src={"https://p2.zoon.ru/1/e/5a6489a5a24fd9100f094bbf_628b05e7b38a94.19357826.jpg"} height={"200px"}/>
                    <div className={"card-header"}>
                    <h2 className={"card-title text-center"}>
                        KDL
                    </h2>
                    </div>
                    <div className={"card-body"}>
                    <div className={"card-text"}>
                        Наш партнер с 2025 года. КДЛ - это сеть лабораторий, которая предоставляет широкий спектр анализов.
                        Они продолжают развиваться и улучшать качество своих услуг, превращаясь в цифровую лабораторию с возможностью
                        проведения врачебных приемов как в оффлайн, так и в онлайн формате. Помимо этого, КДЛ предоставляет возможность
                        сдачи анализов и некоторых процедур на дому.
                    </div>
                    <Link to={"/laboratory/2"} className={"btn btn-light"}>Подробнее</Link>

                    </div>
                </div>
            </div>
        </div>
    );
}
export default Partners;