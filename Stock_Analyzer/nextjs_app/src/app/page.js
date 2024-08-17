'use client';

import React, { useState } from 'react';
import Header from './components/Header';
import StockInput from './components/StockInput';
import Analysis from './components/Analysis';
import Investment from './components/investment';

const Home = () => {
  const [analysis_report, setAnalysisReport] = useState('');
  const [investment_report, setInvestmentReport] = useState('');
  const [error, setError] = useState(null);

  const handleAnalysisResult = (report) => {
    setAnalysisReport(report);
    setError(null);
  };

  const handleInvestmentResult = (report) => {
    setInvestmentReport(report);
    setError(null);
  };

  const handleError = (error) => {
    setAnalysisReport('');
    setInvestmentReport('');
    setError(error);
  };

  return (
    <div>
      <Header />
      <StockInput
        onAnalysisResult={handleAnalysisResult}
        onInvestmentResult={handleInvestmentResult}
        onError={handleError}
      />
      {error && <p style={styles.error}>{error}</p>}
      {analysis_report && <Analysis analysis_report={analysis_report} />}
      {investment_report && <Investment investment_report={investment_report} />}
    </div>
  );
};

const styles = {
  error: {
    color: 'red',
    textAlign: 'center',
    marginTop: '20px',
  },
};

export default Home;
