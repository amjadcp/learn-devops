import pytest
from unittest.mock import patch
from fastapi.testclient import TestClient
from server import app, VoteRequest, candidates_collection

# Create a TestClient for the FastAPI app
client = TestClient(app)

# Mock data for testing
mock_candidates = [
    {"_id": "123456789012345678901234567890", "votes": 100, "candidate": "Raju", "ID": "A"},
    {"_id": "98765432109876543210987654321", "votes": 50, "candidate": "Radha", "ID": "B"},
]

# Mocking MongoDB collection methods
@pytest.fixture(autouse=True)
def mock_db():
    with patch('server.candidates_collection.find') as mock_find:
        # Return an iterator of mock candidates
        mock_find.return_value = iter(mock_candidates)  
        yield  # This will run the tests using the mocked collection

@pytest.fixture
def vote_request():
    return VoteRequest(ID='A')

def test_vote_success(vote_request):
    # Mocking the update operation
    with patch('server.candidates_collection.find_one_and_update') as mock_update:
        mock_update.return_value = {"candidate": "Raju", "votes": 6}  # Simulate updated candidate
        
        response = client.post("/vote", json=vote_request.dict())
        
        assert response.status_code == 200
        assert response.json() == {'success': True, 'candidate': 'Raju'}
