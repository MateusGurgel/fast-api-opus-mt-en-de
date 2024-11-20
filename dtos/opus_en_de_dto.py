from pydantic import BaseModel

class TranslationRequest(BaseModel):
    english_text: str

class TranslationResponse(BaseModel):
    deutsch_translation: str