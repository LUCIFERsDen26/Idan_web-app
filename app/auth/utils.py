# utils.py
import requests
import secrets
import jwt
from typing import Any, Dict, Optional


class Utils:
    @staticmethod
    def fetch_url_data(uri: str) -> Dict[str, Any]:
        response = requests.get(uri, verify=False)  # Not recommended for production
        data = response.json()
        return data

    @staticmethod
    def get_decoded_token(access_token: str, jwks_data: Dict[str, Any], signing_algos: list, client_id: str) -> Dict[str, Any]:
        decoded_token = jwt.api_jwt.decode_complete(
            access_token,
            key=(jwks_data['keys'][0]['kid']),
            algorithms=signing_algos,
            audience=client_id,
            options={"verify_signature": False}
        )
        return decoded_token

    @staticmethod
    def generate_code_verifier(length: int) -> str:
        characters = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        result = ''.join(secrets.choice(characters) for _ in range(length))
        return result

    @staticmethod
    def get_user_info(access_token: str, userinfo_endpoint: str) -> Optional[Dict[str, Any]]:
        try:
            headers = {"Authorization": f"Bearer {access_token}"}
            response = requests.get(userinfo_endpoint, headers=headers, verify=False)  # Not recommended for production
            response.raise_for_status()
            user_info = response.json()
            return user_info
        except requests.exceptions.RequestException as e:
            print(f"Error retrieving user information: {e}")
            return None