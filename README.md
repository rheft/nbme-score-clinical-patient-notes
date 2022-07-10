## NMBE Scoring of Clinical Patient Notes
This project is a companion to a kaggle project here: https://www.kaggle.com/code/robheft/clinical-patient-note-scoring-nbme-v1  

## Problem Overview
Overview taken from the [competition description](https://www.kaggle.com/c/nbme-score-clinical-patient-notes)  

When you visit a doctor, how they interpret your symptoms can determine whether your diagnosis is accurate. By the time they’re licensed, physicians have had a lot of practice writing patient notes that document the history of the patient’s complaint, physical exam findings, possible diagnoses, and follow-up care. Learning and assessing the skill of writing patient notes requires feedback from other doctors, a time-intensive process that could be improved with the addition of machine learning.

Until recently, the Step 2 Clinical Skills examination was one component of the United States Medical Licensing Examination® (USMLE®). The exam required test-takers to interact with Standardized Patients (people trained to portray specific clinical cases) and write a patient note. Trained physician raters later scored patient notes with rubrics that outlined each case’s important concepts (referred to as features). The more such features found in a patient note, the higher the score (among other factors that contribute to the final score for the exam).

However, having physicians score patient note exams requires significant time, along with human and financial resources. Approaches using natural language processing have been created to address this problem, but patient notes can still be challenging to score computationally because features may be expressed in many ways. For example, the feature "loss of interest in activities" can be expressed as "no longer plays tennis." Other challenges include the need to map concepts by combining multiple text segments, or cases of ambiguous negation such as “no cold intolerance, hair loss, palpitations, or tremor” corresponding to the key essential “lack of other thyroid symptoms.”

In this competition, you’ll identify specific clinical concepts in patient notes. Specifically, you'll develop an automated method to map clinical concepts from an exam rubric (e.g., “diminished appetite”) to various ways in which these concepts are expressed in clinical patient notes written by medical students (e.g., “eating less,” “clothes fit looser”). Great solutions will be both accurate and reliable.

If successful, you'll help tackle the biggest practical barriers in patient note scoring, making the approach more transparent, interpretable, and easing the development and administration of such assessments. As a result, medical practitioners will be able to explore the full potential of patient notes to reveal information relevant to clinical skills assessment.

This competition is sponsored by the National Board of Medical Examiners® (NBME®). Through research and innovation, NBME supports medical school and residency program educators in addressing issues around the evolution of teaching, learning, technology, and the need for meaningful feedback. NBME offers high-quality assessments and educational services for students, professionals, educators, regulators, and institutions dedicated to the evolving needs of medical education and health care. To serve these communities, NBME collaborates with a diverse and comprehensive array of practicing health professionals, medical educators, state medical board members, test developers, academic researchers, scoring experts and public representatives.

NBME gratefully acknowledges the valuable input of Dr Le An Ha from the University of Wolverhampton’s Research Group in Computational Linguistics.


## Approach
1. EDA
2. Try a logic/hueristic approach first, it may just work. Worst case scenario, we now have a baseline to compare to.  
3. If the baseline approach doesn't quite work, move onto more complicated solutions. This typically starts with at least some research into the problem space, to find similar problems and how those have been "solved".
4. Apply the research in step 2 to our problem. In this case, I attempt to use Token Classification to learn the many different ways `features` in this dataset can be written. At the time of writing this, I haven't quite trained a model to be robust enough to improve on our baseline.  
5. Repeat steps 3/4 until I've built a competitive system, or I've ran out of time.  


## API
Any solution to a data science problem is a time (and comptue resource) expensive virtual paper weight without a way to enable others to use it. I put together a small API using the [FastAPI Framework](https://fastapi.tiangolo.com/) to showcase how easy it can be to make a model available. Currently only the baseline approach has an endpoint in the API since we haven't had another competitive approach.  


## Setup
1. `git clone <repo url>`  
2. `cd nbme-score-clinical-patient-notes/`
3. (Although not required, its highly recommended) Enable a Python Virual Environment  
4. `pip install -r requirements.txt`  
5. `uvicorn app.main:app --reload` to start the API
6. Navigate to `http://127.0.0.1:8000/docs` to read up on the the API is offering, or to test it out.  

## Other
Note 1: Kaggle requires terms to be agreed to in order to access the data. Although its likely not an issue to share it here, I haven't. In order to execute cells in the `eda_and_basline.ipynb` notebook, you'll need to download the data from the competition here: https://www.kaggle.com/competitions/nbme-score-clinical-patient-notes/data and put the resulting files in the `data/` directory.  