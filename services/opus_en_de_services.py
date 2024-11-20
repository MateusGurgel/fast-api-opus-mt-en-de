from langchain_huggingface import HuggingFacePipeline

class OpusEnDeServices:
    @staticmethod
    def translate(english_text: str) -> str:

        llm = HuggingFacePipeline.from_model_id(
            model_id="Helsinki-NLP/opus-mt-en-de",
            task="translation",
        )

        return llm.invoke(english_text)


