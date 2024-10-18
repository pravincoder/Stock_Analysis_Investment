import os
from langchain.tools import tool


class ExaSearchTool:
    @tool
    def search(stock: str):
        """Search for a webpage based on the stock.
        query: (str)."""
        return ExaSearchTool._exa().search(
            query=stock, use_autoprompt=True, num_results=3
        )

    @tool
    def find_similar(url: str):
        """Search for webpages similar to a given URL.
        The url passed in should be a URL returned from `search`.
        """
        return ExaSearchTool._exa().find_similar(url, num_results=3)

    @tool
    def get_contents(ids: str):
        """Get the contents of a webpage.
        The ids must be passed in as a list, a list of ids returned from `search`.
        """

        print("ids from param:", ids)

        ids = eval(ids)
        print("eval ids:", ids)

        contents = str(ExaSearchTool._exa().get_contents(ids))
        print(contents)
        contents = contents.split("URL:")
        contents = [content[:1000] for content in contents]
        return "\n\n".join(contents)

    def tools():
        return [
            ExaSearchTool.search,
            ExaSearchTool.find_similar,
            ExaSearchTool.get_contents,
        ]

