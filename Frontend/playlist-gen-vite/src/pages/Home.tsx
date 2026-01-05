import MainContainer from "../components/MainContainer";
import SideContainer from "../components/SideContainer";
import "./Home.css";

function Home() {
    return (
        <>
            <h1 className="title">Wassup</h1>
            <div className="screenContent">
                <MainContainer>
                    <h1>Create Playlist</h1>
                </MainContainer>
                <div className="right">
                    <SideContainer>
                    Right Side
                    </SideContainer>
                </div>
            </div>
        </>
    );
}

export default Home
