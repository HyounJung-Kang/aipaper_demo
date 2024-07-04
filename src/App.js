import React, { useState } from 'react';

const App = () => {
  const [activeTab, setActiveTab] = useState('search');
  const [searchResults, setSearchResults] = useState([]);
  const [selectedPaper, setSelectedPaper] = useState(null);
  const [summary, setSummary] = useState('');
  const [translation, setTranslation] = useState('');
  const [algorithmCode, setAlgorithmCode] = useState('// Your algorithm code here');

  // Dummy Search Function
  const handleSearch = (query) => {
    setSearchResults([
      { title: "Deep Learning", author: "Ian Goodfellow" },
      { title: "Reinforcement Learning: An Introduction", author: "Richard S. Sutton" }
    ]);
  };

  const handleSummarize = () => {
    setSummary('This is a summary of the paper.');
  };

  const handleTranslate = () => {
    setTranslation('This is a translation of the paper.');
  };

  const updateAlgorithm = (newCode) => {
    setAlgorithmCode(newCode);
  };

  const runAlgorithm = () => {
    console.log('Running Algorithm:', algorithmCode);
  };

  return (
    <div>
      <nav>
        <button onClick={() => setActiveTab('search paper')}>Search AI Papers</button>
        <button onClick={() => setActiveTab('summary')}>Summarize/Translate</button>
        <button onClick={() => setActiveTab('algorithm')}>AI Algorithm</button>
      </nav>
      {activeTab === 'search' && (
        <div>
          <input type="text" placeholder="Search..." onChange={(e) => handleSearch(e.target.value)} />
          <ul>
            {searchResults.map((paper, index) => (
              <li key={index} onClick={() => setSelectedPaper(paper)}>{paper.title} - {paper.author}</li>
            ))}
          </ul>
        </div>
      )}
      {activeTab === 'summary' && selectedPaper && (
        <div>
          <h2>{selectedPaper.title}</h2>
          <button onClick={handleSummarize}>Summarize</button>
          <button onClick={handleTranslate}>Translate</button>
          <div>
            <h3>Summary</h3>
            <p>{summary}</p>
            <h3>Translation</h3>
            <p>{translation}</p>
          </div>
        </div>
      )}
      {activeTab === 'algorithm' && (
        <div>
          <textarea value={algorithmCode} onChange={(e) => updateAlgorithm(e.target.value)} />
          <button onClick={runAlgorithm}>Run Code</button>
        </div>
      )}
    </div>
  );
};

export default App;

