### DicomApp
DicomApp is a web-based platform that allows users to upload a DICOM image. Upon upload, the pixel data of the DICOM are extracted, normalized, and thresholded. After processing, the system displays the volume (in mm³) of the thresholded pixels.

### Technologies Used
Frontend: Vue.js
Backend: FastAPI (Python)
Containerization: Docker
DICOM Processing: pydicom
### How to Run the Application
How to Run the Application
Prerequisites
Docker: Ensure Docker is installed. You can download it from Docker’s official website.
Docker Compose: It’s included in the Docker Desktop installation.
Steps to Run
Clone the Repository
Open a terminal (Command Prompt, PowerShell, or a Unix-based terminal) and run:
git clone <repository-url>
cd <repository-dir>
Build and Run Docker Containers
Navigate to the project directory (if not already there) and run:
docker-compose up --build
This command will build and start the frontend and backend containers. You will see log outputs on the terminal indicating the progress.
Access the Application
Once the containers are up and running without errors, open a web browser.
Navigate to the frontend service URL, typically:
http://localhost:8080
Interacting with Backend API
To send manual requests to the backend, I used  Postman 

### Testing
I Used the provided DICOM file 1-101.dcm for testing.
The expected volume is ~143,280.029 mm³.
### Future Improvements
Enhanced error handling for corrupt or invalid DICOM files.
Optimize Docker container resources and build times.
Enhance UI/UX for better user interaction.
### Conclusion
This project provides a simple and effective way to calculate the volume of thresholded pixels in DICOM images, helping medical professionals to analyze medical images efficiently.

### Customize configuration
See [Configuration Reference](https://cli.vuejs.org/config/).
