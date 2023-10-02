from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import pydicom  # Import pydicom library
import numpy as np  # Import numpy library

app = FastAPI()

# Add a middleware for CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    try:
        # Read the uploaded DICOM file
        ds = pydicom.dcmread(file.file)

        # Extract pixel data from DICOM file
        pixel_array = ds.pixel_array
        pixel_array = pixel_array.astype(np.float32)  # Convert to float for normalization

        # Normalize pixel data to the range [0, 1]
        normalized_array = (pixel_array - pixel_array.min()) / (pixel_array.max() - pixel_array.min())

        # Apply thresholding (> 0.5)
        threshold = 0.5  # This could also be made configurable
        thresholded_array = normalized_array > threshold

        # Calculate the volume of the thresholded pixels
        voxel_volume = np.prod(ds.PixelSpacing) * ds.SliceThickness  # Voxel volume in mm^3
        volume = np.sum(thresholded_array) * voxel_volume  # Total volume in mm^3

        return {"volume": volume}  # Return the calculated volume

    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=400)
