from operator import add
from typing_extensions import TypedDict, Annotated, Sequence, Optional, Set


class AnswerState(TypedDict):
    question = None
    answer = None

class AgentState(TypedDict):
    context: str
    question: str
    question_type: str
    generalQuestion: str
    newsQuestion: str
    accountQuestion: str
    kelulusanQuestion: str
    ktmQuestion: str
    totalAgents: int
    finishedAgents: Set[str]
    generalContext: str
    generalGraderDocs: str
    checkKelulusan: str
    noPendaftaran: str
    tglLahirPendaftar: str
    checkKTM: str
    nimKTMMhs: str
    urlKTMMhs: str
    newsScrapper: str
    checkAccount: str
    emailAccountUser: Optional[str] = None
    loginAccountStatus : Optional[str] = None
    answerAgents : Annotated[Sequence[AnswerState], add]
    responseFinal: str
    isHallucination: str
    hallucinationCount: int