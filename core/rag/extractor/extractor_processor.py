

from typing import Optional, Union
from pathlib import Path
import tempfile

from config import lune_config
from infrastructure.storage import storage
from domain.rag.entity import document, extract_setting, datasource_type
from core.rag.extractor.unstructured import UnstructuredPPTExtractor, UnstructuredPPTXExtractor, UnstructuredEpubExtractor, UnstructuredTextExtractor, UnstructuredMsgExtractor, UnstructuredXMLExtractor, UnstructuredMDExtractor, UnstructuredEmlExtractor
from core.rag.extractor.common import PdfExtractor, CSVExtractor, ExcelExtractor, MarkdownExtractor, HtmlExtractor, WordExtractor, TextExtractor


class ExtractProcessor:

    @classmethod
    def load_from_upload_file(
        cls, upload_file: extract_setting.UploadInfo, return_text: bool = False, is_automatic: bool = False
    ) -> Union[list[document.Document], str]:
        extract_setting = extract_setting.ExtractSetting(
            datasource_type="upload_file", upload_info=upload_file
        )
        if return_text:
            delimiter = "\n"
            return delimiter.join([document.page_content for document in cls.extract(extract_setting, is_automatic)])
        else:
            return cls.extract(extract_setting, is_automatic)

    @classmethod
    def extract(cls, extract_setting: extract_setting.ExtractSetting, is_automatic: bool = False, file_path: Optional[str] = None) -> list[document.Document]:
        if extract_setting.datasource_type == datasource_type.DatasourceType.FILE.value:
            with tempfile.TemporaryDirectory() as temp_dir:
                if not file_path:
                    suffix = Path(extract_setting.upload_info.key).suffix
                    file_path = f"{temp_dir}/{next(tempfile._get_candidate_names())}{suffix}"
                    storage.download(
                        extract_setting.upload_info.key, file_path)
                input_file = Path(file_path)
                file_extension = input_file.suffix.lower()
                etl_type = lune_config.ETL_TYPE
                unstructured_api_url = lune_config.UNSTRUCTURED_API_URL
                unstructured_api_key = lune_config.UNSTRUCTURED_API_KEY

                if etl_type == "Unstructured":
                    if file_extension in {".xlsx", ".xls"}:
                        extractor = ExcelExtractor(file_path)
                    elif file_extension == ".pdf":
                        extractor = PdfExtractor(file_path)
                    elif file_extension in {".md", ".markdown"}:
                        extractor = (
                            UnstructuredMDExtractor(
                                file_path, unstructured_api_url, unstructured_api_key)
                            if is_automatic
                            else MarkdownExtractor(file_path, autodetect_encoding=True)
                        )
                    elif file_extension in {".htm", ".html"}:
                        extractor = HtmlExtractor(file_path)
                    elif file_extension == ".docx":
                        extractor = WordExtractor(
                            file_path, extract_setting.upload_info.tenant_id, extract_setting.upload_info.created_by)
                    elif file_extension == ".csv":
                        extractor = CSVExtractor(
                            file_path, autodetect_encoding=True)
                    elif file_extension == ".msg":
                        extractor = UnstructuredMsgExtractor(
                            file_path, unstructured_api_url, unstructured_api_key)
                    elif file_extension == ".eml":
                        extractor = UnstructuredEmlExtractor(
                            file_path, unstructured_api_url, unstructured_api_key)
                    elif file_extension == ".ppt":
                        extractor = UnstructuredPPTExtractor(
                            file_path, unstructured_api_url, unstructured_api_key)
                    elif file_extension == ".pptx":
                        extractor = UnstructuredPPTXExtractor(
                            file_path, unstructured_api_url, unstructured_api_key)
                    elif file_extension == ".xml":
                        extractor = UnstructuredXMLExtractor(
                            file_path, unstructured_api_url, unstructured_api_key)
                    elif file_extension == ".epub":
                        extractor = UnstructuredEpubExtractor(
                            file_path, unstructured_api_url, unstructured_api_key)
                    else:
                        # txt
                        extractor = (
                            UnstructuredTextExtractor(
                                file_path, unstructured_api_url)
                            if is_automatic
                            else TextExtractor(file_path, autodetect_encoding=True)
                        )
                else:
                    if file_extension in {".xlsx", ".xls"}:
                        extractor = ExcelExtractor(file_path)
                    elif file_extension == ".pdf":
                        extractor = PdfExtractor(file_path)
                    elif file_extension in {".md", ".markdown"}:
                        extractor = MarkdownExtractor(
                            file_path, autodetect_encoding=True)
                    elif file_extension in {".htm", ".html"}:
                        extractor = HtmlExtractor(file_path)
                    elif file_extension == ".docx":
                        extractor = WordExtractor(
                            file_path, extract_setting.upload_info.tenant_id, extract_setting.upload_info.created_by)
                    elif file_extension == ".csv":
                        extractor = CSVExtractor(
                            file_path, autodetect_encoding=True)
                    elif file_extension == ".epub":
                        extractor = UnstructuredEpubExtractor(file_path)
                    else:
                        # txt
                        extractor = TextExtractor(
                            file_path, autodetect_encoding=True)
                return extractor.extract()
