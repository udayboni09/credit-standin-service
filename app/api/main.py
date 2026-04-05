

# Import FastAPI to create the API application
# FastAPI is a modern, fast web framework for building APIs in Python
from fastapi import FastAPI  # fastapi must be installed via pip

# Import the request and response models defined earlier
from app.api.models import ApplicationRequest, DecisionResponse  # local imports from your project

# Import the decision service which orchestrates rule engine + rule loader
from app.services.decision_service import process_application  # local business logic


# Create a FastAPI application instance
app = FastAPI()  # This is the main API object that handles routes


# Define a simple health check endpoint
@app.get("/health")  # This decorator maps the function to the /health URL
def health_check():  # Function executed when /health is called
    return {"status": "OK"}  # Return a simple JSON response


# Define the main decision endpoint
@app.post("/decision", response_model=DecisionResponse)  # POST endpoint with validated response
def decision_endpoint(application: ApplicationRequest):  # Accepts validated ApplicationRequest
    # Call the decision service to process the application
    result = process_application(application.dict())  # Convert Pydantic model to dictionary

    # Return the result as a DecisionResponse model
    return DecisionResponse(**result)  # Unpack dictionary into the response model
