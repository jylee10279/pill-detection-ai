"""학습된 모델로 추론하는 스크립트.

사용 예:
    python src/predict.py --config configs/default.yaml --checkpoint outputs/default/checkpoints/best.pt --image path/to/image.jpg
"""

import argparse

from model import build_model
from utils import load_config


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", type=str, default="configs/default.yaml")
    parser.add_argument("--checkpoint", type=str, required=True)
    parser.add_argument("--image", type=str, required=True)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    config = load_config(args.config)
    model = build_model(config)

    # TODO: checkpoint 로드, 이미지 전처리, 추론 후 클래스+bbox 출력
    raise NotImplementedError("추론 로직을 구현해주세요.")


if __name__ == "__main__":
    main()
