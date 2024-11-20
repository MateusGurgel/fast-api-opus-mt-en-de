from fastapi import APIRouter
from dtos.opus_en_de_dto import TranslationRequest, TranslationResponse
from services.opus_en_de_services import OpusEnDeServices

opus_en_de_router = APIRouter()


@opus_en_de_router.post("/")
def translate(question: TranslationRequest) -> TranslationResponse:
    translation = OpusEnDeServices.translate(question.english_text)
    return {"deutsch_translation": translation}