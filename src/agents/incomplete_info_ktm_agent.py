from utils.agent_state import AgentState
from utils.debug_time import time_check


class IncompleteInfoKTMAgent:
    @time_check
    @staticmethod
    def incompleteInfoKTMAgent(state: AgentState):
        info = "\n--- Incomplete Info KTM ---"
        print(info)

        response = """
            Untuk melihat KTM dapat melalui SSO Undiksha atau langsung dari pesan ini saya dapat membantu anda, namun diperlukan mengirimkan NIM (Nomor Induk Mahasiswa) yang valid.
            NIM (Nomor Induk Mahasiswa) yang valid dari Undiksha berjumlah 10 digit angka.
            - Format penulisan pesan:
                KTM [NIM]
            - Contoh penulisan pesan:
                KTM 1234567890
        """

        agentOpinion = {
            "answer": response
        }

        state["finishedAgents"].add("incompleteInfoKTM_agent")
        state["responseIncompleteNim"] = response
        return {"answerAgents": [agentOpinion]}
