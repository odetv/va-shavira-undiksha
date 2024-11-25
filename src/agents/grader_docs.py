from langchain_core.messages import HumanMessage, SystemMessage
from utils.agent_state import AgentState
from utils.llm import chat_llm
from utils.debug_time import time_check


class GraderDocsAgent:
    @time_check
    @staticmethod
    def graderDocsAgent(state: AgentState):
        info = "\n--- Grader Documents ---"
        print(info)

        prompt = f"""
        Anda adalah seorang pemilih konteks handal.
        - Ambil informasi yang hanya berkaitan dengan pertanyaan.
        - Pastikan informasi yang diambil lengkap sesuai konteks yang diberikan.
        - Jangan mengurangi atau melebihi konteks yang diberikan.
        - Format nya gunakan sesuai format konteks yang dberikan, jangan dirubah.
        - Jangan jawab pertanyaan pengguna, hanya pilah konteks yang berkaitan dengan pertanyaan saja.
        Konteks: {state["generalContext"]}
        """

        messages = [
            SystemMessage(content=prompt),
            HumanMessage(content=state["generalQuestion"]),
        ]
        responseGraderDocsAgent = chat_llm(messages)

        state["generalGraderDocs"] = responseGraderDocsAgent
        state["finishedAgents"].add("graderDocs_agent")
        print("DEBUG:GENERALGRADER:::", state["generalGraderDocs"])
        return {"generalGraderDocs": state["generalGraderDocs"]}


