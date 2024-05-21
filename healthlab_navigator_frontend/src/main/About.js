function About() {
    return (
        <div className={"container d-flex flex-column justify-content-between mt-5 mb-5"}>
            <h1>
                Курсовая работа по РКСП
            </h1>
            <h3>
            Разработка веб-приложения для агрегации медицинских лабораторий
            </h3>
            <div className={"d-flex gap-4"}>
            <div className={"d-flex flex-column card"}>
                <div className={"card-header"}>
                    <h2 className={"card-title"}>
                        ИКБО-01-21 Исаева АВ
                    </h2>
                </div>
                <img className={"card-img-top"} width={"100px"} height={"auto"} style={{objectFit: "cover"}}
                     src={"https://sun9-18.userapi.com/impg/6f-b53hdXUd039PvDwVpfhzygMYMvC2runKtqw/FeapnYFe5mA.jpg?size=1600x900&quality=96&sign=d65238fc964429d8f2d29923bf14b73c&type=album"} alt={"Isaeva AV"}/>
            </div>
            <div className={"d-flex flex-column card"}>
                <div className={"card-header"}>
                    <h2 className={"card-title"}>
                        ИКБО-24-21 Волков ЕА
                    </h2>
                </div>
                <img className={"card-img-top"} width={"100px"} height={"auto"} style={{objectFit: "cover"}}
                     src={"https://sun9-7.userapi.com/impg/Ely_RgkvE5tX46CeCMcvyqcvyO1g9CpdwokDfw/TLYyOZwMSJs.jpg?size=1200x1600&quality=96&sign=07e0743aeeb1aaab70a2f0deac82e05b&type=album"} alt={"Volkov EA"}/>
            </div>
            </div>
        </div>
    );
}

export default About;