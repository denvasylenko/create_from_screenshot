# Screenshot to JSX Layout Generator

This project is a Python (backend) and React (frontend) application that takes a user-provided screenshot of a design, analyzes components with and generates responsive JSX code.

## Table of Contents

- Overview
- Key Features
- Installation
- Usage
- API Overview
- Frontend Components
- Example JSX Code
- Checklist
- Contributing
- License

## Overview
This project enables front-end developers to quickly transform design screenshots into JSX code for React projects by:

1. Uploading a screenshot image of a design.
2. Marking and providing bounding coordinates of components (e.g., header, buttons, forms).
3. Describing the functionality of each component.
4. Automatically generating JSX

## Key Features

- Component Extraction: Automatically extracts components from the screenshot based on user input.
- Customizable Component Marking: Users can manually mark the components and provide descriptions and functionalities.
- JSX Code Generation: Outputs clean, optimized JSX code for React projects.

## Installation
To install and run the application locally, follow the steps below:

### Prerequisites
- Python 3.x
- Node.js (latest version)
- React and Ant Design libraries
- ChatGPT API key (required for generating code)
- Backend Setup (Python)

**1. Clone the repository:**

```bash
git clone <repository-url>
cd screenshot-jsx-generator
```

**2. Install the Python dependencies:**

```bash
pip install -r requirements.txt
```

**3. Start the Python server:**


```bash
python app.py
```

### Frontend Setup (React)

**1. Navigate to the frontend folder:**

```bash
cd frontend
```


**2. Install the Node.js dependencies:**

```bash
npm install
```

**3. Start the React development server:**


```bash
npm start
```

###
