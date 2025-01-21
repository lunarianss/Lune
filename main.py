import v1.grpc.extractor_pb2_grpc as extractor_pb2_grpc
import v1.grpc.extractor_pb2 as extractor_pb2
import grpc
import app_factory
from core.rag.extractor.unstructured.ppt_extractor import UnstructuredPPTExtractor
from core.rag.extractor.unstructured.pptx_extractor import UnstructuredPPTXExtractor
from core.rag.extractor.common.pdf_extractor import PdfExtractor
from core.rag.extractor.unstructured.xml_extractor import UnstructuredXMLExtractor
from core.rag.extractor.unstructured.md_extractor import UnstructuredMDExtractor
from core.rag.extractor.unstructured.doc_extractor import UnstructuredDocExtractor
from core.rag.extractor.unstructured.epub_extractor import UnstructuredEpubExtractor
from core.rag.extractor.unstructured.text_extractor import UnstructuredTextExtractor
from core.rag.extractor.unstructured.msg_extractor import UnstructuredMsgExtractor
from core.rag.extractor.unstructured.eml_extractor import UnstructuredEmlExtractor
from core.rag.extractor.unstructured.csv_extractor import UnstructuredCsvExtractor
from core.rag.extractor.unstructured.excel_extractor import UnstructuredExcelExtractor
from core.rag.extractor.common.csv_extractor import CSVExtractor
from core.rag.extractor.common.excel_extractor import ExcelExtractor
from core.rag.extractor.common.markdown_extractor import MarkdownExtractor
# from core.rag.extractor.common.html_extractor import HtmlExtractor
from core.rag.extractor.unstructured.html_extractor import UnstructuredHTMLExtractor
from core.rag.extractor.common.word_extractor import WordExtractor
import logging
import pandas as pd
logger = logging.getLogger(__name__)


def create_app():
    app_factory.init_storage()
    app_factory.init_database()


if __name__ == "__main__":
    logging.basicConfig(
        level="INFO",
        format="%(asctime)s.%(msecs)03d %(levelname)s [%(threadName)s] [%(filename)s:%(lineno)d] - %(message)s",
        handlers=None,
        force=True,
    )

    create_app()

    a = WordExtractor(
        file_path="/Users/max/unstructured-api/sample-docs/fake.docx", tenant_id="123456789", user_id="").extract()

    for doc in a:
        logger.info("=======")
        logger.info(doc)
