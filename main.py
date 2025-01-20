from core.rag.extractor.unstructured.ppt_extractor import UnstructuredPPTExtractor
from core.rag.extractor.unstructured.pptx_extractor import UnstructuredPPTXExtractor
from core.rag.extractor.common.pdf_extractor import PdfExtractor
import logging

logger = logging.getLogger(__name__)


if __name__ == "__main__":
    logging.basicConfig(
        level="INFO",
        format="%(asctime)s.%(msecs)03d %(levelname)s [%(threadName)s] [%(filename)s:%(lineno)d] - %(message)s",
        handlers=None,
        force=True,
    )

    a = UnstructuredPPTXExtractor(
        file_path="/Users/max/unstructured-api/sample-docs/fake-power-point.pptx", api_key="", api_url="localhost:8000").extract()

    for doc in a:
        logger.info("=======")
        logger.info(doc)
