import VerseCard from "./VerseCard";


function ResultsSection() {
    return <>
        <h2 className="results-title">Results</h2>
        <ul className="overflow-auto">
            <li><VerseCard></VerseCard></li>

            <li><VerseCard></VerseCard></li>
            
            <li><VerseCard></VerseCard></li>

            <li><VerseCard></VerseCard></li>
        </ul>
    </>
}


export default ResultsSection;