from pydantic import BaseModel, Field, StrictInt, StrictFloat

class InputSchema(BaseModel):
    longitude: StrictFloat = Field(..., description="Longitude")
    latitude: StrictFloat = Field(..., description="Latitude")
    housing_median_age: StrictFloat = Field(..., gt=0, description="Housing Median Age")
    total_rooms: StrictFloat = Field(..., gt=0, description="Total Rooms")
    total_bedrooms: StrictFloat = Field(..., gt=0, description="Total Bedrooms")
    population: int = Field(..., gt=0, description="Population")
    households: StrictInt = Field(..., gt=0, description="Households")
    median_income: StrictFloat = Field(..., gt=0, description="Median Income")

class OutputSchema(BaseModel):
    predicted_price: StrictFloat = Field(..., description="Predicted House Price")