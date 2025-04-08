# **Dynamic Selection Hybrid Model for Enhanced Thyroid Disorder Diagnosis using BOOST Balancing Method in Machine Learning**

### **Overview**

The **Dynamic Selection Hybrid Model** is a **machine learning-driven system** designed to enhance **thyroid disorder diagnosis** by integrating **machine learning and data balancing techniques.**

- Addresses **class imbalances** using **BOOST balancing methods** to ensure **higher accuracy, adaptability, and reliability.**
- Dynamically selects the **most efficient classifiers** based on **Permutation Feature Importance (PFI) and ensemble techniques.**
- Optimizes diagnosis for both **Hyperthyroid** and **Hypothyroid** disorders.

This model ensures **precise and adaptable thyroid condition predictions** by leveraging a **hybrid selection approach** for classifier optimization.

---

## **Key Features**
✅ **Hybrid Model Selection:** EUses multiple ML models for precise classification.

✅ **BOOST Balancing Method:** Combines **SMOTE, Tomek Links, and AdaBoost** to handle imbalanced datasets.

✅ **Dynamic Selection Mechanism:** Selects the best-performing models based on **PFI scores**.

✅ **Secure User Authentication:** Allows registration and login for users.

✅ **User-Friendly Interface:** Web-based application for **uploading patient data and obtaining predictions.**

✅ **Thyroid Disorder Prediction:** Detects **Hyperthyroid and Hypothyroid conditions** with high accuracy

---

## **Tech Stack**
- **Programming Language:** Python, HTML, CSS, Bootstrap, JavaScript
- **Framework:** Flask
- **Database:** MySQL Server
- **Libraries:** Flask, Pandas, MySQL-Connector, Scikit-learn, NumPy
- **Dataset Source:** Thyroid Case Dataset from Kaggle
- **Server Deployment:** XAMPP Server
---

## **Installation & Setup**

### **1. Clone the Repository**
```sh
git clone <repository_url>
cd <repository_folder>
```

### **2. Open VS Code and Set Up Terminal**
- Open **VS Code**
- Open **Terminal** → **Run `cmd`** (to change from PowerShell to cmd)

### **3. Install Dependencies**
```sh
pip install flask
pip install scikit-learn
pip install pandas numpy seaborn
pip install tensorflow
pip install xgboost
pip install matplotlib
```

### **4. Install & Configure XAMPP server**
1. Download **XAMPP** from [here](https://www.apachefriends.org/download.html)
2. Open it and complete the installation setup.

### **5. Installing required dependencies for frontend**
1. Go the project folder and Navigate to the **FRONTEND** folder.
2. Open the command prompt in the FRONTEND folder and run
   ```sh
   code .
   ```
3. Open **VS Code**, select **app.py**, and open a new terminal.
4. Check if **Miniconda** is installed:
   ```sh
   conda -version
   ```
5. If not installed, run:
   ```sh
   conda create -n env python==3.10.14
   ```
6. Activate the environment:
   ```sh
   conda activate env
   ```
### **6.Set Up MySQL Database**
1. Open **XAMPP** server.
2. Start **Apache** and **MySQL** services.
3. In the **MySQL** section, click **Admin**, which opens **phpMyAdmin**.
4. Click **Import** and upload the **db.sql** file from the **FRONTEND** folder.

### **7. Run the Application**
1. Open the **FRONTEND** folder in **VS Code**.
2. Open a new terminal and run:
   ```sh
   conda activate env
   ```
3. Start the application:
   ```sh
   python app.py
   ```
---

## **Output & Usage**
1. **Login/Register** to access the platform.
2. Enter patient data.
3. Click **Submit**
4. We will finally get the Severeity of a tyroid disorder

---

## **Benefits**
✔ **Higher Accuracy** –Hybrid models improve prediction reliability.

✔ **Improved Diagnosis** – Machine learning techniques enhance medical assessments.

✔ **Better Data Handling** – Addresses class imbalance for fair predictions.

✔ **Scalable Solution** – Can be adapted for other medical conditions.

---

## **Contributors**  
**Team B6, Shri Vishnu Engineering College for Women (SVECW)**  

👩‍💻 **Md. Benazir Fathima**     - 21B01A05A8  

👩‍💻 **N. Neha**     - 21B01A05B3

👩‍💻 **N. Sai Ramya Sri** - 21B01A05B4

👩‍💻 **N. Lakshmi Priya**    - 21B01A05B9 

👩‍💻 **O. Pranathi Sudha**       - 21B01A05C7

