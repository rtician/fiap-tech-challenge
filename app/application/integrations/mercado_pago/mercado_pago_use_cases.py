import hashlib
import hmac

import requests

from app import config
from app.application.exceptions import QRCodeGenerationError
from app.domain.entities.order import PaymentStatus
from app.domain.entities.order import QRCodeRequest


class MercadoPagoUseCases:
    POS_URL = "https://api.mercadopago.com/pos"

    def _headers(self):
        return {
            "Authorization": f"Bearer {config.MERCADO_PAGO_ACCESS_TOKEN}",
            "Content-Type": "application/json",
        }

    def verify_signature(self, secret: str, received_signature: str, request_body: str) -> bool:
        computed_signature = hmac.new(
            key=secret.encode("utf-8"), msg=request_body, digestmod=hashlib.sha256
        ).hexdigest()
        return hmac.compare_digest(received_signature, computed_signature)

    def get_external_id(self, payload: dict) -> str:
        return payload.get("metadata", {}).get("external_id") or payload.get("order", {}).get(
            "external_reference"
        )

    def generate_qrcode(self, qr_request: QRCodeRequest) -> str:
        try:
            payload = {
                "name": qr_request.description,
                "fixed_amount": True,
                "external_id": qr_request.order_id,
                "qr_code": {"type": "dynamic", "amount": qr_request.amount},
            }

            response = requests.post(self.POS_URL, json=payload, headers=self._headers())
            response.raise_for_status()

            return response.json()
        except Exception as e:
            raise QRCodeGenerationError() from e

    def get_payment_status(self, payload: dict) -> PaymentStatus:
        url = payload.get("resource")
        response = requests.get(url, headers=self._headers())
        response.raise_for_status()

        try:
            status = response.json()["status"].title()
            return PaymentStatus(status)
        except (KeyError, TypeError):
            return PaymentStatus.UNKNOWN
