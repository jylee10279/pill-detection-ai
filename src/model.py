"""모델 생성 코드.

팀에서 프레임워크(Ultralytics YOLO / torchvision 등)를 결정하면
build_model()의 분기 로직만 채우면 된다. train.py, predict.py는
이 함수를 통해서만 모델을 가져오므로 다른 파일은 수정할 필요가 없다.
"""


def build_model(config: dict):
    """config["model"]["name"] 값에 따라 모델을 생성해서 반환한다."""
    model_name = config["model"]["name"]

    if model_name is None:
        raise ValueError(
            "config['model']['name']이 설정되지 않았습니다. "
            "팀에서 사용할 모델을 정한 뒤 configs/*.yaml에 채워주세요."
        )

    # TODO: 예시
    # if model_name.startswith("yolo"):
    #     from ultralytics import YOLO
    #     return YOLO(f"{model_name}.pt")
    # else:
    #     import torchvision
    #     return torchvision.models.detection.__dict__[model_name](
    #         pretrained=config["model"]["pretrained"]
    #     )

    raise NotImplementedError(f"지원하지 않는 model.name입니다: {model_name}")
