import boto3
import json
from typing import List, Optional

def invoke_claude(query: str, contexts: Optional[List[str]] = None) -> str:
    """
    Claude 3 Sonnet을 호출하여 마크다운 형식의 응답을 받습니다.
    
    Args:
        query (str): 사용자의 질문
        contexts (List[str], optional): 추가적인 컨텍스트 정보
    
    Returns:
        str: 마크다운 형식의 응답
    """
    # Bedrock 클라이언트 생성
    session = boto3.Session()
    bedrock_runtime = session.client(
        service_name="bedrock-runtime",
        region_name="us-east-1"
    )
    
    # 컨텍스트가 있는 경우 프롬프트에 추가
    prompt = ""
    if contexts:
        prompt += "다음은 참고할 컨텍스트 정보입니다:\n"
        for i, context in enumerate(contexts, 1):
            prompt += f"{i}. {context}\n"
        prompt += "\n위 컨텍스트를 참고하여 다음 질문에 답변해주세요:\n"
    
    prompt += query
    prompt += "\n\n마크다운 형식으로 답변해주세요."
    
    # 모델 파라미터 설정
    body = {
        "anthropic_version": "bedrock-2023-05-31",
        "max_tokens": 4096,
        "temperature": 0,
        "top_k": 1,
        "top_p": 1,
        "messages": [{"role": "user", "content": prompt}]
    }
    
    try:
        # Claude 3.5 Sonnet 호출
        response = bedrock_runtime.invoke_model(
            modelId="anthropic.claude-3-5-sonnet-20240620-v1:0",
            body=json.dumps(body)
        )
        
        # 응답 처리
        response_body = json.loads(response.get("body").read())
        return response_body["content"][0]["text"]
        
    except Exception as e:
        print(f"Error invoking Claude: {str(e)}")
        return None

# 사용 예시
# python3 claude_call_test.py
if __name__ == "__main__":
    payload = {
        "query": "고대 그리스 철학의 주요 사상가들과 그들의 핵심 아이디어를 간단히 설명해주세요. 마크다운 형식으로 답변해주세요.",
        "contexts": [
            "철학은 인간의 지식과 이해를 넓히는 학문입니다.", 
            "고대 그리스는 서양 철학의 발상지로 알려져 있습니다."
        ]
    }
    
    response = invoke_claude(
        query=payload["query"],
        contexts=payload["contexts"]
    )
    
    if response:
        print("Claude's response:")
        print(response)
