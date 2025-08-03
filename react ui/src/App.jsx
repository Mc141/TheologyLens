import { useState } from "react";
import Header from "./Header";
import SearchInput from "./SearchInput";
import ResultsSection from "./ResultsSection";
import Footer from "./Footer";

function App() {
  const [results, setResults] = useState([]);

  const API_URL = import.meta.env.VITE_API_URL || "http://127.0.0.1:8000";

  const handleSearch = async (query) => {
    if (!query.trim()) return;

    const res = await fetch(`${API_URL}/search`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ question: query }),
    });

    const data = await res.json();
    setResults(data);
  };

  return (
    <section className="main-card">
      <Header />
      <SearchInput onSearch={handleSearch} />
      <ResultsSection results={results} />
      <Footer />
    </section>
  );
}

export default App;
