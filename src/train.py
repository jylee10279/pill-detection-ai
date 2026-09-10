"""학습 실행 스크립트.

사용 예:
    python src/train.py --config configs/default.yaml
"""

import argparse

from dataset import PillDataset
from model import build_model
from utils import load_config, set_seed


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", type=str, default="configs/default.yaml")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    config = load_config(args.config)
    set_seed(config["train"]["seed"])

    # TODO: PillDataset으로 train/val DataLoader 구성
    # TODO: build_model(config)로 모델 생성
    # TODO: 학습 루프 작성, config["output"]["dir"]/config["output"]["experiment_name"] 아래에 체크포인트 저장
    raise NotImplementedError("학습 루프를 구현해주세요.")


if __name__ == "__main__":
    main()
