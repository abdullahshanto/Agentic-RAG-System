from typing import List, Literal
from typing_extensions import TypedDict
from pydantic import BaseModel, Field
from langchain_core.documents import Document


class RouteDecision(BaseModel):
    route: Literal["kb", "direct"] = Field(
        description="kb for IT/support questions; direct for greetings/simple chat"
    )


class EvidenceGrade(BaseModel):
    grade: Literal["good", "weak"] = Field(
        description="Whether evidence is sufficient to answer"
    )


class AgentState(TypedDict):
    question: str
    current_query: str
    kb_docs: List[Document]
    web_results: str
    kb_grade: str
    web_grade: str
    answer: str
    source_used: str
    retry_count: int
    trace: List[str]
    citations: List[dict]


class ChatRequest(BaseModel):
    question: str = Field(min_length=2, max_length=3000)


class ChatResponse(BaseModel):
    answer: str
    source_used: str
    trace: List[str]
    citations: List[dict]
    rewritten_query: str


class IngestResponse(BaseModel):
    message: str
    file: str
    chunks: int
    ids_created: int