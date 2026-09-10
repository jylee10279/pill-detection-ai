# data/

이 폴더의 실제 데이터 파일은 git에 커밋하지 않는다 (`.gitignore` 처리됨).

- `raw/` — Kaggle에서 받은 원본 이미지·라벨을 그대로 넣는 곳.
- `processed/` — `raw/`를 전처리하거나 포맷을 변환(예: 라벨을 YOLO 포맷 ↔ COCO 포맷으로 변환)한 결과를 저장하는 곳.

## 데이터 다운로드 (Kaggle)

### 1. Kaggle 인증 (최초 1회만, 팀원별로 한 번)

[kaggle.com](https://www.kaggle.com) → **Settings** → **API** → **Create New Token** 클릭하면 `kaggle.json` 파일이 다운로드된다. 이 파일을 아래 경로에 저장한다.

```bash
mkdir -p ~/.kaggle
mv ~/Downloads/kaggle.json ~/.kaggle/kaggle.json
chmod 600 ~/.kaggle/kaggle.json
```

> `kaggle.json`은 개인 인증 정보이니 **절대 git에 커밋하지 않는다.**

이 파일이 있으면 `kagglehub`가 자동으로 인증에 사용하므로, 이후에는 매번 로그인할 필요가 없다.

### 2. 다운로드 실행

```bash
python src/download_data.py
```

Kaggle 대회(`ai14-level-project`) 데이터를 받아서 `data/raw/`로 옮겨준다.
