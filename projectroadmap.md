# ScalpScan - Project Roadmap

## Codebase Exploration

### Repository Explored:
**GitHub Repo:** (https://github.com/pblgroupproject/ScalpSmart)

### Summary of Codebase:
This project uses a Convolutional Neural Network (CNN) to classify scalp images into healthy or alopecia-affected categories. The code includes:
- Dataset preprocessing using OpenCV
- Model training and evaluation
- Accuracy plotting and loss visualization
- Binary classification logic

### What Worked:
- I was able to clone the repository and run the preprocessing and training scripts after installing dependencies.
- The code is modular, with clearly defined functions for training and prediction.

### Challenges:
- The dataset used in the project is not publicly available, so I had to simulate inputs.
- Some outdated dependencies required updates (e.g., `tensorflow==1.x`).

### Applicability to ScalpScan:
- Useful as a starting point for our CNN model  
- Clear separation of training and inference pipelines  
- Will need to customize for multiclass classification (e.g., alopecia areata, CCCA, psoriasis)

### Next Steps:
- Adapt the CNN architecture for multiclass detection
- Train on more diverse datasets
- Integrate model with front-end interface
