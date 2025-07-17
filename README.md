# 🩺 Diabetes Monitoring Dashboard

A healthcare web application that uses Machine Learning to predict diabetes risk and offers personalised lifestyle suggestions with the help of ChatGPT.

---

## 🌟 What Makes It Different?

This dashboard stands out from other diabetes prediction tools due to its focus on real-time interaction and meaningful feedback:

- 🔄 **Real-Time Data Input**: Users can fill in the required details on the go without needing lab reports or complex medical history.
- 📟 **IoT Integration**: The system connects with an IoT device to fetch real-time blood glucose readings.
- 💡 **Personalised Recommendations**: Beyond the prediction, the app provides tailored fitness and health suggestions for each user.
- 💬 **Built-in ChatGPT Support**: The dashboard includes ChatGPT to help users understand their results and get additional health insights. 😊

---

## 🧠 Model Overview

We’ve trained a Support Vector Machine (SVM) model using a simplified dataset (`Pima Indians Diabetes Dataset`) that focuses on the most essential parameters needed for diabetes prediction.

### 📊 Model Performance

- **Accuracy**: 77.27%
- **Precision**: 72.72%
- **Recall**: 58.18%
- **F1 Score**: 64.64%

This balance of precision and recall allows the model to make effective predictions with minimal input data.

---

## 📦 Requirements

To set up the application, install the required packages:

```bash
pip install -r requirements.txt
