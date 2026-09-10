"""알약 검출용 PyTorch Dataset."""

from torch.utils.data import Dataset


class PillDataset(Dataset):
    """이미지와 (클래스, bbox) 라벨을 반환하는 Dataset.

    한 이미지에 최대 4개의 알약이 있으므로, 이미지당 최대 4개의
    (label, bbox) 쌍을 반환하도록 구현한다.
    """

    def __init__(self, data_dir: str, transform=None):
        self.data_dir = data_dir
        self.transform = transform
        # TODO: data_dir 안의 이미지·라벨 목록 로드

    def __len__(self) -> int:
        raise NotImplementedError

    def __getitem__(self, index: int):
        raise NotImplementedError
