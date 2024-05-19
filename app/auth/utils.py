# utils.py
import requests

import jwt
from typing import Any, Dict, Optional, Tuple
import secrets
import hashlib
import base64

from flask import  current_app
from typing import Optional
import logging

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
    def generate_code_verifier_and_code_challenge() -> Tuple[str, str]:
        # Generate a secure random code verifier
        code_verifier: str = secrets.token_urlsafe(128)  # Recommended by RFC 7636

        # Hash the code verifier using SHA256
        hashed_code_verifier: bytes = hashlib.sha256(code_verifier.encode('utf-8')).digest()

        # Base64 URL-encode the hash without padding
        code_challenge: str = base64.urlsafe_b64encode(hashed_code_verifier).decode('utf-8').rstrip('=')
        
        return code_verifier, code_challenge
    
    @staticmethod
    def generate_auth_uri(challenge: str) -> Optional[str]:
        try:
            auth = current_app.auth_base
            uri = auth.sdk.get_auth_link(redirect_uri='http://127.0.0.1:5000/auth/callback')
            uri += f"&code_challenge_method=S256&code_challenge={challenge}"
            logging.info("URI: %s", uri)
            return uri
        except Exception as e:
            logging.error("An error occurred while generating the auth URI: %s", e)
            return {"error": "An error occurred"}
        
    @staticmethod
    def generate_payload(code_value: str, verifier: str) -> Dict[str, str]:
        """
        Generate the payload for an access token request.

        Parameters:
        - code_value (str): The authorization code received from the authorization server.
        - verifier (str): The code verifier for PKCE.

        Returns:
        - Dict[str, str]: The payload dictionary for the access token request.
        """
        try:
            auth = current_app.auth_base
            # Presuming sdk._get_payload_for_access_token_request() is a method that creates the payload
            payload = auth.sdk._get_payload_for_access_token_request(code=code_value)
            del payload['client_secret']
            # Uncomment the next line if you need to set the redirect_uri in the payload
            # payload['redirect_uri'] = "http://localhost:5000/callback"    
            payload['code_verifier'] = verifier

            logging.info('Payload generated successfully: %s', payload)
            return payload
        except Exception as e:
            logging.error('Error while generating payload: %s', e)
            raise