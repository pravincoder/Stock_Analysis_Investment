import React, { useState } from "react";

const StockInput = ({ onAnalysisResult, onInvestmentResult, onError }) => {
  const [stockName, setStockName] = useState("");
  const [loading, setLoading] = useState(false);
  const [mode, setMode] = useState("analyze"); // Mode can be "analyze" or "invest"

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);

    const endpoint =
      mode === "analyze" ? "analyze-stock" : "invest-stock";

    try {
      const response = await fetch(`http://127.0.0.1:5000/${endpoint}`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ stock_name: stockName }),
      });

      const data = await response.json();

      if (response.ok) {
        if (mode === "analyze") {
          onAnalysisResult(data.analysis_report);
        } else {
          onInvestmentResult(data.investment_report);
        }
      } else {
        onError(data.error || "Something went wrong");
      }
    } catch (error) {
      onError("Unable to connect to the server");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="flex justify-center items-center min-h-screen bg-gray-100">
      <form
        onSubmit={handleSubmit}
        className="bg-white shadow-lg rounded-lg p-8 flex flex-col items-center space-y-4 w-full max-w-md"
      >
        <label
          htmlFor="stock-name"
          className="text-lg font-semibold text-gray-700"
        >
          Enter a stock name
        </label>
        <input
          type="text"
          placeholder="Enter stock you want to analyze or invest"
          value={stockName}
          onChange={(e) => setStockName(e.target.value)}
          className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
          disabled={loading}
        />
        <div className="flex space-x-4">
          <button
            type="button"
            onClick={() => setMode("analyze")}
            className={`${
              mode === "analyze"
                ? "bg-blue-600 text-white"
                : "bg-gray-300 text-gray-700"
            } px-4 py-2 rounded-lg`}
          >
            Analyze
          </button>
          <button
            type="button"
            onClick={() => setMode("invest")}
            className={`${
              mode === "invest"
                ? "bg-blue-600 text-white"
                : "bg-gray-300 text-gray-700"
            } px-4 py-2 rounded-lg`}
          >
            Invest
          </button>
        </div>
        <button
          type="submit"
          className={`w-full text-white bg-gradient-to-r from-blue-500 via-blue-600 to-blue-700 hover:bg-gradient-to-br focus:ring-4 focus:outline-none focus:ring-blue-300 shadow-lg font-medium rounded-lg text-sm px-5 py-2.5 text-center ${
            loading
              ? "cursor-not-allowed opacity-50"
              : "hover:shadow-blue-500/50"
          }`}
          disabled={loading}
        >
          {loading ? "Processing..." : mode === "analyze" ? "Analyze" : "Invest"}
        </button>
      </form>
    </div>
  );
};

export default StockInput;
