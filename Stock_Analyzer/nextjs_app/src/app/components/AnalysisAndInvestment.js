import React from 'react';
import ReactMarkdown from 'react-markdown';
import remarkGfm from 'remark-gfm'; // GitHub Flavored Markdown support

const AnalysisAndInvestment = ({ stockReport, investmentReport }) => {
    return (
        <div className="flex flex-col mt-8 space-y-4">
            <div className="w-full border border-gray-300 rounded-lg p-6 bg-white shadow-lg">
                <h3 className="text-xl font-semibold mb-4">Stock Analysis</h3>
                <ReactMarkdown
                    className="prose prose-lg"
                    remarkPlugins={[remarkGfm]}
                >
                    {stockReport}
                </ReactMarkdown>
            </div>
            <div className="w-full border border-gray-300 rounded-lg p-6 bg-white shadow-lg">
                <h3 className="text-xl font-semibold mb-4">Investment Analysis</h3>
                <ReactMarkdown
                    className="prose prose-lg"
                    remarkPlugins={[remarkGfm]}
                >
                    {investmentReport}
                </ReactMarkdown>
            </div>
        </div>
    );
};

export default AnalysisAndInvestment;
