# Cartique AI : Enhanced Personalized Shopping Assistant

## Overview
**Cartique** is a innovative AI-powered Personalized Shopping Assistant built using NVIDIA’s Riva SDK. It offers an innovative, voice-enabled shopping experience that helps users discover products, receive personalized recommendations, and navigate an e-commerce platform effortlessly using voice commands. With Riva’s advanced natural language processing capabilities, Cartique adapts to user preferences and learns over time, making the shopping experience faster, smarter, and more intuitive.

## Features
- **Voice-Enabled Interaction**: Customers can use voice commands to explore products, get recommendations, and interact with the platform hands-free.
- **Personalized Recommendations**: Cartique continuously learns from user behavior to provide tailored product suggestions.
- **Real-Time Responses**: Powered by NVIDIA’s Riva SDK, Cartique ensures quick, real-time voice recognition and responses.
- **Seamless Shopping Experience**: Navigate the platform, add items to the cart, and make decisions without typing a single word.
- **Scalable and Efficient**: With AI learning, Cartique enhances the user experience with accuracy and speed.

## Installation & Setup

### Prerequisites
- Python 3.x
- NVIDIA Riva SDK
- AWS EC2 instance with GPU (for optimal performance)

### Steps
1. **Install dependencies:**
   - Set up your Python environment and install required packages:
     ```bash
     pip install -r requirements.txt
     ```

2. **Download NVIDIA Riva SDK**:
   - Follow the official [NVIDIA Riva SDK installation guide](https://developer.nvidia.com/riva) to download and set up the SDK on your instance.

3. **Configure AWS EC2**:
   - Launch an EC2 instance with NVIDIA P4 or A100 GPU for optimal performance.
   - Set up access to the instance and ensure it’s ready for deploying the AI model.

4. **Run the Cartique Application**:
   - Start the Flask application for the personalized shopping assistant:
     ```bash
     python app.py
     ```

5. **Access Cartique**:
   - Visit the application in your browser to interact with Cartique, either via voice or text.

## Usage
- **Start Voice Interaction**: Press the 'Start' button to begin speaking. Cartique will recognize your voice and respond with product recommendations or queries.
- **Product Discovery**: Ask Cartique to find specific products, or request personalized suggestions based on your shopping history.
- **Add to Cart**: Use voice commands to add products to your cart, view details, or navigate the site.

## Technology Stack
- **Backend**: Python, Flask
- **AI**: NVIDIA Riva SDK (for NLP and voice recognition)
- **Cloud**: AWS EC2 instances with GPU optimization (Amazon EC2 P4 instances)

## Contributing
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-xyz`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add new feature'`).
5. Push to the branch (`git push origin feature-xyz`).
6. Create a new pull request.

## License
Cartique is licensed under the MIT License. See the LICENSE file for more details.

## Contact
For inquiries, contact us at [info@viteefe.com](mailto:info@viteefe.com).
