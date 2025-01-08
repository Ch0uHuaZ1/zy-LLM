import llama_index
from RAG import basic_rag
from model import load_chatglm_model,generate_response_from_model

def run():
    """
    命令行对话功能
    """
    print("欢迎使用易经问答系统！输入 '退出' 或 'exit' 结束对话。")
    while True:
        # 获取用户输入
        query = input("\n请输入问题: ").strip()
        
        # 退出条件
        if query.lower() in ["退出", "exit"]:
            print("对话结束，再见！")
            break
        
        # 调用 RAG 生成回答
        response = basic_rag(query)
        
        # 输出回答
        print(f"\n回答: {response}")

if __name__ == "__main__":
    run()

