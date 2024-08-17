import React from 'react';
import ReactMarkdown from 'react-markdown';
import remarkGfm from 'remark-gfm'; // GitHub Flavored Markdown support

const Investment = ({ investment_report }) => {
    return (
        <div className="flex justify-center mt-8">
            <div className="w-full max-w-3xl border border-gray-300 rounded-lg p-6 bg-white shadow-lg">
                <h3 className="text-2xl font-semibold mb-4 text-center">Stock Analysis</h3>
                <ReactMarkdown
                    className="prose prose-lg"
                    remarkPlugins={[remarkGfm]}
                >
                    {investment_report}
                </ReactMarkdown>
            </div>
        </div>
    );
};

export default Investment;