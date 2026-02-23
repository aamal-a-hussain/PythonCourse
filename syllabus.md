 # Weekend 1: Python Fundamentals

- Variables
- Arithmetic
- Control Flow (If, Fors, Whiles, Match)
- Functions (Arguments, Variable Scoping)
- Collections (Lists, Dictionary, Tuples)

For the below, first do given data, then do user input, then a for-loop, then read from file

Simple Arithmetic
    - Might be worth doing a simple banking app simulator here:
        - Take in expenses from a file
        - Categorise them
        - Create a savings pot and implement a round-up savings function
        - Predict returns over time based on interest.


Data Analysis
    - https://www.kaggle.com/datasets/fungainicolechirombe/nhs-free-dataset-for-analysis
    
    - EDA
        - Plot AE Activity over time
        - Plot activity over time period
        - Time Average activity
        - Compute pct of patients who were seen within the NHS 4-hour target. Q: Are there any trends? Group by month and year.
        - Compute Did not attend rate
        
        - Plot volume of outpatient follow ups vs first appointments across specialties. Which one has the highest
        
        - Is there a correlation between higher DNA rates in outpatients and A&E attendances?

        - Determine the patient volume vs cost across specialties
        - Identify the 10% of trusts that have the lowest A&E wait times whilst also having a below average cost-per-patient
            - Can we identify what these trusts have in common? Size, Location, Specialty mix?


- Image Segmentation (CXR) https://www.kaggle.com/datasets/paultimothymooney/chest-xray-pneumonia
    
    - Cropping to a region of interest
    - Enhance detail by applying a log transform to the image
    - Gaussian blurring to reduce noise
    - Edge detection (e.g. Sobel)
    - use a threshold to identify lungs / heart
      - Possibly use this to obtain CTR




# Weekend 2: Object Oriented Programming

Extend the Patient database from the last one (which was dictionaries / csv) to a Patient Class
    - why is this useful? because we can add methods to the class

    As an example we can create a method which adds medication & vitals can be updated
    This can communicate with a server / frontend where a user can create their own patient profile, put in their vitals & check their medication.
        Students are required to create the necessary classes and methods.


Final Project: https://medshapenet.ikim.nrw/
    - We will have a pretrained 3d model that takes in a 3d scan of a skull with defects
        and outputs the coordinates of an implant that can fit that defect
        - the student will need to create a surgical plan that includes
            - The Patient id
            - The surgeon id
            - The skull obj

        - They will need to do some preprocessing on the skull object to pass it into the model
        - The model will output the implant

        - They will then need to check if the implant actually fits the hole

    - We can then create a bit of a surgical checklist based on patient medical history (e.g. comorbidities / medications, comparing volume of ai-generated implant to original bone fragment)

    Our frontend can display the skull & implant as well as a surgical checklist
        - We can make it so that the patient can see certain information if they login with their details & the surgeon can see other info if they login with their details
        - The student would have to create the logic to hide / show information.
