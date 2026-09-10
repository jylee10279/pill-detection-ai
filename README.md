# pill-detection-ai

사진 속 최대 4개 알약의 이름(클래스)과 위치(bounding box)를 검출하는 모델을 구현하고, 성능을 지속적으로 개선해나가는 팀 프로젝트입니다.

## 환경 설정

```bash
conda env create -f environment.yml
conda activate pill-detection
```

- `environment.yml`의 패키지 버전은 모두 고정되어 있습니다. 전원이 동일한 버전을 쓰기 위함이니 임의로 버전을 올리지 말고, 꼭 필요하면 `environment.yml`을 수정하는 PR을 올려서 팀 전체가 같은 시점에 업데이트하세요.
- 위 버전은 CPU/MPS(맥) 기준입니다. GPU 학습 서버에서는 동일한 PyTorch 버전(2.4.1)의 CUDA 빌드를 서버 CUDA 버전에 맞는 `pytorch-cuda` 채널 조합으로 다시 설치해야 합니다.

## 폴더 구조

| 경로 | 용도 |
|---|---|
| `configs/` | 학습에 쓸 설정값(모델 종류, 하이퍼파라미터 등)을 담은 yaml 파일. 실험마다 파일을 복사해서 사용 |
| `data/raw/` | 원본 이미지·라벨 데이터 (git에는 올리지 않음, 각자 로컬에 다운로드) |
| `data/processed/` | 전처리·포맷 변환된 데이터 |
| `notebooks/` | 데이터 탐색(EDA), 실험용 노트북. 자유롭게 사용하되 재사용 코드는 `src/`로 옮기기 |
| `src/download_data.py` | Kaggle 대회 데이터를 받아서 `data/raw/`로 옮기는 스크립트 |
| `src/dataset.py` | 이미지·라벨을 불러오는 PyTorch Dataset 클래스 |
| `src/model.py` | 모델을 생성하는 코드 (프레임워크가 정해지면 이 파일만 수정하면 됨) |
| `src/train.py` | 학습 실행 스크립트 |
| `src/predict.py` | 학습된 모델로 추론하는 스크립트 |
| `src/utils.py` | 여러 파일에서 공통으로 쓰는 함수 (seed 고정, config 로드 등) |
| `outputs/` | 학습 결과(체크포인트, 예측 결과). git에는 올리지 않음 |
| `.github/PULL_REQUEST_TEMPLATE.md` | PR 생성 시 자동으로 채워지는 템플릿 |

## 데이터 준비

```bash
python src/download_data.py
```

최초 1회는 Kaggle 토큰 발급이 필요하다. 자세한 내용은 `data/README.md` 참고.

## 실행 방법

```bash
# 학습
python src/train.py --config configs/default.yaml

# 추론
python src/predict.py --config configs/default.yaml --checkpoint outputs/default/checkpoints/best.pt --image path/to/image.jpg
```

## 새 실험 추가하기

1. `configs/default.yaml`을 복사해서 `configs/exp2.yaml` 처럼 이름을 바꾼다.
2. 모델 종류/하이퍼파라미터 값만 수정한다.
3. `python src/train.py --config configs/exp2.yaml`로 실행하면 `outputs/<experiment_name>/`에 결과가 저장된다.

## 협업 규칙

- **브랜치**: `main`은 항상 동작하는 상태로 유지. 작업은 `feature/작업내용` 브랜치에서 진행 후 PR로 머지.
- **PR**: `.github/PULL_REQUEST_TEMPLATE.md`가 자동으로 채워지니 항목을 채우고, 최소 1명 이상 리뷰 받은 뒤 머지.
- **노트북**: `notebooks/README.md`의 네이밍 규칙(`yyyymmdd_이름_주제.ipynb`)을 따른다.
- **모델/실험 관리 도구**: 아직 미정. 팀 논의 후 정해지면 이 섹션과 `src/model.py`, `src/utils.py`를 업데이트한다.
