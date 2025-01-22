
import logging
from v1.grpc.extractor import extractor_pb2_grpc
from v1.grpc.extractor.extractor_pb2 import ExtractorReply, ExtractorRequest, DocumentReply
from domain.rag.entity.extract_setting import ExtractSetting
from core.rag.extractor.extractor_processor import ExtractProcessor

logger = logging.getLogger(__name__)


class ExtractorService(extractor_pb2_grpc.ExtractorServicer):
    def extract(self, request: ExtractorRequest, context):
        try:
            setting = ExtractSetting(upload_info=request.upload_info,
                                     datasource_type=request.datasource_type,
                                     document_model=request.document_model)
            docs = ExtractProcessor.extract(
                setting, request.process_rule_mode == "automatic")

            docs_reply = [DocumentReply(
                page_content=document.page_content, meta_data=document.metadata) for document in docs]

            return ExtractorReply(code=0, msg="", documents=docs_reply)
        except Exception as e:
            logger.error(f"extractor process error: {e}")
            return ExtractorReply(code=500, msg="internal error", documents=[])
