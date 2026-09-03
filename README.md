Student Performance Prediction using AWS

📌 Overview

An end-to-end Machine Learning project that predicts student performance using Scikit-learn and Amazon SageMaker.

The model is stored in Amazon S3, deployed as a real-time SageMaker Endpoint, and exposed through AWS Lambda + API Gateway for prediction.

🏗️ Architecture

Frontend
   ↓
API Gateway
   ↓
AWS Lambda
   ↓
SageMaker Endpoint
   ↓
ML Prediction

Amazon S3 → Dataset & Model Storage

🛠️ Technologies

- Python
- Pandas & NumPy
- Scikit-learn
- AWS S3
- AWS SageMaker
- AWS Lambda
- API Gateway
- HTML, CSS & JavaScript
- Postman
- Git & GitHub

🔄 Workflow

1. Store dataset in Amazon S3
2. Preprocess and train ML model
3. Deploy model on SageMaker
4. Create real-time endpoint
5. Connect Lambda with SageMaker
6. Expose prediction API using API Gateway
7. Test using Postman and Frontend

🎯 Result

The application accepts student details and returns the predicted performance through a real-time AWS API.

👨‍💻 Author

Sameer Kumar
B.Tech CSE | Machine Learning | AWS | Python
