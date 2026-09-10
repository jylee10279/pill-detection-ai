"""Kaggle 대회 데이터를 받아서 data/raw/로 옮기는 스크립트.

사전 준비 (최초 1회만, 팀원별로 한 번):
    kaggle.com -> Settings -> API에서 "Create New Token"으로 kaggle.json을
    발급받아 ~/.kaggle/kaggle.json에 저장한다 (chmod 600 권장). 이 파일이
    있으면 kagglehub가 자동으로 인증에 사용하므로, 이 스크립트에서 매번
    로그인할 필요는 없다.

사용법:
    python src/download_data.py
"""

import shutil
from pathlib import Path

import kagglehub

COMPETITION = "ai14-level-project"
RAW_DIR = Path(__file__).resolve().parent.parent / "data" / "raw"
CREDENTIALS_PATH = Path.home() / ".kaggle" / "kaggle.json"


def main() -> None:
    if not CREDENTIALS_PATH.exists():
        raise SystemExit(
            f"{CREDENTIALS_PATH}가 없습니다. kaggle.com -> Settings -> API에서 "
            "kaggle.json을 발급받아 해당 경로에 저장해주세요."
        )

    downloaded_path = Path(kagglehub.competition_download(COMPETITION))

    RAW_DIR.mkdir(parents=True, exist_ok=True)
    for item in downloaded_path.iterdir():
        dest = RAW_DIR / item.name
        if dest.exists():
            shutil.rmtree(dest) if dest.is_dir() else dest.unlink()
        shutil.move(str(item), str(dest))

    print(f"데이터 준비 완료: {RAW_DIR}")


if __name__ == "__main__":
    main()
