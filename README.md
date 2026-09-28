# Run Instructions
1. Clone the repository:
   ```bash
   git clone
   ```
2. Navigate to the project directory:
   ```bash
   cd LinearRegressionArchitecture_Workshop
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Configure your environment variables in the `.env` file (e.g., database connection strings).
   Ensure ontario_housing_processed.csv and california_housing_processed.csv exist in the `data/processed` folder.
5. Set Experiment Parametsers in the `config/ontario_config.yaml` or `config/california_config.yaml` file.
6. Execute the pipeline and input which config file to use (default is `configs/ontario_config.yaml`):
   ```bash
   python run_pipeline.py configs/ontario_config.yaml
   or
   python run_pipeline.py configs/california_config.yaml
   ```
7. Review results: Open `experiments/ontario_results.csv` or `experiments/california_results.csv` to compare model performance metrics.


# 🏡 Linear Regression Architecture Workshop

## 🚀 High-Level Goal

This workshop bridges **theory and practice**, preparing students not only to understand linear regression, but also to work like professional ML engineers: building **reproducible**, **scalable**, and **well-architected** machine learning projects.

## Overview

The **Linear Regression Architecture Workshop** is designed for students to gain practical, hands-on experience with **machine learning fundamentals** and **MLOps design principles** in a structured, project-based learning environment.  

This workshop is built around a real-world use case: predicting **housing prices in California and Ontario** using **Univariate Linear Regression**. Students will move beyond simply coding models in a notebook—by also learning how to source, structure, and architect their projects with the same rigor used in professional machine learning workflows.  

The workshop is structured into **two sessions (2 hours each)**, with preparatory homework assignments before each session. By the end, students will not only understand how to implement Linear Regression, but also how to **design an experiment-ready ML project architecture**.

---

## 🎯 Learning Targets

By participating in this workshop, students will:

1. **Understand Univariate Linear Regression**  
   - Grasp the mathematical foundations (hypothesis function, cost function, gradient descent).  
   - Implement regression both **from scratch** and using libraries like `scikit-learn`.  
   - Evaluate model performance using RMSE, MAE, and \( R^2 \) metrics.  

2. **Develop Data Sourcing Skills**  
   - Load data from **CSV files**, **APIs**, and **Relational Databases**.  
   - Explore and clean real housing datasets.  
   - Perform exploratory data analysis (EDA) and visualization.  

3. **Learn ML Architecture & MLOps Patterns**  
   - Organize projects into modular components (`data_loader`, `preprocessing`, `model`, `evaluation`).  
   - Apply configuration-driven design using YAML files.  
   - Track experiments and ensure reproducibility.  
   - Practice setting up placeholders and stubs for future implementation sprints.  

4. **Build Professional Project Practices**  
   - Create a repository (`LinearRegressionArchitecture_Workshop`) with proper structure.  
   - Include `requirements.txt` for reproducibility and a well-documented `README.md`.  
   - Submit work in a professional format, simulating a real ML team workflow.  

---

## 🛠️ What Students Will Do

- **Before Session 1**: Source housing data from CSVs, APIs, and relational databases.  
- **During Session 1**: Implement and evaluate Univariate Linear Regression.  
- **After Session 1**: Refactor notebooks into modular Python scripts.  
- **Before Session 2**: Prepare configs and organize project folder structure.  
- **During Session 2**: Apply MLOps architecture and design patterns.  
- **After Session 2**: Extend the project with placeholders and stubs for future sprints.  

---

## 📂 Deliverables

- A **GitHub repository** titled:  LinearRegressionArchitecture_Workshop

The repository must contain:  
- A **frozen version of the codebase** (no changes after submission).  
- A `requirements.txt` file listing all Python dependencies.  
- A `README.md` file (this document) that clearly explains the workshop project.  
- An updated `RobotPM_MLOps.ipynb` notebook documenting architectural changes, recommended additions, and placeholders for future enhancements.
