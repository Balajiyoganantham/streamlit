from langchain_community.embeddings import HuggingFaceEmbeddings
import logging
from .config import EMBEDDING_MODEL_NAME

logger = logging.getLogger(__name__)

def get_embeddings():
    try:
        # Try with explicit device configuration
        return HuggingFaceEmbeddings(
            model_name=EMBEDDING_MODEL_NAME,
            model_kwargs={'device': 'cpu', 'trust_remote_code': True},
            encode_kwargs={'normalize_embeddings': True}
        )
    except Exception as e:
        logger.warning(f"Failed to load {EMBEDDING_MODEL_NAME}, using fallback: {e}")
        try:
            # Use a more stable fallback model
            return HuggingFaceEmbeddings(
                model_name="sentence-transformers/all-MiniLM-L6-v2",
                model_kwargs={'device': 'cpu', 'trust_remote_code': True},
                encode_kwargs={'normalize_embeddings': True}
            )
        except Exception as e2:
            logger.error(f"Fallback model also failed: {e2}")
            # Use the most basic model as last resort
            return HuggingFaceEmbeddings(
                model_name="sentence-transformers/paraphrase-MiniLM-L3-v2",
                model_kwargs={'device': 'cpu'},
                encode_kwargs={'normalize_embeddings': True}
            ) 