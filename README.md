# Claude 3.5 Sonnet Bedrock API Call 샘플소스

AWS Bedrock을 통해 Claude 3 Sonnet을 호출하는 Python 유틸리티입니다. 이 도구는 마크다운 형식의 응답을 생성합니다.

## 사전 요구사항

- Python 3.6 이상
- AWS 계정 및 적절한 권한
- 필요한 Python 패키지:
  - boto3
  - json
  - typing

## 설치 방법

1. 필요한 패키지 설치:
```bash
pip install boto3
```

2. AWS 자격 증명 설정:
   - AWS CLI 구성
   - 또는 환경 변수 설정
   ```bash
   export AWS_ACCESS_KEY_ID='your_access_key'
   export AWS_SECRET_ACCESS_KEY='your_secret_key'
   ```

## 사용 방법

### 기본 사용법

```python
from claude_bedrock import invoke_claude

# 단순 질의
response = invoke_claude(query="당신의 질문을 여기에 입력하세요")

# 컨텍스트와 함께 질의
contexts = [
    "참고할 첫 번째 컨텍스트",
    "참고할 두 번째 컨텍스트"
]
response = invoke_claude(query="질문", contexts=contexts)
```

### 실행 예시

```python
payload = {
    "query": "고대 그리스 철학의 주요 사상가들과 그들의 핵심 아이디어를 설명해주세요.",
    "contexts": [
        "철학은 인간의 지식과 이해를 넓히는 학문입니다.",
        "고대 그리스는 서양 철학의 발상지로 알려져 있습니다."
    ]
}

response = invoke_claude(
    query=payload["query"],
    contexts=payload["contexts"]
)
```

## 주요 기능

- Claude 3 Sonnet 모델 호출
- 컨텍스트 기반 질의 지원
- 마크다운 형식의 응답 생성
- 에러 처리 및 로깅

## 파라미터 설정

- `max_tokens`: 4096 (최대 토큰 수)
- `temperature`: 0 (응답의 창의성 수준, 0은 가장 결정적)
- `top_k`: 1
- `top_p`: 1

## 에러 처리

함수는 예외 발생 시 None을 반환하며, 에러 메시지를 콘솔에 출력합니다.

## 주의사항

- AWS Bedrock 서비스 사용 요금이 발생할 수 있습니다.
- 적절한 IAM 권한이 필요합니다.
- 리전이 'us-east-1'로 설정되어 있습니다. 필요시 변경하세요.

<img width="765" alt="image" src="https://github.com/user-attachments/assets/f1f28e94-5a15-4f03-90af-38043dca9dfb">

