"""
配置文件
"""
import os
from dotenv import load_dotenv

load_dotenv()


class Settings():
    # LLM相关配置
    # Qwen
    qwen_llm_api_endpoint = os.getenv("QWEN_BASE_URL")
    qwen_llm_api_key = os.getenv("QWEN_API_KEY")
    qwen_llm_model_name = os.getenv("QWEN_MODEL_NAME")
    # AZ Claude
    claude_llm_api_endpoint = os.getenv("CLAUDE_BASE_URL")
    claude_llm_api_key = os.getenv("CLAUDE_API_KEY")
    claude_llm_model_name = os.getenv("CLAUDE_MODEL_NAME")
    # New API GPT
    gpt_llm_api_endpoint = os.getenv("NEW_API_BASE_URL")
    gpt_llm_api_key = os.getenv("NEW_API_API_KEY")
    gpt_llm_model_name = os.getenv("NEW_API_MODEL_NAME")

    # 文档解析服务配置
    doc_parser_url = os.getenv("DOCUMENT_PARSER_URL")

    # 知识图谱的相关Protocol章节内容召回接口
    related_toc_info_url = os.getenv("KG_RELATED_TOC_INFO_URL")
    # 知识图谱的获取研究流程图/研究日程表接口
    kg_study_flow_url = os.getenv("KG_STUDY_FLOW_URL")



    @staticmethod
    def get_project_root(marker="README.md"):
        """
        通过README.md标记获取项目的绝对路径。
        注意：该仓库中只能有一个名为“README.md”的文件，且放在项目根目录下

        :param marker: 项目根目录的标记文件，默认为README.md
        :return: 项目根目录的绝对路径，如果找不到则返回None
        """
        # 从当前文件开始向上搜索
        path = os.path.abspath(os.path.dirname(__file__))

        while path != os.path.dirname(path):  # 直到到达根目录
            if os.path.exists(os.path.join(path, marker)):
                return path
            path = os.path.dirname(path)

        # 如果没有找到，返回None
        return None


# 实例化Settings
settings = Settings()
