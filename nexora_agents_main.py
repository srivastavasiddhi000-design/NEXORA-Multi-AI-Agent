from core.rag import chunk_text, retrieve_context
from core.search import web_search
from core.llm import groq_chat
from core.memory import save_memory, recall_memory



def research_agent(query):

    memory = recall_memory("Research")


    prompt = f"""
You are NEXORA Research Agent.

Previous Research Memory:
{memory}

User query:
{query}

Give:
1. Overview
2. Key Points
3. Analysis
4. Conclusion
"""


    response = groq_chat(prompt)


    save_memory(
        "Research",
        query
    )


    return response





def knowledge_agent(query):


    memory = recall_memory("Knowledge")


    prompt = f"""
You are NEXORA Knowledge Agent.

Previous Knowledge Memory:
{memory}

User query:
{query}

Explain clearly with examples.
"""


    response = groq_chat(prompt)


    save_memory(
        "Knowledge",
        query
    )


    return response






def planner_agent(query):


    memory = recall_memory("Planner")


    prompt = f"""
You are NEXORA Planning Agent.

Previous Planning Memory:
{memory}

User request:
{query}


Create:

1. Goal
2. Strategy
3. Steps
4. Timeline
5. Success metrics
"""


    response = groq_chat(prompt)


    save_memory(
        "Planner",
        query
    )


    return response






def code_agent(query):


    memory = recall_memory("Code")


    prompt = f"""
You are NEXORA Coding Agent.

Previous Code Memory:
{memory}

User query:
{query}

Give clean technical solution.
"""


    response = groq_chat(prompt)


    save_memory(
        "Code",
        query
    )


    return response