Nursing Wizard of Oz Simulation

This is a Wizard of Oz prototype using Streamlit to simulate a rule-based nursing decision support tool.

Features:

- Simulates nurse workflow following the Nursing Process:  
  (Assessment → Diagnosis → Outcomes Identification → Planning → Implementation → Evaluation)

- Integrated with the Morse Fall Scale to assess and guide fall risk intervention

- Grounded in the Georgia 2023 Public Health Nurse Protocols for contextual justification

- Designed to support research into trust and plausibility in clinical decision support  
  (Pre-ML/XAI phase using rule-based logic)

- Outputs rule-based justifications aligned with the XAIR framework 


Purpose: 

This prototype is part of a research study on Explainable AI (XAI) in healthcare (XAIR framework), HAII, and simulation of contextual reasoning.

How to Run:

1. Clone or download this repo
2. Install dependencies: pip install streamlit
3. Launch the app: python –m streamlit run nursing_process_morse_only.py

References

- Bienefeld, N., Antons, D., Wenzel, M., & Schilling, M. A. (2023). Solving the XAI conundrum: When and how to enhance user trust by making artificial intelligence explainable. *Journal of Management, 49*(2), 553–584. https://doi.org/10.1177/01492063221136846

- Georgia Department of Public Health. (2023). *Standard nurse protocols for registered professional nurses in public health*. https://dph.georgia.gov/nursing/nursing-protocols

- Monks, T., & Harper, A. (2023). Improving the usability of open health service delivery simulation models using Python and web apps. NIHR open research, 3, 48.

- Xu, J., He, C., Liu, X., Yin, Y., Yang, Y., & Zhang, J. (2023). XAIR: A framework of explainable AI in augmented reality. *Computers in Industry, 146*, 103819. https://doi.org/10.1016/j.compind.2023.103819

- Zhu, X., Panigrahi, A., & Arora, S. (2025). On the power of context-enhanced learning in LLMs. *Proceedings of the 42nd International Conference on Machine Learning (ICML)*. https://arxiv.org/abs/2503.01821

- Morse Fall Scale: https://www.ahrq.gov/patient-safety/settings/hospital/fall-prevention/toolkit/morse-fall.html

