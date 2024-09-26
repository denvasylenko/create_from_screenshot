from flask import Flask, request, jsonify
import openai
import base64
from io import BytesIO
from PIL import Image
from flask_cors import CORS  # Import flask_cors
from dotenv import load_dotenv
import os

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Initialize OpenAI with your API key
openai.api_key = os.getenv("CHATGPT_API_KEY")

@app.route('/generate', methods=['POST'])
def generate():
    try:
        print(request)
        if 'image' not in request.files:
            return jsonify({"error": "Image is required"}), 400

        # Retrieve the image file
        image_file = request.files['image']
         # Get the text data
        image_design_examples = request.form.get('imageDesignExamples')
        jsx_examples = request.form.get('jsxExamples')
        components_api_description = request.form.get('componentsAPIDescription')
        grid_system_examples = request.form.get('gridSystemExamples')

        print("request.files : ", request.files)
        # Open the image and convert to base64
        image = Image.open(image_file)
        buffered = BytesIO()
        image.save(buffered, format="PNG")
        img_base64 = base64.b64encode(buffered.getvalue()).decode('utf-8')

        prompt = f"""
            Instruction:

            You are a skilled Front-End Developer tasked with transforming a design image into JSX code for a React project. 
            Follow the steps below to ensure the JSX output adheres to best practices, uses a grid layout, and is responsive to different screen sizes.

            Step-by-Step Plan:

            Analyze the Design:

            - Break down the design image into distinct components (e.g., header, sections, buttons, forms).
            - Identify spacing, alignment and how components fit together.

            Choose a Grid System:

            - Select the appropriate grid system based on user input.
            - Ensure components are placed within the grid correctly (e.g., based on the grid structure provided by the user).

            Component Hierarchy:

            - Establish the parent-child relationships between components, ensuring nested elements are structured logically.

            -----------

            ### User Inputs:
            **Image(s) Design Examples**: {image_design_examples}
            **JSX Examples**: {jsx_examples}
            **Components API Description**: {components_api_description}
            **Grid System Examples**: {grid_system_examples}        
        
        """

        # Call the OpenAI API (GPT-4)
        # response = openai.Completion.create(
        #     engine="gpt-4o",  # Use the GPT-4 engine
        #     prompt=prompt,
        #     max_tokens=150,  # Adjust token length as needed
        #     temperature=0.7,  # Adjust creativity of response
        # )
        response = openai.chat.completions.create(
            model="gpt-4o",  # Use GPT-4 model
            messages=[
                {"role": "system", "content": prompt},
                {
                "role": "user",
                "content": [
                        {
                            "type": "text",
                            "text": """
                                Use only JSX in your response.
                                Ensure the output is responsive and properly follows a grid layout using Ant Design.
                                Include all necessary imports and components in the JSX code.
                                Follow best practices for structuring the form elements.
                                Do not provide any explanations or extra comments, only the JSX code.
                                Output only the JSX code without wrapping it in "jsx" or "" notation. Just return the JSX content directly.
                            """
                        },
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": f"data:image/jpeg;base64,{img_base64}"
                            }
                        }
                    ]
                },
            ]
        )

        # Get the response text
        generated_text = response.choices[0].message.content.strip()

        return jsonify({"generated_text": generated_text}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)



# Instruction:

#             You are a skilled Front-End Developer tasked with transforming a design image into JSX code for a React project. 
#             Follow the steps below to ensure the JSX output adheres to best practices, uses a grid layout, and is responsive to different screen sizes.

#             Step-by-Step Plan:
#             Analyze the Design:

#             Break down the design image into distinct components (e.g., header, sections, buttons, forms).
#             Identify spacing, alignment (e.g., padding, margins), and how components fit together.
#             Choose a Grid System:

#             Select the appropriate grid system for the project (you will use ONLY ant design system).
#             Ensure components are placed within the grid correctly (e.g., col-6 for half-width elements).
#             Component Hierarchy:

#             Establish the parent-child relationships between components, ensuring nested elements are structured logically.
#             Ensure Consistent Spacing:

#             Use CSS utility classes or custom styles to match margins and padding from the design.
#             Responsive Design:

#             Ensure the layout works on various screen sizes, following responsive design principles.
#             Example Implementation:
#             Let’s assume the design includes:

#             A header with a logo and navigation links.
#             A main section with an image and text.
#             A footer with centered text.

#             import React from 'react';
#             import 'bootstrap/dist/css/bootstrap.min.css';

#             import React from 'react';
#             import {{ Row, Col, Input, Select, Button }} from 'antd';

#             const {{ Option }} = Select;

#             const FormWithGrid = () => {{
#             return (
#                 <div className="form-container">
#                     <Row gutter={[16, 16]}>
#                         {{/* Field 0 */}}
#                         <Col span={8}>
#                         <label>
#                             <span style={{ color: 'red' }}>*</span> Field 0:
#                         </label>
#                         <Input placeholder="placeholder" />
#                         </Col>

#                         {{/* Field 1 */}}
#                         <Col span={8}>
#                         <label>
#                             <span style={{ color: 'red' }}>*</span> Field 1:
#                         </label>
#                         <Select placeholder="longlonglonglonglonglonglonglong" style={{ width: '100%' }}>
#                             {{/* Add options here */}}
#                             <Option value="1">Option 1</Option>
#                             <Option value="2">Option 2</Option>
#                         </Select>
#                         </Col>

#                         {{/* Field 2 */}}
#                         <Col span={8}>
#                         <label>
#                             <span style={{ color: 'red' }}>*</span> Field 2:
#                         </label>
#                         <Input placeholder="placeholder" />
#                         </Col>

#                         {{/* Field 3 */}}
#                         <Col span={8}>
#                         <label>
#                             <span style={{ color: 'red' }}>*</span> Field 3:
#                         </label>
#                         <Input placeholder="placeholder" />
#                         </Col>

#                         {{/* Field 4 */}}
#                         <Col span={8}>
#                         <label>
#                             <span style={{ color: 'red' }}>*</span> Field 4:
#                         </label>
#                         <Select placeholder="longlonglonglonglonglonglonglong" style={{ width: '100%' }}>
#                             {{/* Add options here */}}
#                             <Option value="1">Option 1</Option>
#                             <Option value="2">Option 2</Option>
#                         </Select>
#                         </Col>

#                         {{/* Field 5 */}}
#                         <Col span={8}>
#                         <label>
#                             <span style={{ color: 'red' }}>*</span> Field 5:
#                         </label>
#                         <Input placeholder="placeholder" />
#                         </Col>

#                         {{/* Buttons */}}
#                         <Col span={24} style={{ display: 'flex', justifyContent: 'flex-start', alignItems: 'center', marginTop: '16px' }}>
#                         <Button type="primary" style={{ marginRight: '10px' }}>Search</Button>
#                         <Button>Clear</Button>
#                         <a href="#" style={{ marginLeft: 'auto' }}>Collapse</a>
#                         </Col>
#                     </Row>
#                     </div>
#                 );
#             }};

#             export default FormWithGrid;

#             Final Review:
#             Header: The logo and navigation links are properly aligned in a two-column grid.
#             Main Section: The image and text each take half the available width and stack vertically on smaller screens (using col-md-6).
#             Footer: Spans the full width and is centered.
#             Responsive: The layout is adaptable to different screen sizes thanks to Bootstrap's grid.
#             Checklist Before Completion:
#             Grid layout is implemented correctly.
#             Spacing (margins, padding) is consistent with the design.
#             The layout is responsive for smaller screens.
#             Ensure custom adjustments based on the specific design requirements.