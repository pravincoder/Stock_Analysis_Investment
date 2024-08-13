import { useState } from 'react';

export default function Home() {
  const [stockName, setStockName] = useState('');
  const [stockReport, setStockReport] = useState('');
  const [investmentReport, setInvestmentReport] = useState('');
  const [error, setError] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault();

    // Reset reports and error before fetching
    setStockReport('');
    setInvestmentReport('');
    setError(null);

    try {
      const response = await fetch('http://127.0.0.1:5000/analyze-stock', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ stock_name: stockName }),
      });

      if (!response.ok) {
        const errorData = await response.json();
        throw new Error(errorData.error || 'Something went wrong');
      }

      const data = await response.json();
      setStockReport(data.stock_report);
      setInvestmentReport(data.investment_report);
    } catch (err) {
      setError(err.message);
    }
  };

  return (
    <div className="bg-black text-white min-h-screen flex flex-col items-center justify-center">
      <h1 className="text-3xl font-bold mb-8">Stock Investment And Analysis Agent</h1>
      <form onSubmit={handleSubmit} className="flex flex-col items-center">
        <input
          type="text"
          value={stockName}
          onChange={(e) => setStockName(e.target.value)}
          placeholder="Enter stock name"
          className="px-4 py-2 text-black"
        />
        <button type="submit" className="mt-4 px-6 py-2 bg-blue-600 text-white rounded">
          Analyze Stock
        </button>
      </form>

      {error && <p className="text-red-500 mt-4">{error}</p>}

      {stockReport && (
        <div className="mt-8">
          <h2 className="text-xl font-bold">Stock Analysis Report</h2>
          <pre className="whitespace-pre-wrap mt-2">{stockReport}</pre>
        </div>
      )}

      {investmentReport && (
        <div className="mt-8">
          <h2 className="text-xl font-bold">Investment Analysis Report</h2>
          <pre className="whitespace-pre-wrap mt-2">{investmentReport}</pre>
        </div>
      )}
    </div>
  );
}
