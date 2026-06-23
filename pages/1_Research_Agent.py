def research_agent(query):

    memory = recall_memory("Research")

    sources = web_search(query)

    prompt = f"""
You are NEXORA Research Agent.

Previous Memory:
{memory}

Web Sources:
{sources}

User Query:
{query}

Create a detailed research report:

1. Overview
2. Latest Information
3. Key Findings
4. Advantages / Disadvantages
5. Future Scope
6. Conclusion

Use the sources intelligently.
"""


    response = groq_chat(prompt)


    save_memory(
        "Research",
        query
    )


    return response