import VerseCard from "./VerseCard";

function ResultsSection({ results }) {
  return (
    <>
      <h2 className="results-title">Results</h2>
      <ul className="overflow-auto">
        {results.length > 0 ? (
          results.map((verse, idx) => (
            <li key={idx}>
              <VerseCard verse={verse} />
            </li>
          ))
        ) : (
          <li>
            <p style={{ color: "rgb(242, 161, 161)", textAlign: "center", padding: "10px" }}>
              Start your search above to explore meaningful scripture.
            </p>
          </li>
        )}
      </ul>
    </>
  );
}

export default ResultsSection;
