import os
from dotenv import load_dotenv

from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import DashScopeEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import (
    PyPDFLoader,
    Docx2txtLoader,
    TextLoader,
    UnstructuredMarkdownLoader
)
load_dotenv()

print(os.getenv("api_key"))
# 初始化嵌入模型
embeddings = DashScopeEmbeddings(
    model="text-embedding-v1",
    dashscope_api_key=os.getenv("api_key")

)


def load_document(file_path):
    """根据文件类型加载文档"""
    # 标准化文件路径
    file_path = os.path.normpath(file_path)

    if not os.path.exists(file_path):
        raise FileNotFoundError(f"文件不存在: {file_path}")

    file_ext = os.path.splitext(file_path)[1].lower()

    try:
        if file_ext == ".pdf":
            loader = PyPDFLoader(file_path)
        elif file_ext == ".docx":
            loader = Docx2txtLoader(file_path)
        elif file_ext == ".txt":
            # 显式指定UTF-8编码处理中文文本
            loader = TextLoader(file_path, encoding='utf-8')
        elif file_ext == ".md":
            loader = UnstructuredMarkdownLoader(file_path)
        else:
            raise ValueError(f"不支持的文件类型: {file_ext}")

        return loader.load()
    except Exception as e:
        raise Exception(f"加载文档失败: {str(e)}")


def process_document(file_path, user_id):
    """处理文档并存入向量数据库"""
    try:
        # 加载文档
        documents = load_document(file_path)
        print(f"成功加载文档，共 {len(documents)} 页/部分")

        # 分割文本
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200
        )
        splits = text_splitter.split_documents(documents)
        print(f"分割为 {len(splits)} 个块")

        # 创建向量存储目录
        vectorstore_path = os.path.join("data/vectorstore", str(user_id))
        os.makedirs(vectorstore_path, exist_ok=True)

        # 创建向量存储
        vectorstore = Chroma.from_documents(
            documents=splits,
            embedding=embeddings,
            persist_directory=vectorstore_path
        )

        vectorstore.persist()
        print(f"向量存储已保存到 {vectorstore_path}")

        return True
    except Exception as e:
        print(f"文档处理错误: {str(e)}")
        return False


def get_vectorstore(user_id):
    """获取用户的向量存储"""
    vectorstore_path = os.path.join("data/vectorstore", str(user_id))
    if not os.path.exists(vectorstore_path):
        return None

    return Chroma(
        persist_directory=vectorstore_path,
        embedding_function=embeddings
    )


def search_documents(user_id, query, k=3):
    """在用户文档中搜索相关内容"""
    vectorstore = get_vectorstore(user_id)
    if vectorstore is None:
        return []

    return vectorstore.similarity_search(query, k=k)

def hcy_search(path, query, k=3):
    
    if not os.path.exists(path):
        return "向量数据库不存在"
    vectorstore = Chroma(
        persist_directory=vectorstore_path,
        embedding_function=embeddings
    )
    if vectorstore is None:
        return []

    return vectorstore.similarity_search(query, k=k)

def main():
    #写入向量，跑一次就行了
    process_document(r"C:\jyproject\CRM\1\测试数据.txt", 1)
    #查询
    print(search_documents(1, "于跃那一年出生？", 3))

if __name__ == "__main__":
    main()