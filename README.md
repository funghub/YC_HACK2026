# Drug Discovery Web Application

This repository contains the source code for a web application developed for the YC Bio x AI Hackathon on March 8th, 2026. The application provides a platform for computational drug discovery, allowing users to analyze protein-ligand interactions, predict novel ligand candidates, and review detailed ADMET (Absorption, Distribution, Metabolism, Excretion, and Toxicity) prediction scores.

## Project Description

Our team leveraged bioinformatics machine learning tools (DrugFlow, PLACER, and ADMET-AI) to build a centralized platform that helps researchers evaluate generated ligand compounds and identify the most promising candidates for further research and development.
 
In addition, AI and bioinformatics tools are powerful, but they’re often hard for new scientists to access and interpret. Navigating multiple platforms, understanding outputs, and connecting results into meaningful insights can create a steep learning curve during the drug discovery process.

Our solution: a centralized platform that simplifies early-stage drug exploration.

🔬 What we built
- A dashboard that analyzes proteins and ligands from just two inputs: PDB and SDF files
- Interactive 3D visualization of protein–ligand structures using 3Dmol.js
- Integration with Tamarind.bio’s API to generate novel ligand candidates for a protein target, predict protein-ligand docking, and ADMET predictions. 


⚙️ Under the hood
- Tamarind API powering ligand generation (DrugFlow), protein–ligand modeling (PLACER), and ADMET-AI predictions to evaluate compound safety compared to approved DrugBank drugs
- RDKit to convert SDF → SMILES
- Next.js + React frontend
- Convex backend for serverless functions and data

💡 Why this matters
Our goal was to lower the barrier to computational drug discovery by:
- Centralizing multiple bioinformatics tools
- Explaining tools and results in a way that new researchers can understand
- Helping scientists identify promising compounds faster during the exploratory phase of research.

## Key Features

-   **Protein & Ligand Upload:** Users can upload protein (PDB) and ligand (SDF) files to initiate an analysis.
-   **3D Visualization:** Interactive 3D visualization of protein and ligand structures using 3Dmol.js.
-   **Alternate Ligand Prediction:** Integration with the Tamarind.bio API to submit jobs and predict alternative ligands for a given protein target.
-   **Result Retrieval & Display:** Fetch and display prediction results, including novel ligand structures.
-   **Sample Report Page:** A comprehensive demo page (`/demo`) showcasing the application's analysis and visualization capabilities with sample data.
-   **ADMET Score Analysis:** Download detailed CSV reports of ADMET prediction scores for generated ligands.
    - convert .sdf files to SMILES with RDKit
    - access Tamarind API to utilize ADMET-AI for scores analysis and generate a saftey summary plot of molecule’s predicted ADMET property ranks compared to all approved drugs on DrugBank

## Tech Stack

This project leverages a modern, full-stack serverless architecture:

-   **Backend & Database:** [**Convex**](https://www.convex.dev/) is used for the backend logic, real-time database, and file storage. All API interactions and data mutations are handled through Convex functions.
-   **Computation & Biological Models:** [**Tamarind.bio**](https://www.tamarind.bio/) provides the core computational power for predicting alternate ligands and running complex biological simulations.
-   **Frontend Framework:** [**Next.js**](https://nextjs.org/) (with the App Router) and [**React**](https://react.dev/) are used to build the user interface.
-   **3D Molecular Visualization:** [**3Dmol.js**](https://3dmol.csb.pitt.edu/) is used for rendering interactive 3D structures of proteins and ligands directly in the browser.

## Sample UI

![alt text](image.png)


Refer this URL for the sample demo : [https://bioaihack.eshan.dev/demo](https://bioaihack.eshan.dev/demo)


## Getting Started

1.  **Clone the repository:**
    ```bash
    git clone <repository-url>
    ```
2.  **Install dependencies:**
    ```bash
    npm install
    ```
3.  **Set up Convex:**
    -   Follow the Convex documentation to initialize the project and deploy the backend functions.
    -   Add the required Tamarind.bio API key and email to your Convex project's environment variables.
4.  **Run the development server:**
    ```bash
    npm run dev
    ```
5.  Open [http://localhost:3000](http://localhost:3000) with your browser to see the result.
