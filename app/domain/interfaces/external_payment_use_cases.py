from abc import ABC
from abc import abstractmethod

from app.domain.entities.order import PaymentStatus
from app.domain.entities.order import QRCodeRequest


class ExternalPaymentUseCases(ABC):
    @abstractmethod
    def generate_qrcode(self, qr_request: QRCodeRequest) -> str:
        pass

    @abstractmethod
    def get_payment_status(self, payload: dict) -> PaymentStatus:
        pass
