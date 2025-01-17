from core.rag.extractor.unstructured.pdf_extractor import UnstructuredPdfExtractor
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

    # a = PdfExtractor(
    #     file_path="/Users/max/unstructured-api/sample-docs/layout-parser-paper.pdf").extract()
