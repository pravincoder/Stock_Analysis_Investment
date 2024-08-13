'use client';

import React, { useState } from 'react';
import Header from './components/Header';
import StockInput from './components/StockInput';
import AnalysisAndInvestment from './components/AnalysisAndInvestment';

const Home = () => {
    const [stockReport, setStockReport] = useState('');
    const [investmentReport, setInvestmentReport] = useState('');
    const [error, setError] = useState(null);

    const handleResult = (stockReport, investmentReport) => {
        setStockReport(stockReport);
        setInvestmentReport(investmentReport);
        setError(null);
    };

    const handleError = (error) => {
        setStockReport('');
        setInvestmentReport('');
        setError(error);
    };

    return (
        <div>
            <Header />
            <StockInput onResult={handleResult} onError={handleError} />
            {error && <p style={styles.error}>{error}</p>}
            {stockReport && investmentReport && (
                <AnalysisAndInvestment 
                    stockReport={stockReport} 
                    investmentReport={investmentReport} 
                />
            )}
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