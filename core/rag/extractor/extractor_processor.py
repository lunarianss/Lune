
from domain.rag.entity import document, extract_setting, datasource_type
from typing import Optional


class ExtractProcessor:
    @classmethod
    def extract(cls, extract_setting: extract_setting.ExtractSetting, is_automatic: bool = False, file_path: Optional[str] = None) -> list[document.Document]:
        if extract_setting.datasource_type == datasource_type.DatasourceType.FILE.value:
            pass
