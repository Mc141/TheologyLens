import Header from "./Header";
import SearchInput from "./SearchInput";
import ThemesHeader from "./ThemesHeader";
import ResultsSection from "./ResultsSection";
import Footer from "./Footer";


function App() {

  return <section className="main-card">

    <Header></Header>

    <SearchInput></SearchInput>

    <ThemesHeader></ThemesHeader>
    
    <ResultsSection></ResultsSection>

    <Footer></Footer>
  </section>



}

export default App
